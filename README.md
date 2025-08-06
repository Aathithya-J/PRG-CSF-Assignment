# Sundrop Caves

**PRG1 Assignment (Apr 2025)**  
**Student Name:** Aathithya Jegatheesan  
**Student ID:** S10271062H  
**Class:** CSF01  

---

## 1. Overview

This program is a text-based adventure game titled **Sundrop Caves**, developed for the PRG1 Assignment (Semester 1, AY2025/26). It is written in Python and implements both the **Basic** and **Advanced Requirements** outlined in the official assignment. The player explores a mine, collects ores, sells them, and upgrades tools to reach 500 GP and retire.

---

## 2. Features Implemented

### Basic Requirements ✅
- Main menu: New Game, Load Game, Quit  
- Town menu: Buy items, View Player Info, View Map, Save Game, Enter Mine  
- Mining system with randomized ore yields  
- Fog-of-war view system  
- Saving and loading game data  
- Automatic ore selling upon returning to town  
- Backpack upgrade system  
- Turn-based (20 moves/day) system  

### Advanced Requirements ✅
- Pickaxe upgrades (Copper → Silver → Gold)  
- Portal system to return to town  
- Input validation for name and shop purchases  
- Leaderboard tracking top 5 players (by days, steps, GP)  

### Additional Features ✅
- Magic torch (increased vision)  
- GitHub: Committed via one-shot (developed in 1 sitting)  
  [GitHub Repo](https://github.com/Aathithya-J/PRG-CSF-Assignment)  
  > If inaccessible, please inform me.

---

## 3. Game Constants & Data Structures

| Name            | Description                              |
|-----------------|------------------------------------------|
| `MAP_WIDTH` / `MAP_HEIGHT` | Set dynamically from `level1.txt` |
| `TURNS_PER_DAY` | 20 moves allowed per day                 |
| `WIN_GP`        | 500 GP to win the game                   |
| `player`        | Dictionary containing player stats       |
| `game_map`      | 2D list holding the mine layout          |
| `fog`           | 2D list for fog-of-war status            |
| `prices`        | Ore sale price ranges                    |
| `mineral_names` | Symbol-to-mineral type mapping           |

---

## 4. User-Defined Function (UDF) Descriptions

### `load_map(filename, map_struct)`
Loads mine layout from file and updates the game map.  
**Used in:** `initialize_game`, `load_game`  
**Assignment Ref:** Section 3 – Mine Map  

### `clear_fog(fog, player)`
Clears fog-of-war based on player position and vision range.  
**Used in:** `initialize_game`, movement  
**Assignment Ref:** Section 3.2 – Fog of War  

### `initialize_game(player, fog, game_map)`
Initializes all game data, player stats, and map for a new game.  
**Used in:** `show_main_menu()`  
**Assignment Ref:** Section 4 – New Game Flow  

### `draw_map(game_map, fog, player)`
Displays the full revealed map including player and portal.  
**Used in:** `show_town_menu`, `draw_view()`  
**Assignment Ref:** Section 2.3 – See Mine Map  

### `check_to_mine(position_x, position_y, player)`
Checks if player can step on tile; mines ore if valid.  
**Used in:** Movement in `draw_view()`  
**Assignment Ref:** Section 3.1 – Mining Logic, Section 5 – Pickaxe Levels  

### `draw_view(game_map, fog, player)`
Main mining screen. Handles player movement, mining, and ending the day.  
**Used in:** `show_town_menu()`  
**Assignment Ref:** Section 3 – Enter Mine  

### `sell_ore()`
Sells collected ores, adds GP, checks win condition, and logs leaderboard.  
**Used in:** `draw_view()`, auto-triggered when returning to town  
**Assignment Ref:** Table 2 – Mineral Prices, Section 4 – Winning the Game  

### `show_information()`
Displays player stats: position, ore, load, GP, steps, and upgrades.  
**Used in:** Mine and town menus  
**Assignment Ref:** Section 2.2 – Player Information  

### `buy_stuff()`
Lets player upgrade backpack, pickaxe, or buy torch. Validates GP.  
**Used in:** `show_town_menu()`  
**Assignment Ref:** Section 2.1 and Section 5 – Upgrades  

### `save_game(game_map, fog, player)`
Saves game state into `level1.txt` and `user_info.txt`.  
**Used in:** `show_town_menu()`  
**Assignment Ref:** Section 2.5 – Save Game  

### `load_game()`
Loads data from saved files. Restores fog, map, and player info.  
**Used in:** `show_main_menu()`  
**Assignment Ref:** Section 1.2 – Load Game  

### `show_main_menu()`
Initial menu with options to start a new game, load game, or quit.  
**Used in:** Game start, returning from town  
**Assignment Ref:** Section 1 – Main Menu  

### `show_town_menu()`
Menu hub for all town actions like shopping, saving, entering mine, etc.  
**Used in:** After game starts or loads  
**Assignment Ref:** Section 2 – Town Menu  

---

## 5. Leaderboard Functionality

- Stored in `leaderboard.txt`  
- Tracks: player name, number of days, steps, and GP  
- Sorted by:
  1. Fewest days
  2. Fewest steps
  3. Highest GP  

**Referenced in:** `sell_ore()`, `show_main_menu()`  
**Assignment Ref:** Section 5 – View Top Scores

---

## 6. Saving & Loading Format

### Files
- `level1.txt`: Map layout  
- `user_info.txt`:  
  - `[FOG]`: Each tile stored as `1` (seen) or `0` (hidden)  
  - `[Player]`: Key-value pairs of player attributes  

---

## 7. Additional Notes

- Inputs are validated (e.g., player name must be non-numeric).  
- The portal system returns player to town and saves position.  
- Mined nodes do not disappear; they remain visible.  
- Players are **not allowed** to load previously won games to replay.  
- Deleting system files like `level1.txt` or `user_info.txt` will break functionality.

---

## 8. Conclusion

This game fully satisfies the PRG1 assignment specifications. All required features are implemented, including validation and leaderboard tracking. The code is modular and organized with clear user-defined functions to support maintainability and future enhancements.
