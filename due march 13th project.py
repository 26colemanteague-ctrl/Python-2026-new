
global playerName
playerName= input()
import os, time, random 
choice = input().strip().lower()



options =("left", "middel", "right", "up", "down", "complete darkness", "and a way out")


def start():
    os.system ('cls' if os.name == 'nt' else 'clear')
    print(" hello welcom to the game. what is you name?")
    newRoom()



def sameRoom():
    os.system ('cls' if os.name == 'nt' else 'clear')
    print()


def newRoom():
    os.system ('cls' if os.name == 'nt' else 'clear')
    print("you find your self in a new room and see",random.choice(options), random.choice(options), random.choice(options))
    if choice == "way out":
        print ("congrat you made your way out.")



def down():
    os.system ('cls' if os.name == 'nt' else 'clear')
    if  choice == "down":
        down()
        print("you crowl down a tight whole leading to an other room.")
        newRoom()

def right():
    os.system ('cls' if os.name == 'nt' else 'clear')
    if choice == "right":
        right()
        print("you have desided to go right.")
        print("you find your self seeing a way", random.choice(options))
        newRoom()


def left():
    os.system ('cls' if os.name == 'nt' else 'clear')
    if choice == "left":
        print(random.choice(options))
        print("you have desided to go left.")
        newRoom()


def up():
    os.system ('cls' if os.name == 'nt' else 'clear')
    if choice == "up":
        up()
        print("you desided to clime up the latter.")
        newRoom()

def middel():
    os.system ('cls' if os.name == 'nt' else 'clear')
    if choice == "middel":
        middel()
        print("you have desided to go on the middel.")
        newRoom()

def wayOut():
    os.system ('cls' if os.name == 'nt' else 'clear')
    if choice == "way out":
        print ("you see light at the end of the tunoal.")
        print ()
        print ("after you leave and you eyes adjust you see your car at the bottem of the hill and you drive home.")


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


def main():
    start()




if __name__ == "__main__":
    main()



