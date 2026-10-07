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
- **Upstream**: `jonof/jfduke3d` pinned at tag `20260105` (nested submodules). Package version `20260105-3`.
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
| `patches/jfduke3d/0004-psc-stick-sensitivity.patch` | **the console build only** (`-DAB_PSC`, `target_psc`): the turning axis (0, `analog_turning`) defaults to a scale of **0.1** (6554) instead of 1.0, the other axes keep 1.0. The console's own pad has no stick - the virtual pad turns its D-pad into the left stick at full deflection, and at 1.0 it turned far too fast (the owner, 2026-09-25, from `20260105-2`). A pad with a real stick wants more - the game keeps one value for every pad, so the console build defaults to its own pad's. A config saved before keeps its value (Options -> Joystick setup). |
| `resources/` | `app.ini` (`Exec=bin/{key}/duke3d`, `Args=-nosetup`, `VirtualPad=true`), `readme.txt`, `icon.png` |
| `ci/build.sh` | JFSW's, for `duke3d` - see there |
| `tools/make_icon.py` | the icon from the title screen, BETASCREEN (tile 2493) - **in the title palette** (LOOKUP.DAT's third palette, after the shade tables and the water and slime palettes, as `astub.c` reads it); the game palette gives wrong colours |
| `tools/store_item.py` | as in the other ports |
| `/opt/ab/tools/check_psc_binary.sh`, `/opt/ab/tools/check_needed.sh` (autobleem-build image) | no longer vendored (APPS-6) - as in the other ports |

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
- **Category** (the owner, 2026-10-07): every `app.ini` carries `Category=games` (the launcher's Apps tab files an App by it: games, emulators, tools, media, other - any case) and `tools/store_item.py` writes `"category": "games"` into the Store item.
- **Releases**: a `v<version>` tag (`v20260105-1`) builds a stable GitHub release (in the release image);
  `master` follows the released commit. The Store gets it by hand: `gh release download <tag>`,
  `tools/store_item.py` per zip, then autobleem-repo's `repo_publish.sh store <key> dist/store/<key>/*`.
  v20260105-1 went to all five catalogs on 2026-09-25, replacing the RetroBoot EDuke32 on psc.
- **Not yet run**: on a console, a Pi or the PC stick (the tester checklist, section 12). An early build
  (-1) was started on a console on 2026-09-25; the fault found there is fixed in -2 (`7868a5d`, the turning
  axis), which has not run on a console yet.
