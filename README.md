# app_jfduke3d

[JFDuke3D](https://github.com/jonof/jfduke3d) - Jonathon Fowler's port of Duke Nukem 3D - packaged as an
[AutoBleem](https://github.com/autobleem2/autobleem) App for the PlayStation Classic, the Raspberry Pi, the
AutoBleem PC stick and Windows, with the v1.3d shareware episode. Install it from the AutoBleem Store.

The upstream source is a pinned submodule; this repository holds only the build (`ci/build.sh`, run in the
[autobleem-build](https://github.com/autobleem2/autobleem-build) image), three small patches (the PlayStation
Classic pad layout, and no setup window when started with `-nosetup`) and the App's files.

```
git clone --recurse-submodules https://github.com/autobleem2/app_jfduke3d
ci/build.sh all    # inside ghcr.io/autobleem2/autobleem-build
```

Controls (PlayStation Classic pad): D-pad move and turn, Cross fire, Circle crouch, Triangle jump, Square open
(twice: kick), L1 next item (twice: use), R1 next weapon, L2/R2 strafe, Select map, Start menu. Press Reset on
the console or hold Start + Select to leave.

Licence: the build, patches and tools GPL-3.0-or-later, JFDuke3D GPL-2.0 with the Build engine under Ken
Silverman's licence; the shareware episode is freely distributable (see `LICENSE`).
