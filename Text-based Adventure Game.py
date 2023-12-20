import time

# Game Variables
inventory = []
player_health = 100

# Game Functions
def add_to_inventory(item):
    inventory.append(item)

def remove_from_inventory(item):
    if item in inventory:
        inventory.remove(item)

def show_inventory():
    print("Inventory:", inventory)

def display_status():
    print(f"Player Health: {player_health}")

def intro():
    print("Welcome to 'Lost in the Enchanted Forest'!")
    print("You find yourself trapped in a mystical forest after a magical portal mishap.")
    print("Your goal is to navigate through the forest and find a way to escape.\n")

def make_choice(choices):
    print("Choose your path:")
    for i, choice in enumerate(choices, start=1):
        print(f"{i}. {choice}")

    while True:
        try:
            choice = int(input("Enter the number of your choice: "))
            if 1 <= choice <= len(choices):
                return choice
            else:
                print("Invalid choice. Try again.")
        except ValueError:
            print("Invalid input. Enter a number.")

# Game Story
def start_game():
    intro()
    time.sleep(1)

    # Beginning of the story
    print("You wake up in a clearing surrounded by tall trees.")
    print("In front of you, there are two paths.")
    path_choices = ["Take the left path", "Take the right path", "Examine the surroundings"]
    choice = make_choice(path_choices)

    if choice == 1:
        print("You chose to take the left path.")
        add_to_inventory("Map")
        time.sleep(1)
    elif choice == 2:
        print("You chose to take the right path.")
        player_health -= 10
        display_status()
        time.sleep(1)
    else:
        print("You chose to examine the surroundings.")
        time.sleep(1)

    # Continue the story based on player choices

# Main Game Loop
if __name__ == "__main__":
    start_game()
