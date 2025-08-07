from random import randint

#this dictionary contains player information
player = {
    "playername": "",
    "x": 0,
    "y": 0,
    "pickaxe": 1,
    "pickaxelvl": "copper",
    "load": 0,
    "backpack": 10,
    "GP": 50,
    "steps": 0,
    "day": 1,  
    "silver": 0,
    "gold": 0,
    "copper": 0,
    "turns": 20, 
    "torch": False
}

game_map = []
fog = []

MAP_WIDTH = 0
MAP_HEIGHT = 0

TURNS_PER_DAY = 20
WIN_GP = 500

minerals = ['copper', 'silver', 'gold']
mineral_names = {'C': 'copper', 'S': 'silver', 'G': 'gold'}
pickaxe_price = [50, 150]

prices = {}
prices['copper'] = (1, 3)
prices['silver'] = (5, 8)
prices['gold'] = (10, 18)


#this is used to load the map
def load_map(filename, map_struct):
    try:
        map_file = open(filename, 'r')
        global MAP_WIDTH
        global MAP_HEIGHT
        
        map_struct.clear()
        
        for i in map_file:
            i = i.strip('\n')
            if i:
                map_struct.append(list(i))
        
        if map_struct:
            MAP_WIDTH = len(map_struct[0])
            MAP_HEIGHT = len(map_struct)
        map_file.close()
        return True
    except FileNotFoundError:
        print("Error: Could not find {}".format(filename))
        return False

#this is used to remove the fog by assigning True, False
def clear_fog(fog, player):
    pos_x = player["x"]
    pos_y = player["y"]
    view_size = 2 if player["torch"] else 1
    for i in range(-view_size, view_size + 1):
        for j in range(-view_size, view_size + 1):
            newpos_x = pos_x + j
            newpos_y = pos_y + i
            if newpos_x >= 0 and newpos_x < MAP_WIDTH and newpos_y >= 0 and newpos_y < MAP_HEIGHT:
                fog[newpos_y][newpos_x] = True


#this is to start the game and set the necessay info
def initialize_game(player, fog, game_map):
    #map
    if not load_map("level1.txt", game_map):
        print("Error loading map file. Please ensure level1.txt exists.")
        return False
    #set fog
    fog.clear()  
    for i in game_map:
        row = []
        for j in i:
            row.append(False)
        fog.append(row)   
    
    #input
    while True:
        playername = input("Greetings, miner! What is your name? ").strip()
        if len(playername) > 0 and not playername.isnumeric():
            print("Pleased to meet you, {}. Welcome to Sundrop Town!\n".format(playername))
            player["playername"] = playername
            break
        else:
            print("Invalid name, please enter a valid name (not just numbers).")
    
    #player info
    player['x'] = 0
    player['y'] = 0
    player['copper'] = 0
    player['silver'] = 0
    player['gold'] = 0
    player['GP'] = 50
    player['day'] = 1
    player['steps'] = 0
    player['turns'] = TURNS_PER_DAY
    player['torch'] = False
    player['load'] = 0
    player['backpack'] = 10
    player['pickaxe'] = 1
    player['pickaxelvl'] = "copper"
    
    if 'portal_x' in player:
        del player['portal_x']
    if 'portal_y' in player:
        del player['portal_y']

    clear_fog(fog, player)
    return True

#this is to view the entire map
def draw_map(game_map, fog, player):
    print("+------------------------------+")
    for y in range(MAP_HEIGHT):
        print("|", end="")
        for x in range(MAP_WIDTH):
            if x == player["x"] and y == player["y"]:
                print("M", end="")
            elif "portal_x" in player and "portal_y" in player and x == player["portal_x"] and y == player["portal_y"]:
                print("P", end="")
            elif fog[y][x]==True:
                print(game_map[y][x], end="")
            else:
                print("?", end="")
        print("|")
    print("+------------------------------+")

#this is used to check if we can mine the node
def check_to_mine(position_x, position_y, player):
    if position_x < 0 or position_x >= MAP_WIDTH or position_y < 0 or position_y >= MAP_HEIGHT:
        return False
        
    mineral = game_map[position_y][position_x]  
    
    if mineral in ["C", "S", "G"]:
        can_mine = False
        if mineral == "C": 
            can_mine = True
        elif mineral == "S" and player["pickaxe"] >= 2:
            can_mine = True
        elif mineral == "G" and player["pickaxe"] >= 3:
            can_mine = True
        
        if not can_mine:
            print("You can't mine that with your current pickaxe!")
            return False  
            
        if mineral == "C":
            pieces = randint(1, 5)
            mineral_name = "copper"
        elif mineral == "S":
            pieces = randint(1, 3)
            mineral_name = "silver"
        elif mineral == "G":
            pieces = randint(1, 2)
            mineral_name = "gold"
        
        if pieces + player["load"] <= player["backpack"]:
            player["load"] += pieces
            player[mineral_name] += pieces  
            print("You mined {} piece(s) of {}.".format(pieces, mineral_name))
        else:
            pieces_can_carry = player["backpack"] - player["load"]
            if pieces_can_carry > 0:
                player["load"] += pieces_can_carry
                player[mineral_name] += pieces_can_carry
                print("You mined {} piece(s) of {}.".format(pieces_can_carry, mineral_name))
                print("...but you can only carry {} more piece(s)!".format(pieces_can_carry))
            else:
                print("You can't carry any more, so you can't go that way.")
                return False  
    
    return True  

#this is for the viewport to see 3x3 and 5x5 and the game logic
def draw_view(game_map, fog, player):
    while True:
        view_size = 2 if player["torch"] else 1  
        grid_size = view_size * 2 + 1
        
        print("+" + "-" * grid_size + "+")
        
        for i in range(-view_size, view_size + 1):
            print("|", end="")
            for j in range(-view_size, view_size + 1):
                view_x = player["x"] + j
                view_y = player["y"] + i
                if i == 0 and j == 0:
                    print("M", end="")
                elif view_x < 0 or view_x >= MAP_WIDTH or view_y < 0 or view_y >= MAP_HEIGHT:
                    print("#", end="")
                elif "portal_x" in player and "portal_y" in player and view_x == player["portal_x"] and view_y == player["portal_y"]:
                    print("P", end="")
                else:
                    cell = game_map[view_y][view_x]
                    print(cell, end="")
            print("|")
        
        print("+" + "-" * grid_size + "+")
        
        torch_status = " (Torch equipped)" if player["torch"] else ""
        print("Turns left: {}    Load: {} / {}    Steps: {}{}".format(player['turns'], player['load'], player['backpack'], player['steps'], torch_status))
        print("(WASD) to move")
        print("(M)ap, (I)nformation, (P)ortal, (Q)uit to main menu")
        
        if player["turns"] <= 0:
            print("You are exhausted.")
            print("You place your portal stone here and zap back to town.")
            player["portal_x"] = player["x"]
            player["portal_y"] = player["y"]
            
            player["x"] = 0
            player["y"] = 0
            player["day"] += 1
            player["turns"] = TURNS_PER_DAY
            sell_ore()
            break
        
        #input 
        choice = input("Action? ").lower().strip()
        
        #move up
        if choice == "w":
            new_y = player["y"] - 1
            if new_y >= 0:
                can_move = check_to_mine(player["x"], new_y, player)
                if can_move:
                    player["y"] = new_y
                    player["steps"] += 1
                    clear_fog(fog, player)
                    
                    if player["x"] == 0 and player["y"] == 0:
                        print("You return to town.")
                        player["day"] += 1
                        player["turns"] = TURNS_PER_DAY
                        sell_ore()
                        break
                
                player["turns"] -= 1
            else:
                print("You can't go that way.")
                player["turns"] -= 1

        #movde down
        elif choice == "s":
            new_y = player["y"] + 1
            if new_y < MAP_HEIGHT:
                can_move = check_to_mine(player["x"], new_y, player)
                if can_move:
                    player["y"] = new_y
                    player["steps"] += 1
                    clear_fog(fog, player)
                    
                    if player["x"] == 0 and player["y"] == 0:
                        print("You return to town.")
                        player["day"] += 1
                        player["turns"] = TURNS_PER_DAY
                        sell_ore()
                        break
                
                player["turns"] -= 1
            else:
                print("You can't go that way.")
                player["turns"] -= 1
        
        #move to the left
        elif choice == "a":
            new_x = player["x"] - 1
            if new_x >= 0:
                can_move = check_to_mine(new_x, player["y"], player)
                if can_move:
                    player["x"] = new_x
                    player["steps"] += 1
                    clear_fog(fog, player)
                    
                    if player["x"] == 0 and player["y"] == 0:
                        print("You return to town.")
                        player["day"] += 1
                        player["turns"] = TURNS_PER_DAY
                        sell_ore()
                        break
                
                player["turns"] -= 1
            else:
                print("You can't go that way.")
                player["turns"] -= 1

        #move to the right
        elif choice == "d":
            new_x = player["x"] + 1
            if new_x < MAP_WIDTH:
                can_move = check_to_mine(new_x, player["y"], player)
                if can_move:
                    player["x"] = new_x
                    player["steps"] += 1
                    clear_fog(fog, player)
                    
                    if player["x"] == 0 and player["y"] == 0:
                        print("You return to town.")
                        player["day"] += 1
                        player["turns"] = TURNS_PER_DAY
                        sell_ore()
                        break
                
                player["turns"] -= 1
            else:
                print("You can't go that way.")
                player["turns"] -= 1

        elif choice == "m":
            draw_map(game_map, fog, player)

        elif choice == "i":
            show_information()

        elif choice == "p":
            print("You place your portal stone here and zap back to town.")
            player["portal_x"] = player["x"]
            player["portal_y"] = player["y"]
            
            player["x"] = 0
            player["y"] = 0
            player["day"] += 1
            player["turns"] = TURNS_PER_DAY
            sell_ore()
            break

        elif choice == "q":
            break
        
        else:
            print("Invalid choice. Please try again.")


#this is used to sell the ore and reset the necessary info
def sell_ore():
    total_gp = 0
    sold_any = False

    for ore in ["copper", "silver", "gold"]:
        quantity = player[ore]
        if quantity > 0:
            price_range = prices[ore]
            price = randint(price_range[0], price_range[1])
            gp_earned = price * quantity
            player["GP"] += gp_earned
            total_gp += gp_earned
            print("You sell {} {} ore for {} GP.".format(quantity, ore, gp_earned))
            player[ore] = 0
            sold_any = True
    
    if sold_any==True:
        player["load"] = 0
        print("You now have {} GP!".format(player["GP"]))
        print("All your ore has been sold and you're ready for a new day!")
    else:
        print("You have no ore to sell.")
    
    if player["GP"] >= WIN_GP:
            print("-------------------------------------------------------------")
            print("Woo-hoo! Well done, {}, you have {} GP!".format(player['playername'], player['GP']))
            print("You now have enough to retire and play video games every day.")
            print("And it only took you {} days and {} steps! You win!".format(player['day'], player['steps']))
            print("-------------------------------------------------------------")

            try:
                with open("leaderboard.txt", "a") as f:
                    f.write("{},{},{},{}\n".format(player['playername'], player['day'], player['steps'], player['GP']))
            except Exception as e:
                print("Error writing to leaderboard:", e)
            show_main_menu()


#this is used to show the information when requested
def show_information():
    portal_pos = "Not set"
    if "portal_x" in player and "portal_y" in player:
        portal_pos = "({}, {})".format(player['portal_x'], player['portal_y'])
    
    torch_status = "Yes" if player["torch"] else "No"
    
    pickaxe_desc = "{}".format(player['pickaxe'])
    if player['pickaxe'] == 1:
        pickaxe_desc += " (copper)"
    elif player['pickaxe'] == 2:
        pickaxe_desc += " (silver)"
    elif player['pickaxe'] == 3:
        pickaxe_desc += " (gold)"
    
    print("""----- Player Information -----
Name: {}
Portal position: {}
Pickaxe level: {}
Magic torch: {}
------------------------------
Load: {} / {}
------------------------------
GP: {}
Steps taken: {}
------------------------------""".format(player['playername'], portal_pos, pickaxe_desc, torch_status, player['load'], player['backpack'], player['GP'], player['steps']))

#this is the logic to buy items from the shop
def buy_stuff():
    while True:
        print("----------------------- Shop Menu -------------------------")
        
        if player["pickaxe"] == 1:
            print("(P)ickaxe upgrade to Level 2 to mine silver ore for 50 GP")
        elif player["pickaxe"] == 2:
            print("(P)ickaxe upgrade to Level 3 to mine gold ore for 150 GP")
        
        print("(B)ackpack upgrade to carry {} items for {} GP".format(player['backpack']+2, player['backpack']*2))
        
        if not player["torch"]:
            print("(T)orch - Magic torch for 50 GP (increases view to 5x5)")
        
        print("(L)eave shop")
        print("-----------------------------------------------------------")
        print("GP: {}".format(player['GP']))
        print("-----------------------------------------------------------")
        
        choice = input("Your choice? ").lower().strip()
        
        if choice == "b":
            cost = player["backpack"] * 2
            if player["GP"] >= cost:
                player["GP"] -= cost
                player["backpack"] += 2 
                print("Congratulations! You can now carry {} items!".format(player["backpack"]))
            else:
                print("Insufficient GP!")
        
        elif choice == "p" and player["pickaxe"] != 3:
            if player["pickaxe"] == 1:
                cost = 50
            else:
                cost = 150
                
            if player["GP"] >= cost:
                player["GP"] -= cost
                player["pickaxe"] += 1
                if player["pickaxe"] == 2:
                    player["pickaxelvl"] = "silver"
                    print("Congratulations! You can now mine silver!")
                elif player["pickaxe"] == 3:
                    player["pickaxelvl"] = "gold"
                    print("Congratulations! You can now mine gold!")
            else:
                print("Insufficient GP!")
        
        elif choice == "t" and not player["torch"]:
            if player["GP"] >= 50:
                player["GP"] -= 50
                player["torch"] = True
                print("Congratulations! You now have a magic torch! Your view range has increased to 5x5.")
            else:
                print("Insufficient GP!")

        elif choice == "l":
            break
        
        else:
            print("Invalid choice!")


#this is used to save the game into the respective files
def save_game(game_map, fog, player):
    try:
        with open("level1.txt", "w") as f:
            for row in game_map:
                for cell in row:
                    f.write(cell)
                f.write("\n")
        
        with open("user_info.txt", "w") as t:
            t.write("[FOG]\n")
            for row in fog:
                for cell in row:
                    t.write("1" if cell else "0")
                t.write("\n")

            t.write("[Player]\n")
            for key, value in player.items():
                t.write("{}:{}\n".format(key, value))
        return True
    except Exception as e:
        print("Error saving game: {}".format(e))
        return False

#this is used to load the game from the files
def load_game():
    try:
        try:
            with open("user_info.txt", "r") as f:
                content = f.read().strip()
                if not content:
                    print("Save file is empty. Returning to main menu...")
                    return False
        except FileNotFoundError:
            print("No saved game found. Returning to main menu...")
            return False
        
        with open("user_info.txt", "r") as f:
            lines = f.readlines()
            
        section = None
        fog_data = []
        
        for line in lines:
            line = line.strip()
            
            if line == "[FOG]":
                section = "fog"
                continue
            elif line == "[Player]":
                section = "player"
                continue
            
            if section == "fog" and line:
                fog_row = []
                for char in line:
                    if char == "1":
                        fog_row.append(True)
                    elif char == "0":
                        fog_row.append(False)
                fog_data.append(fog_row)
            elif section == "player" and ":" in line:
                key, value = line.split(":", 1)
                if key in ["x", "y", "pickaxe", "load", "backpack", "GP", "steps", "day", "silver", "gold", "copper", "turns", "portal_x", "portal_y"]:
                    player[key] = int(value)
                elif key == "torch":
                    player[key] = value.lower() == "true"
                else:
                    player[key] = value
        
        if not load_map("level1.txt", game_map):
            print("Error loading map file. Returning to main menu...")
            return False
        
        fog.clear()
        if fog_data:
            fog.extend(fog_data)
        else:
            for i in game_map:
                row = []
                for j in i:
                    row.append(False)
                fog.append(row)
        
        
        print("Game loaded successfully!")
        return True
        
    except Exception as e:
        print("Error loading saved game: {}".format(e))
        print("Returning to main menu...")
        return False

#this does the printing of the menu and taking input and directing them to the udfs
def show_main_menu():
    while True:
        print()
        print("--- Main Menu ----")
        print("(N)ew game")
        print("(L)oad saved game")
        print("(H)igh scores")
        print("(Q)uit")
        print("------------------")
        choice = input("Your choice? ").lower().strip()
        
        if choice == "n":
            if initialize_game(player, fog, game_map):
                show_town_menu()
            break
        elif choice == "l":
            if load_game():
                show_town_menu()
                break
        elif choice == "h":
            try:
                with open("leaderboard.txt", "r") as f:
                    scores = []
                    for line in f:
                        name, days, steps, gp = line.strip().split(",")
                        scores.append({
                            "name": name,
                            "days": int(days),
                            "steps": int(steps),
                            "gp": int(gp)
                        })

                    def sort_score(entry):
                        return (entry["days"], entry["steps"], -entry["gp"])

                    scores.sort(key=sort_score)

                    print("\n===== TOP 5 HIGH SCORES =====")
                    for i in range(min(5, len(scores))):
                        entry = scores[i]
                        print("{}. {} - Days: {}, Steps: {}, GP: {}".format(i+1, entry['name'], entry['days'], entry['steps'], entry['gp']))
                    print("=============================\n")

            except FileNotFoundError:
                print("No leaderboard data found yet.")

        elif choice == "q":
            print("Thanks for playing Sundrop Caves!")
            break
        else:
            print("Invalid input. Please try again.")

#this is for the town menu
def show_town_menu():
    while True:
        print()
        print("Day {}".format(player["day"]))
        print("----- Sundrop Town -----")
        print("(B)uy stuff")
        print("See Player (I)nformation")
        print("See Mine (M)ap")
        print("(E)nter mine")
        print("Sa(V)e game")
        print("(Q)uit to main menu")
        print("------------------------")
        choice = input("Your choice? ").lower().strip()
        
        if choice == "b":
            buy_stuff()
        elif choice == "i":
            show_information()
        elif choice == "m":
            draw_map(game_map, fog, player)
        elif choice == "e":
            if "portal_x" in player and "portal_y" in player:
                player["x"] = player["portal_x"]
                player["y"] = player["portal_y"]
                print("---------------------------------------------------")
                print("{:^51}".format("DAY {}".format(player['day'])))
                print("---------------------------------------------------")
            else:
                player["x"] = 0
                player["y"] = 0
                print("---------------------------------------------------")
                print("{:^51}".format("DAY {}".format(player['day'])))
                print("---------------------------------------------------")
            
            draw_view(game_map, fog, player)
        elif choice == "v":
            if save_game(game_map, fog, player):
                print("Game saved.")
            else:
                print("Error saving game.")
        elif choice == "q":
            show_main_menu()
            break
        else:
            print("Invalid input, please try again.")


#main game
game_state = "main"
print("---------------- Welcome to Sundrop Caves! ----------------")
print("You spent all your money to get the deed to a mine, a small")
print("backpack, a simple pickaxe and a magical portal stone.")
print()
print("How quickly can you get the 500 GP you need to retire")
print("and live happily ever after?")
print("-----------------------------------------------------------")

show_main_menu()
