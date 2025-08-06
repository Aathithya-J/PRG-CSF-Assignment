Documentation for Sundrop Caves


PRG1 Assignment (Apr 2025)
Student Name: Aathithya Jegatheesan
Student ID: S10271062H
Class: CSF01

1. Overview
This program is a text-based adventure game titled Sundrop Caves, developed as part of the PRG1 Assignment for Semester 1, AY2025/26. It is written in Python and meets both the Basic and Advanced Requirements outlined in the assignment handout. The player assumes the role of a miner who explores a mine, collects valuable ores, sells them, and upgrades tools with the ultimate goal of earning 500 GP to retire.

2. Features Implemented
Basic Requirements ✔
Main menu with options to start a new game, load game, and quit


Town menu for buying items, viewing player information, map, saving, entering mine


Mining system with randomised ore yields


Fog-of-war implementation


Saving and loading game data


Automatic ore selling when returning to town


Backpack upgrade system


Turn-based day system


Advanced Requirements ✔
Pickaxe upgrade system (copper → silver → gold)


Portal system to return to town


Validation for player name and shop purchases


Leaderboard (top 5) tracking players based on days, steps, and GP
Additional Features ✔
Magic torch
Github (Committed one-shot as I did it in 1 sitting)
https://github.com/Aathithya-J/PRG-CSF-Assignment
If not accessible, please inform me



3. Game Constants & Data Structures
MAP_WIDTH / MAP_HEIGHT: dynamically set from level1.txt


TURNS_PER_DAY: max number of steps (20) per day


WIN_GP: amount of GP required to win (500)


player: dictionary storing player attributes


game_map: 2D list holding the mine map


fog: 2D boolean list used for fog-of-war


prices: dictionary containing ore sale price ranges


mineral_names: maps symbol letters to mineral types



4. User-Defined Function (UDF) Descriptions
load_map(filename, map_struct)
Purpose: Loads the mine layout from a .txt file and updates the map structure.
Used in: initialize_game, load_game
References: PRG1 Assignment, Section 3 – Mine Map

clear_fog(fog, player)
Purpose: Clears the fog-of-war around the player's position (3x3 or 5x5 if torch is equipped).
Used in: initialize_game, movement in draw_view
References: PRG1 Assignment, Section 3.2 – Fog of War

initialize_game(player, fog, game_map)
Purpose: Sets up a new game by resetting all player stats, clearing the fog, and loading the map.
Used in: show_main_menu()
References: PRG1 Assignment, Section 4 – New Game Flow

draw_map(game_map, fog, player)
Purpose: Displays the full mine map with discovered areas, player location, and portal.
Used in: show_town_menu, draw_view
References: PRG1 Assignment, Section 2.3 – See Mine Map

check_to_mine(position_x, position_y, player)
Purpose: Checks if the player can move onto a tile and mines the ore if conditions are met. Validates pickaxe level and backpack capacity.
Used in: Movement logic in draw_view()
References: PRG1 Assignment, Section 3.1 – Mining Logic, Section 5 – Pickaxe Levels

draw_view(game_map, fog, player)
Purpose: Displays the current viewport around the player (3x3 or 5x5 with torch). Handles movement (WASD), turns, mining, portal usage, and return to town.
Used in: show_town_menu()
References: PRG1 Assignment, Section 3 – Enter Mine

sell_ore()
Purpose: Sells all the ores in the backpack upon returning to town. Calculates GP based on randomised prices. Checks win condition and updates leaderboard.
Used in: draw_view, use_portal, automatic on town return
References: PRG1 Assignment, Table 2 – Mineral Prices, Section 4 – Winning the Game

show_information()
Purpose: Displays current player status, including ore quantities, GP, steps, portal position, pickaxe, and backpack stats.
Used in: Town and mine menus
References: PRG1 Assignment, Section 2.2 – Player Information

buy_stuff()
Purpose: Allows player to upgrade backpack, pickaxe, or buy a torch if conditions are met. Validates GP before purchase.
Used in: show_town_menu()
References: PRG1 Assignment, Section 2.1 and Section 5 – Upgrades

save_game(game_map, fog, player)
Purpose: Saves the current map, fog visibility, and player stats into two files (level1.txt, user_info.txt).
Used in: show_town_menu()
References: PRG1 Assignment, Section 2.5 – Save Game

load_game()
Purpose: Loads saved data from user_info.txt and level1.txt to resume previous progress. Handles file errors and returns to main menu if missing.
Used in: show_main_menu()
References: PRG1 Assignment, Section 1.2 – Load Game

show_main_menu()
Purpose: Displays the main game menu with options for New Game, Load Game, View High Scores, and Quit.
Used in: Program start, Quit from town
References: PRG1 Assignment, Section 1 – Main Menu

show_town_menu()
Purpose: Displays town interaction options and directs to corresponding functions: buying, viewing info, entering mine, saving, and quitting.
Used in: New game, loaded game
References: PRG1 Assignment, Section 2 – Town Menu

5. Leaderboard Functionality
High scores stored in leaderboard.txt
Tracked by: player name, days taken, steps taken, and total GP
Sorted by:
Fewest days
Fewest steps
Most GP


Referenced in: sell_ore(), show_main_menu()
PRG1 Reference: Section 5 – View Top Scores (Advanced Requirement)

6. Saving & Loading Format
Files:
level1.txt: Map data (layout of mine)
User_info.txt:
[FOG]: Each tile as 1 (visible) or 0 (hidden)
[Player]: Key-value data of all player attributes



7. Additional Notes
All inputs are validated (Eg: shop items require enough GP).
The game resets properly upon winning.
The portal system is correctly implemented to return to last mine location.
Mined nodes will not be removed and will remain at it’s original position
Players are not to load winning player information and are to start a new game
Players are not to remove any of the files which will not allow them to experience in full

8. Conclusion
This game meets and exceeds the PRG1 assignment expectations, implementing all required basic and advanced features with additional features. All user-defined functions are written in modular, reusable form, following programming best practices.

