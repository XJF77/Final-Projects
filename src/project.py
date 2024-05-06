import random
import time

class CharacterClass:
    def __init__(self, hp, damage, defense, agility, accuracy):
        self.hp = hp
        self.damage = damage
        self.defense = defense
        self.agility = agility
        self.accuracy = accuracy


class Mage(CharacterClass):
    def __init__(self):
        super().__init__(hp=80, damage=15, defense=0.1, agility=10, accuracy=80)

class Fighter(CharacterClass):
    def __init__(self):
        super().__init__(hp=120, damage=22, defense=0.2, agility=5, accuracy=70)


class Rogue(CharacterClass):
    def __init__(self):
        super().__init__(hp=100, damage=18, defense=0.15, agility=15, accuracy=90)

class Player:
    def __init__(self, name, player_class):
        self.name = name
        self.player_class = player_class
        self.hp = player_class.hp
        self.weapon, self.weapon_damage = self.get_starter_weapon(player_class)
        self.potions = 0
        self.exp = 0  # Starting experience points
        self.level = 1  # Starting level
        self.base_attack = player_class.damage  # Base attack stat
        self.exp_to_level_up = 20  # Experience points required to level up
        self.exp_bar = 0  # Experience points progress bar
        self.gold = 1000  # Starting gold
        self.agility = player_class.agility
        self.defense = player_class.defense
        self.accuracy = player_class.accuracy 
        self.current_title = self.get_title()


    def __str__(self):
        return f"[{self.current_title}] {self.name} ({self.player_class.__class__.__name__})"

    def level_up(self):
        self.level += 1
        self.hp += 10  # Increase overall HP by 10 points upon leveling up
        self.player_class.hp += 10  # Increase max HP by 10 points upon leveling up
        self.base_attack += 5  # Increase attack by 5 points upon leveling up
        self.exp_bar = 0  # Reset exp bar
        self.exp_to_level_up *= 2  # Double the exp required for next level
        print(f"\nLEVEL UP! You've reached {self.get_title()} as a {self.player_class.__class__.__name__}!")
        print(f"\nYour max HP is now {self.player_class.hp} and your attack is {self.base_attack}.")


    def get_title(self):
        # Define titles based on class and level
        if self.player_class.__class__.__name__ == "Mage":
            titles = ["Novice", "Apprentice", "Sorcerer", "Archmage", "Ether Magisters", "Supreme Archon", "Eternal Sage"]
        elif self.player_class.__class__.__name__ == "Fighter":
            titles = ["Recruit", "Warrior", "Knight", "Champion", "Brutal Warlord", "Imperial Overlord", "Divine Conqueror"]
        elif self.player_class.__class__.__name__ == "Rogue":
            titles = ["Thief", "Bandit", "Assassin", "Ninja", "Phantom Thief", "Shadow Master", "Silent Executioner"]
        return titles[min(self.level - 1, len(titles) - 1)]

    def get_starter_weapon(self, player_class):
        # Define starter weapons based on class
        if player_class.__class__.__name__ == "Mage":
            return "Birch Stick", 5
        elif player_class.__class__.__name__ == "Fighter":
            return "Rusted Greatsword", 8
        elif player_class.__class__.__name__ == "Rogue":
            return "Kitchen Knives", 6

class Enemy:
    def __init__(self, name, hp, damage, exp, defense, agility, accuracy):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.exp = exp
        self.defense = defense
        self.agility = agility
        self.accuracy = accuracy  # Add accuracy attribute

class Boss(Enemy):
    def __init__(self, name, hp, damage, exp, defense, agility, accuracy):
        super().__init__(name, hp, damage, exp, defense, agility, accuracy)

class Location:
    def __init__(self, name, description, enemies, boss=None, shop_name=None, weapon_titles=None, armor_titles=None, armor_stats_range=None):
        self.name = name
        self.description = description
        self.enemies = enemies
        self.boss = boss
        self.shop_name = shop_name
        self.weapon_titles = weapon_titles
        self.armor_titles = armor_titles
        self.armor_stats_range = armor_stats_range


def create_locations():
    locations = [
        Location("Dark Forest", "You venture into the Dark Forest...", 
                 [Enemy("Goblin", 30, 10, 5, 0.1, 15, 80),  
                  Enemy("Wolf", 25, 15, 7, 0.2, 20, 85),
                  Enemy("Spider", 35, 12, 6, 0.15, 18, 75)], 
                 Boss("Elder Treant", 100, 25, 50, 0.3, 25, 90),  
                 shop_name="Shadow Trader's Emporium",
                 weapon_titles=["Rusted", "Old", "Tattered", "Weathered"],
                 armor_titles=["Rugged", "Sturdy", "Reinforced", "Fortified"],
                 armor_stats_range=[(-2, 4), (3, 5), (4, 6), (5, 7)]),
        Location("Mystic Cavern", "You enter the Mystic Cavern...", 
                 [Enemy("Skeleton", 40, 8, 4, 0.1, 12, 70),
                  Enemy("Mimic", 60, 18, 10, 0.2, 22, 85),
                  Enemy("Giant Bat", 45, 10, 5, 0.15, 17, 75),
                  Enemy("Stone Guardian", 80, 22, 12, 0.25, 23, 80)], 
                 Boss("Arcane Golem", 150, 30, 60, 0.35, 28, 90),
                 shop_name="Arcane Relics Emporium",
                 weapon_titles=["Ancient", "Mystic", "Ethereal", "Enchanted"],
                 armor_titles=["Mystical", "Arcane", "Ethereal", "Enchanted"],
                 armor_stats_range=[(4, -6), (-5, 7), (6, -8), (-7, -9)]),
        Location("Abandoned Ruins", "You explore the Abandoned Ruins...", 
                 [Enemy("Zombie", 45, 10, 6, 0.1, 14, 70),
                  Enemy("Ghost", 30, 12, 8, 0.2, 19, 85),
                  Enemy("Wraith", 60, 14, 9, 0.15, 21, 75),
                  Enemy("Specter", 65, 16, 10, 0.25, 24, 80)], 
                 Boss("Lich King Mal'Gorath", 200, 35, 70, 0.4, 30, 95),
                 shop_name="Ghostly Wares Market",
                 weapon_titles=["Forgotten", "Haunted", "Cursed", "Shadow"],
                 armor_titles=["Tattered", "Decayed", "Corroded", "Cursed"],
                 armor_stats_range=[(2, -4), (-3, 5), (4, -6), (-5, -7)]),
        Location("Dragon's Lair", "You approach the Dragon's Lair...", 
                 [Enemy("Dragonling", 80, 20, 15, 0.2, 30, 85),
                  Enemy("Wyvern", 120, 30, 20, 0.25, 35, 90),
                  Enemy("Basilisk", 150, 35, 25, 0.3, 40, 90)],  
                 Boss("Pyrothor, the Flame Tyrant", 500, 50, 100, 0.5, 35, 99),
                 shop_name="Dragon's Treasure Trove",
                 weapon_titles=["Basilik Bone", "Draconic", "Ignis", "Sarlet"],
                 armor_titles=["Scorched", "Dragonhide", "Flameforged", "Infernal"],
                 armor_stats_range=[(8, -10), (-9, 12), (10, -14), (-11, -15)])
    ]
    return locations


def intro():
    print("Welcome to ...")
    print("""
/* 888      8888888888 .d8888b.  8888888888 888b    888 8888888b.   .d8888b.       .d88888b.  8888888888 */
/* 888      888       d88P  Y88b 888        8888b   888 888  "Y88b d88P  Y88b     d88P" "Y88b 888        */
/* 888      888       888    888 888        88888b  888 888    888 Y88b.          888     888 888        */
/* 888      8888888   888        8888888    888Y88b 888 888    888  "Y888b.       888     888 8888888    */
/* 888      888       888  88888 888        888 Y88b888 888    888     "Y88b.     888     888 888        */
/* 888      888       888    888 888        888  Y88888 888    888       "888     888     888 888        */
/* 888      888       Y88b  d88P 888        888   Y8888 888  .d88P Y88b  d88P     Y88b. .d88P 888        */
/* 88888888 8888888888 "Y8888P88 8888888888 888    Y888 8888888P"   "Y8888P"       "Y88888P"  888        */
/*                                                                                                       */
/*                                                                                                       */
 time.sleep(1)
 
/*                                                                                                       */
/*        d8888 8888888888P 8888888888 8888888b.   .d88888b. 88888888888 888    888                      */
/*       d88888       d88P  888        888   Y88b d88P" "Y88b    888     888    888                      */
/*      d88P888      d88P   888        888    888 888     888    888     888    888                      */
/*     d88P 888     d88P    8888888    888   d88P 888     888    888     8888888888                      */
/*    d88P  888    d88P     888        8888888P"  888     888    888     888    888                      */
/*   d88P   888   d88P      888        888 T88b   888     888    888     888    888                      */
/*  d8888888888  d88P       888        888  T88b  Y88b. .d88P    888     888    888                      */
/* d88P     888 d8888888888 8888888888 888   T88b  "Y88888P"     888     888    888                      */
/*                                                                                                       */
 time.sleep(1)
 
/*                                                                                                       */
/*                                                                                                       */
/* 8888888b.        d8888 888       888 888b    888      .d88888b.  8888888888                           */
/* 888  "Y88b      d88888 888   o   888 8888b   888     d88P" "Y88b 888                                  */
/* 888    888     d88P888 888  d8b  888 88888b  888     888     888 888                                  */
/* 888    888    d88P 888 888 d888b 888 888Y88b 888     888     888 8888888                              */
/* 888    888   d88P  888 888d88888b888 888 Y88b888     888     888 888                                  */
/* 888    888  d88P   888 88888P Y88888 888  Y88888     888     888 888                                  */
/* 888  .d88P d8888888888 8888P   Y8888 888   Y8888     Y88b. .d88P 888                                  */
/* 8888888P" d88P     888 888P     Y888 888    Y888      "Y88888P"  888                                  */
/*                                                                                                       */
/*                                                                                                       */
/*                                                                                                       */
/* 8888888b.        d8888 8888888b.  888    d8P  888b    888 8888888888 .d8888b.   .d8888b.              */
/* 888  "Y88b      d88888 888   Y88b 888   d8P   8888b   888 888       d88P  Y88b d88P  Y88b             */
/* 888    888     d88P888 888    888 888  d8P    88888b  888 888       Y88b.      Y88b.                  */
/* 888    888    d88P 888 888   d88P 888d88K     888Y88b 888 8888888    "Y888b.    "Y888b.               */
/* 888    888   d88P  888 8888888P"  8888888b    888 Y88b888 888           "Y88b.     "Y88b.             */
/* 888    888  d88P   888 888 T88b   888  Y88b   888  Y88888 888             "888       "888             */
/* 888  .d88P d8888888888 888  T88b  888   Y88b  888   Y8888 888       Y88b  d88P Y88b  d88P             */
/* 8888888P" d88P     888 888   T88b 888    Y88b 888    Y888 8888888888 "Y8888P"   "Y8888P"              */



    """)

    time.sleep(2)  # Delay for 3 seconds

    print("You find yourself in the land of Azeroth, a world plagued by monsters and darkness.")
    print("Legends speak of a time when this land was bathed in light and prosperity, but those days are long gone.")
    print("A great dragon, known as Pyrothor, has brought about an apocalypse, unleashing hordes of monsters upon the land.")
    print("Entire cities lie in ruins, and the once-verdant forests now burn with an unholy fire.")
    print("It's up to you, a brave hero, to venture forth, confront the minions of Pyrothor, and save the kingdom from eternal darkness.")
    print("The fate of Azeroth rests in your hands. Let us embark on this perilous journey...\n")

    time.sleep(2)

def create_player():
    print("Choose your class:")
    print("1. Mage")
    print("2. Fighter")
    print("3. Rogue")

    while True:
        class_choice = input("Enter the number of your chosen class: ")

        if class_choice == "1":
            player_class = Mage()
            break
        elif class_choice == "2":
            player_class = Fighter()
            break
        elif class_choice == "3":
            player_class = Rogue()
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 3.")

    time.sleep(2)  # Delay for 2 seconds before showing class description

    if class_choice == "1":
        print("\nYou have chosen to become a Mage.")
        print("Mages in the land of Azeroth are revered for their mastery over arcane energies.")
        print("They are the keepers of ancient knowledge, wielding spells that can shape reality itself.")
        print("Your personal quest is to unlock the secrets of the arcane, keeping the realms safe.")
    elif class_choice == "2":
        print("\nYou have chosen to become a Fighter.")
        print("Fighters are the stalwart defenders of the realm, renowned for their martial prowess.")
        print("They stand as guardians against the encroaching darkness, facing every challenge with unwavering courage.")
        print("Your personal quest is to prove yourself in the crucible of battle, seeking out legendary foes to test your mettle.")
    elif class_choice == "3":
        print("\nYou have chosen to become a Rogue.")
        print("Rogues are the shadows that move unseen, masters of stealth and subterfuge.")
        print("They thrive in the underworld, navigating the treacherous paths of intrigue and deception.")
        print("Your personal quest is to amass wealth and power through cunning schemes and daring heists, infiltrating the highest echelons of society to uncover hidden treasures and secrets.")

    name = input("\nEnter your character's name: ")
    player = Player(name, player_class)
    print(f"Welcome, {player}! Your journey begins now as a {player.player_class.__class__.__name__}.")
    return player

def shop(player, location, location_index):
    print(f"\nWelcome to the {location.shop_name}!")
    print("What would you like to buy?")
    print("1. Health Potion (20 gold)")

    # Determine weapon options based on player class
    if player.player_class.__class__.__name__ == "Mage":
        class_weapons = ["Staff", "Wand", "Orb", "Grimoire"]
    elif player.player_class.__class__.__name__ == "Fighter":
        class_weapons = ["Sword", "Axe", "Mace", "Spear"]
    elif player.player_class.__class__.__name__ == "Rogue":
        class_weapons = ["Dagger", "Shortbow", "Crossbow", "Throwing knives"]

    # Rotate through the weapon options based on location index
    weapon_index_1 = location_index % len(class_weapons)
    weapon_index_2 = (location_index + 1) % len(class_weapons)

    weapon_name_1 = class_weapons[weapon_index_1]
    weapon_name_2 = class_weapons[weapon_index_2]

    weapon_title_1 = location.weapon_titles[location_index]
    weapon_title_2 = location.weapon_titles[(location_index + 1) % len(location.weapon_titles)]

    # Calculate cost and damage based on location index
    base_cost = 100 + (30 * location_index)  # Base cost increases by 30 gold per location
    base_damage = 5 + (5 * location_index)  # Base damage increases by 5 per location

    print(f"2. {weapon_title_1} {weapon_name_1} ({base_cost} gold) - Damage: {base_damage}")
    print(f"3. {weapon_title_2} {weapon_name_2} ({base_cost + 5} gold) - Damage: {base_damage + 5}")
    
    # Determine armor options based on player class
    if player.player_class.__class__.__name__ == "Mage":
        class_armor = ["Robe", "Bracers", "Rings", "Tunic"]
    elif player.player_class.__class__.__name__ == "Fighter":
        class_armor = ["Breast Plate", "Pauldrons", "Helm", "Plate"]
    elif player.player_class.__class__.__name__ == "Rogue":
        class_armor = ["Shroud", "Boots", "Cape", "Hood"]

    armor_index_1 = location_index % len(class_armor)
    armor_index_2 = (location_index + 1) % len(class_armor)

    armor_name_1 = class_armor[armor_index_1]
    armor_name_2 = class_armor[armor_index_2]

    armor_title_1 = location.weapon_titles[location_index]
    armor_title_2 = location.weapon_titles[(location_index + 1) % len(location.weapon_titles)]

    base_cost_armor = 150 + (40 * location_index)  # Base cost increases by 40 gold per location
    base_defense = 3 + (3 * location_index)  # Base defense increases by 3 per location
    base_agility = 1 + (1 * location_index)  # Base agility increases by 1 per location

    print(f"4. {armor_title_1} {armor_name_1} ({base_cost_armor} gold) - Defense: {base_defense}, Agility: {base_agility}")
    print(f"5. {armor_title_2} {armor_name_2} ({base_cost_armor + 5} gold) - Defense: {base_defense + 3}, Agility: {base_agility + 3}")
    
    print(f"Gold: {player.gold}")  # Display player's current gold

    while True:
        choice = input("Enter your choice (or 'exit' to leave the shop): ")

        if choice == "1":
            if player.gold >= 20:
                player.potions += 1
                player.gold -= 20
                print("You bought a health potion!")
                print(f"Gold: {player.gold}")
            else:
                print("You don't have enough gold!")
        elif choice == "2":
            if player.gold >= base_cost:
                player.weapon = f"{weapon_title_1} {weapon_name_1}"
                player.weapon_damage += base_damage
                player.gold -= base_cost
                print(f"You bought a {weapon_title_1} {weapon_name_1}! Damage increased by {base_damage}.")
                print(f"Your total damage is now: {player.base_attack + player.weapon_damage}")
                print(f"Gold: {player.gold}")
            else:
                print("You don't have enough gold!")
        elif choice == "3":
            if player.gold >= base_cost + 5:
                player.weapon = f"{weapon_title_2} {weapon_name_2}"
                player.weapon_damage += base_damage + 5
                player.gold -= base_cost + 5
                print(f"You bought a {weapon_title_2} {weapon_name_2}! Damage increased by {base_damage + 5}.")
                print(f"Your total damage is now: {player.base_attack + player.weapon_damage}")
                print(f"Gold: {player.gold}")
            else:
                print("You don't have enough gold!")
        elif choice == "4":
            if player.gold >= base_cost_armor:
                player.armor = f"{armor_title_1} {armor_name_1}"
                player.defense += base_defense
                player.agility += base_agility
                player.gold -= base_cost_armor
                print(f"You bought a {armor_title_1} {armor_name_1}! Defense increased by {base_defense}, Agility increased by {base_agility}.")
                print(f"Your total defense is now: {player.defense}, Your total agility is now: {player.agility}")
                print(f"Gold: {player.gold}")
            else:
                print("You don't have enough gold!")
        elif choice == "5":
            if player.gold >= base_cost_armor + 5:
                player.armor = f"{armor_title_2} {armor_name_2}"
                player.defense += base_defense + 3
                player.agility += base_agility + 3
                player.gold -= base_cost_armor + 5
                print(f"You bought a {armor_title_2} {armor_name_2}! Defense increased by {base_defense + 3}, Agility increased by {base_agility + 3}.")
                print(f"Your total defense is now: {player.defense}, Your total agility is now: {player.agility}")
                print(f"Gold: {player.gold}")
            else:
                print("You don't have enough gold!")
        elif choice.lower() == "exit":
            print("Thank you for visiting the shop!")
            break
        else:
            print("Invalid choice!")

def display_health_bar(current, max_hp):
    bar_length = 10
    filled_length = int(bar_length * current / max_hp)
    health_bar = "|" + "#" * filled_length + "-" * (bar_length - filled_length) + "|"
    return health_bar

def combat(player, location, stage):
    if isinstance(location, Boss):  # Check if the current location contains a boss
        enemy = location
        initial_enemy_hp = enemy.hp
        print(f"You encounter the {enemy.name}!")
    else:
        enemy = random.choice(location.enemies)
        initial_enemy_hp = enemy.hp
    
    while player.hp > 0 and enemy.hp > 0:
        exp_percentage = (player.exp / player.exp_to_level_up) * 100
        exp_bar_length = int(exp_percentage / 10)
        exp_bar = "|" + "#" * exp_bar_length + "-" * (10 - exp_bar_length) + "|"
        
        print("---------------------------------------")
        print(f"{enemy.name}\nHP: {display_health_bar(enemy.hp, initial_enemy_hp)} ({int((enemy.hp / initial_enemy_hp) * 100)}%)")
        print("\n\n")  # Two lines of space between enemy and player display
        print(f"[{player.get_title()}] ({player.player_class.__class__.__name__}) {player.name}:\nHP: {display_health_bar(player.hp, player.player_class.hp)} ({int((player.hp / player.player_class.hp) * 100)}%)")
        print("1. Attack | 2. Item")
        print("---------------------------------------")
        print(f"Exp: {exp_bar} ({int(exp_percentage)}%)")
        
        choice = input("Enter your choice (1-2): ")

        if choice == "1":
            # Calculate hit chance based on player's accuracy and enemy's agility
            hit_chance = player.accuracy - enemy.agility
            if random.randint(0, 99) < hit_chance:
                total_attack = player.base_attack + player.weapon_damage + random.randint(-2, 2)
                enemy.hp -= total_attack
                print(f"\nYou attack the {enemy.name} for {total_attack} damage!")
            else:
                print(f"\nYour attack missed!")
            time.sleep(1)
            
            # Enemy's turn
            if enemy.hp > 0:  # Check if the enemy is still alive
                # Calculate hit chance based on enemy's accuracy and player's agility
                hit_chance = enemy.accuracy - player.agility
                if random.randint(0, 99) < hit_chance:
                    total_attack = enemy.damage + random.randint(-2, 2)
                    player.hp -= total_attack
                    print(f"\nThe {enemy.name} attacks you for {total_attack} damage!")
                else:
                    print(f"\nThe {enemy.name}'s attack missed!")
                
        elif choice == "2":
            if player.potions > 0:
                player.hp += 20 
                if player.hp > player.player_class.hp:
                    player.hp = player.player_class.hp
                player.potions -= 1  
                print("\nYou used a health potion and restored 20 HP!")
                print(f"\nYour HP: {player.hp}")
            else:
                print("\nYou don't have any potions left!")
            continue  # Continue with the player's turn after using an item
        else:
            print("\nInvalid choice! Please enter a number between 1 and 2.")

        if enemy.hp <= 0:
            print(f"\nYou defeated the {enemy.name}!")
            player.gold += random.randint(10, 20)
            player.exp += enemy.exp
            print(f"Gold gained: {player.gold}")
            print(f"Exp gained: {enemy.exp}")
            break  

        if player.hp <= 0:
            print("\nYou were defeated!")
            exit()  # Exit the program

        # Break out of combat loop if the enemy is defeated and player chooses to continue the journey
        if isinstance(location, Boss) and choice == "2":
            break

    enemy.hp = initial_enemy_hp
    if player.exp >= player.exp_to_level_up:
        player.level_up()  # Level up if experience exceeds required amount



def explore(player, stage, locations, location_index, location):
    print(location.description)
    time.sleep(2)

    while True:
        print("\n---")
        print("What will you do?")
        print("1. Explore")
        print("2. Continue Journey")
        print("3. Visit the shop")
        print("4. Quit Game")  # Add the quit option

        choice = input("Enter your choice: ")

        if choice == "1":
           combat(player, location, stage)  # Pass the location object to the combat function along with the stage
        elif choice == "2":
            if location.boss:
                print(f"You encounter the {location.boss.name}!")
                combat(player, location.boss, stage)  # Fight the boss instead of regular enemies
                if player.hp <= 0:
                    print("You were defeated!")
                    exit()  # Exit the program if player loses to boss
                else:
                    print(f"You defeated the {location.boss.name}! You can now continue your journey.")
                    break
            else:
                print("You journey onward, facing no immediate threats.")
                break
        elif choice == "3":
            shop(player, location, location_index)  # Pass the location object to the shop function
        elif choice == "4":
            print("Quitting the game...")
            exit()  # Quit the game
        else:
            print("Invalid choice!")
            
def restart_game():
    while True:
        choice = input("Do you want to restart the game? (yes/no): ")
        if choice.lower() == "yes":
            main()
        elif choice.lower() == "no":
            print("Thank you for playing!")
            exit()
        else:
            print("Invalid choice! Please enter 'yes' or 'no'.")



def main():
    intro()
    player = create_player()
    locations = create_locations()  # Generate locations with enemies and weapon titles

    while True:  # Game loop
        stage = 0
        
        while stage < len(locations):
            explore(player, stage, locations, stage, locations[stage])  # Pass the location object
            stage += 1
            if player.hp <= 0:  # Check if player loses during exploration
                print("Game Over!")
                restart_game()
            elif player.exp >= player.exp_to_level_up:
                player.level_up()  # Level up if experience exceeds required amount

        if player.hp > 0:
            print("With a final, thunderous roar, the Infamous Pyrothor falls, defeated before your might!")
            print("The kingdom erupts into cheers, celebrating your valor and heroism!")
            print("You stand as a beacon of hope, a legendary figure whose name will echo through the ages!")
            retry = input("Do you wish to embark on another adventure? (yes/no): ")
            if retry.lower() != "yes":
                break
            else:
                player.name += "⭐"  # Add a star to the player's name upon retry
                print(f"Welcome back, {player}!")
        else:
            break

if __name__ == "__main__":
    main()


