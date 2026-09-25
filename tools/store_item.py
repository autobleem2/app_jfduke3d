#!/usr/bin/env python3
"""Write the AutoBleem Store's descriptor for one platform's package (autobleem-repo CLAUDE.md, "The AutoBleem
Store's catalog"), next to the package and the picture, ready for `repo_publish.sh store <platform> ...`:

    tools/store_item.py dist/eduke32-psc-20260105-1.zip  -> dist/store/psc/eduke32.item.json
                                                                        + eduke32.png + the zip

The id is the same on every platform (app/eduke32 - the RetroBoot App's id, updated in place), so an installed App is updated in place.
Only the standard library is needed.
"""
import json
import os
import re
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)

DESCRIPTION = ("L.A. Meltdown, the shareware episode of Duke Nukem 3D (1996), through JFDuke3D - Jonathon "
               "Fowler's port of the original source. Built for this machine; the pad out of the box.")


def main(argv):
    if len(argv) != 2:
        print(__doc__)
        return 2
    package = argv[1]
    m = re.match(r"^eduke32-(?P<key>[a-z0-9]+)-(?P<version>.+)\.zip$", os.path.basename(package))
    if not m:
        print("not an eduke32-<key>-<version>.zip: %s" % package)
        return 1
    key, version = m.group("key"), m.group("version")
    out = os.path.join(os.path.dirname(package), "store", key)
    os.makedirs(out, exist_ok=True)
    shutil.copy(package, out)
    shutil.copy(os.path.join(ROOT, "resources", "icon.png"), os.path.join(out, "eduke32.png"))
    item = {
        "id": "app/eduke32",
        "kind": "app",
        "title": "Duke Nukem 3D (Shareware)",
        "version": version,
        "author": "JFDuke3D by Jonathon Fowler; Duke Nukem 3D by 3D Realms",
        "licence": "GPL-2.0 (the Build engine: Ken Silverman's licence; the shareware data: freely distributable)",
        "description": DESCRIPTION,
        "image": "eduke32.png",
        "files": [{"name": os.path.basename(package)}],
    }
    with open(os.path.join(out, "eduke32.item.json"), "w", encoding="utf-8") as f:
        json.dump(item, f, indent=2)
        f.write("\n")
    print(out)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
