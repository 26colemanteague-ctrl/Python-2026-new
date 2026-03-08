print(" hello welcom to the game. what is you name?")
global playerName
playerName= input()
import os, time, random 
choice = input().strip().lower()



options =("left", "middel", "right", "up", "down", "conplet darkness")



def sameRoom():
    os.system ('cls' if os.name == 'nt' else 'clear')
    print()

def newRoom():
    os.system ('cls' if os.name == 'nt' else 'clear')
    print("you find your self in a new room and see",random.choice(options), random.choice(options), random.choice(options))
if sameRoom():
    newRoom()

def down():
    os.system ('cls' if os.name == 'nt' else 'clear')

def right():
    os.system ('cls' if os.name == 'nt' else 'clear')


def left():
    os.system ('cls' if os.name == 'nt' else 'clear')
if choice == "left":
    print(random.choice(options))
    newRoom()


def up():
    os.system ('cls' if os.name == 'nt' else 'clear')

def middel():
    os.system ('cls' if os.name == 'nt' else 'clear')


if choice == "left":
    left()
elif choice == "right":
    right()
elif choice == "middle":
    middel()
elif choice == "up":
    up()
elif choice == "down":
    down()
else:
    print ("you can't deside maybe take another look.")

    

print(random.choice(options))
os.system ('cls' if os.name == 'nt' else 'clear')
print ("you have woke up in a stange cave only lighten by a torch on the ground. you pick up the torch and see a path to", random.choice(options), random.choice(options), random.choice(options))
choice = input().strip().lower()
if choice == "left":
    left()
    print("you have desided to go left.")
    newRoom()
elif choice == "middel":
    middel()
    print("you have desided to go on the middel.")
    newRoom()
elif choice == "right":
    right()
    print("you have desided to go right.")
    print("you find your self seeing a way", random.choice(options))
    newRoom()
elif choice == "up":
    up()
    print("you desided to clime up the latter.")
    newRoom()
elif choice == "down":
    down()
    print("you crowl down a tight whole leading to an other room.")
    newRoom()

else: 
    print("you can't desided maybe take another look.")
    sameRoom()











playerName = ""