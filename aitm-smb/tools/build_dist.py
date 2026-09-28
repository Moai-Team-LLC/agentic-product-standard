#!/usr/bin/env python3
"""Build the AITM-SMB Core and Full distributions.

Core = MANIFEST.md `canonical_core` + `registries` + LICENSE + CHANGELOG.md.
Full = every file under the AITM-SMB root (except build output and caches).

Writes dist/aitm-smb-core-<version>.zip and dist/aitm-smb-full-<version>.zip.
Both unpack into a single `aitm-smb-<version>/` folder. Standard library only.
"""
import argparse
import os
import sys
import zipfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from validate import ROOT, manifest, rel  # noqa: E402

SKIP_DIRS = {".git", "dist", "__pycache__", "node_modules"}
SKIP_FILES = {".DS_Store", "Thumbs.db"}
# Zip timestamps are pinned so identical inputs give identical archives.
FIXED_TIME = (2026, 1, 1, 0, 0, 0)


def full_files():
    out = []
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = sorted(d for d in dirnames if d not in SKIP_DIRS)
        for name in sorted(filenames):
            if name in SKIP_FILES or name.endswith(".pyc"):
                continue
            out.append(rel(os.path.join(dirpath, name)))
    return out


def core_files(man):
    wanted = list(man.get("canonical_core") or []) + list(man.get("registries") or [])
    wanted += ["LICENSE", "CHANGELOG.md"]
    missing = [p for p in wanted if not os.path.isfile(os.path.join(ROOT, p))]
    if missing:
        raise SystemExit("core files missing: %s" % ", ".join(missing))
    seen, out = set(), []
    for p in wanted:
        if p not in seen:
            seen.add(p)
            out.append(p)
    return out


def write_zip(path, files, folder):
    with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as zf:
        for f in files:
            info = zipfile.ZipInfo("%s/%s" % (folder, f), FIXED_TIME)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = (0o755 if f.startswith("tools/") and f.endswith(".py") else 0o644) << 16
            with open(os.path.join(ROOT, f), "rb") as fh:
                zf.writestr(info, fh.read())


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--out", default=os.path.join(ROOT, "dist"), help="output directory (default: dist/)")
    args = parser.parse_args(argv)

    man = manifest()
    version = man.get("version")
    if not version:
        raise SystemExit("MANIFEST.md has no framework version")
    os.makedirs(args.out, exist_ok=True)
    folder = "aitm-smb-%s" % version
    for kind, files in (("core", core_files(man)), ("full", full_files())):
        target = os.path.join(args.out, "aitm-smb-%s-%s.zip" % (kind, version))
        write_zip(target, files, folder)
        print("%s: %d files -> %s" % (kind, len(files), os.path.relpath(target)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
