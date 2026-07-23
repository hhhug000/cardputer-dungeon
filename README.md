# Cardputer Dungeon

A small top-down action-adventure built with `pygame`.
Collect gold and weapons, fight enemies, and descend into a dungeon hidden beneath a
bunker in the center of the map.

## Requirements

- Python 3.9+
- pygame

Install dependencies:

```bash
pip install -r requirements.txt
```

## Running the game

```bash
python3 main.py
```

## Controls

| Key                 | Action               |
|---------------------|----------------------|
| Arrow keys / WASD    | Move                 |
| Space                | Attack with current weapon |
| Esc                  | Quit                 |

## Gameplay

- Walk into gold (`$`) to increase your score, and into weapon pickups (`W` sword,
  `G` gun, `P` spear, `M` wand) to equip them. Melee weapons hit adjacent tiles.
  ranged weapons fire a projectile in the direction you're facing.
- Enemies (`E`) chase the player and deal damage on contact; you have 5 hearts.
- Chests (`C`) grant bonus score when opened.
- Numbered tiles along the edge of each map are doors that connect to neighboring
  rooms — walk into them to transition. The overworld's center room contains a
  staircase (`>`) down into the dungeon.

## Level editor

`level_editor.html` is a standalone browser tool (no build step — just open it in a
browser) for authoring the ASCII room layouts used in `MAPS` inside `main.py`.

## Project structure

- `main.py` — game engine, map data (`MAPS`), room connections (`MAP_LINKS`), and
  the main loop.
- `level_editor.html` — visual editor for map layouts.
