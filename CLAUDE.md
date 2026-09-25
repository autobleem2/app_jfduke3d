# app_jfduke3d - developer context

**JFDuke3D** (Jonathon Fowler's port of Duke Nukem 3D) packaged as an AutoBleem App with the v1.3d shareware
episode: `Apps/eduke32/`, Store id `app/eduke32` - the folder and id of the 2020 EDuke32 App it replaces, so the
Store updates it in place - one zip per platform (`dist/eduke32-<key>-<version>.zip`). Started 2026-09-25, the
sixth third-party App port (autobleem-main `docs/decisions.md`, "Third-party App ports" - the rules). It is
`app_jfsw`'s twin: same author, same engine (jfbuild/jfmact/jfaudiolib), same build, same three patches - read
`app_jfsw`'s CLAUDE.md for the details this file does not repeat.

## The owner's decisions for this port (2026-09-25)

- **JFDuke3D, not EDuke32** (what the 2020 App was): the JFSW family - a known build and known patches,
  the original game faithfully - over EDuke32's much bigger C++ build with no releases.
- **Upstream**: `jonof/jfduke3d` pinned at tag `20260105` (nested submodules). Package version `20260105-1`.
- **The 2020 layout, as far as a button-per-function config allows** (`0001-psc-pad-layout.patch`): Cross fire,
  Circle crouch, Triangle jump, Square open (double: Quick_Kick), Select map (double: AutoRun), Start menu, **L1
  next inventory item (double: use it), R1 next weapon** (the owner's choice - 2020's "hold L1/R1 + D-pad" has no
  equivalent here, and the console's pad gets weapon switching it lacked), L2/R2 strafe, the D-pad move/turn,
  right stick strafe + look up/down. EDuke32's alt fire does not exist in the original game.
- **The software renderer everywhere; Windows is upstream's native Win32 build** (as JFSW).

## Layout

| path | what |
|---|---|
| `upstream/jfduke3d` | the pinned upstream source (submodule, with nested submodules) |
| `patches/jfduke3d/0001-psc-pad-layout.patch` | the default pad tables in `src/_functio.h` (above) |
| `patches/jfduke3d/0002-nosetup-on-the-first-start.patch`, `0003-no-start-window-with-nosetup.patch` | as JFSW's: `-nosetup` wins on the first start, and no start window at all |
| `resources/` | `app.ini` (`Exec=bin/{key}/duke3d`, `Args=-nosetup`, `VirtualPad=true`), `readme.txt`, `icon.png` |
| `ci/build.sh` | JFSW's, for `duke3d` - see there |
| `tools/make_icon.py` | the icon from the title screen, BETASCREEN (tile 2493) - **in the title palette** (LOOKUP.DAT's third palette, after the shade tables and the water and slime palettes, as `astub.c` reads it); the game palette gives wrong colours |
| `tools/store_item.py`, `tools/check_psc_binary.sh`, `tools/check_needed.sh` | as in the other ports |

## Things to know

- **The data**: `mirror/jfduke3d/duke3d-shareware-1.3d.zip` (duke3d.grp from the 2020 package; CRC32 0x983AD923 is
  JFDuke3D's "Shareware Version" in `grpscan.c`).
- **Portable mode** (`user_profiles_disabled` in the App folder): `duke3d.cfg`, the saves, `grpfiles.cache` and
  `duke3d.log` in the App folder.
- **Windows**: run on the dev PC on 2026-09-25 from a fresh folder - straight into the game, full screen, 4:3,
  no setup window (the owner watched).
- **Build on the server**: sync with MSYS2's rsync (excluding `/build_*`, `/dist`), then
  `docker run --rm -u $(id -u):$(id -g) -v $PWD:/src -w /src ghcr.io/autobleem2/autobleem-build:develop ci/build.sh all`;
  delete what it left once finished (autobleem-main `docs/decisions.md`).
- **Releases**: a `v<version>` tag (`v20260105-1`) builds a stable GitHub release (in the release image);
  `master` follows the released commit. The Store gets it by hand: `gh release download <tag>`,
  `tools/store_item.py` per zip, then autobleem-repo's `repo_publish.sh store <key> dist/store/<key>/*`.
  v20260105-1 went to all five catalogs on 2026-09-25, replacing the RetroBoot EDuke32 on psc.
- **Not yet run**: on a console, a Pi or the PC stick (the tester checklist, section 12).
