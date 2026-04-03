# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Running the Game

```bash
python main.py
```

Run the sprite viewer (debug tool for verifying sprite frames):
```bash
python debug_sprite_viewer.py
```

## Controls

- **Arrow keys** — move left/right
- **M** — jump

## Architecture

The game uses a flat module structure with no package `__init__.py` files. All imports use full dotted paths (e.g. `import data.constants as const`).

**Entry point:** `main.py` → instantiates `states/app.py:GameManager` and calls `main_loop()`.

**Game loop flow:**
```
GameManager.main_loop()
  → pygame.key.get_pressed()
  → Level.run(keys)
      → active_sprites.update()       # Goombas, Mushrooms (no keys needed)
      → player.update(keys)           # Mario (needs keys)
      → visible_sprites.custom_draw(player)  # CameraGroup handles offset
```

**Sprite groups (all in `Level`):**
- `visible_sprites` — `CameraGroup` instance; all sprites join this for rendering
- `active_sprites` — enemies/items that self-update each frame
- `collision_sprites` — static `Block` tiles that other sprites collide against

Mario is intentionally **not** in `active_sprites` — his `update(keys)` is called directly by `Level.run()` so keyboard input can be passed in.

## Key Files

- `data/constants.py` — all tunable values: physics (`GRAVITY`, `JUMP_VEL`, `MARIO_SPEED`), display, `TILE_SIZE`, `CAMERA_BORDERS`, and `LEVEL_MAP`
- `communityChest/spriteSheet.py` — `SpriteSheet.extract_image(x, y, w, h)` extracts a region from a surface and scales it by `SIZE_MULTIPLIER` (currently 4×)
- `states/level.py` — `Level` sets up sprite groups and parses `LEVEL_MAP`; `CameraGroup` (bottom of same file) handles the scrolling camera

## Level Map

`LEVEL_MAP` in `data/constants.py` is a list of strings. Each character maps to:
- `X` — `Block` (solid, collidable)
- `P` — Mario spawn point
- `G` — Goomba
- `M` — Mushroom
- ` ` — empty space

Each tile is `TILE_SIZE` (64px) × `TILE_SIZE`.

## Sprite Sheet

All sprites come from `resources/graphics/misc-3.gif` (680×1252px). Sprites are **not** on a regular grid — boundaries must be found by scanning for non-transparent pixels. Confirmed small Mario frame positions (all at y=507, height=16):

| Frame | x   | w  |
|-------|-----|----|
| Stand | 23  | 13 |
| Walk1 | 85  | 12 |
| Walk2 | 100 | 14 |
| Walk3 | 117 | 16 |
| Jump  | 139 | 17 |

Left-facing frames are generated with `pygame.transform.flip(frame, True, False)`. Frames at x=45 (death) and x=67 (skid/left-facing) exist on the same row — avoid using them for walk animation. Frames at x=192+ on y=507 are Luigi sprites.

## Camera

`CameraGroup` (in `states/level.py`) uses a border-box approach: the camera only scrolls when Mario exits the inner rectangle defined by `CAMERA_BORDERS` in `constants.py`. Rendering is done via `custom_draw(player)` instead of the standard pygame `draw()`.

## Collision Pattern

All moving entities (Mario, Goomba, Mushroom) use the same two-axis collision approach:
1. Move on X axis → check `collision_sprites` → resolve
2. Apply gravity on Y axis → check `collision_sprites` → resolve, set `on_floor`

Only `Block` tiles are in `collision_sprites`. Sprite-to-sprite collision (e.g. Mario vs Goomba) is not yet implemented.
