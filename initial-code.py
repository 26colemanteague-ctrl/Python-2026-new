# os = operating system.
import os, time
# make the text type out and be seen being type insted of it just apering
def slowText(text, delay=0.1):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print() 

# the starting of the code that is the game
def start():
    global playerName #establishes your name as a global variable
    os.system('cls' if os.name == 'nt' else 'clear')
    slowText("Welcome to the game! Please enter your name: ")
    playerName = input()
    slowText("Hello, {}! You find yourself in the living room of a mysterious house.".format(playerName))
    slowText("From here, you can go to the kitchen, the bedroom, or the garden.")
    # Further game logic would go here
    livingRoom()

# this gives you the chose of where you want to go/contution of start
def livingRoom():
    global backpack
    os.system('cls' if os.name == 'nt' else 'clear')
    print("backpack: {}".format(backpack))
    slowText("You are in the living room. There are doors to the kitchen, bedroom, and garden. You can also look for items.")
    slowText("What would you like to do?")
    choice = input().strip().lower()
    if choice == "kitchen":
        kitchen()
    elif choice == "bedroom":
        bedroom()
    elif choice == "garden":
        garden()
    elif choice == "look around":
        if searchBackpack(backpack, "oreos"):
            slowText("You decided to scan the room. And you found nothing.")
        else:
            slowText("You decided to scan the room. You find a half-eaten pack of oreos. Do you want to pick them up?")
            choice = input().strip().lower()
            if choice == "yes":
                backpack.append("oreos")
                print(backpack) # this line is only for testing
        time.sleep(2)
        livingRoom()

def kitchen ():
    os.system('cls' if os.name == 'nt' else 'clear')
    slowText("You are in the kitchen. There is a doors to the living room.")
    slowText("What would you like to do?")
    global backpack
    choice = input().strip().lower()
    if choice == "living room":
        livingRoom()
    elif choice == "look for items":
        if searchBackpack(backpack, "knife"):
            slowText("You decided to scan the room. And you found nothing.")
        else:
            slowText("You decided to scan the room. You find a knife. Do you want to pick them up?")
            choice = input().strip().lower()
            if choice == "yes":
                backpack.append("knife")
                print(backpack) # this line is only for testing
        time.sleep(2)
        kitchen()

def bedroom():
    os.system('cls' if os.name == 'nt' else 'clear')
    slowText("You are in the bed room. there is a door to the living room.")
    slowText("What would you like to do?")
    choice = input().strip().lower()
    if choice == "living room":
        livingRoom()
    else:
        print("Invalid choice. Please try again.")
        bedroom()


def garden():
    os.system('cls' if os.name == 'nt' else 'clear')
    slowText("You are in the garden. There is a door to the living room.")
    slowText("What would you like to do?")
    choice = input().strip().lower()
    if choice == "living room":
        livingRoom()
    else:
        print("Invalid choice. Please try again.")
        garden()


def searchbackpack(backpake, item):
    # this function should return true if you have something in your bag
    found = False
    for i in range(len(backpack)):
        if backpack[i] == item:
            found = True
    


# alwose you to inter your name and start the program
playerName = ""
backpack = []
start()