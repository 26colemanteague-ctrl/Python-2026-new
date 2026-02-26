print(" hello welcom to the game. what is you name?")
global playerName
playerName= input()
import os, time, random 
options =("left", "middel", "right", "up", "down")
print(random.choice(options))
os.system ('cls' if os.name == 'nt' else 'clear')
print ("you have woke up in a stange cave only lighten by a torch on the ground. you pick up the torch and see a path to", random.choice(options))
choice = input().strip().lower()
if choice == "left":
    #left()
    print("you have desided to go left.")
elif choice == "middel":
    #middle()
    print("you have desided to go on the middel.")
elif choice == "right":
    #right()
    print("you have desided to go right.")
elif choice == "up":
    #up()
    print("you desided to clime up the latter.")
elif choice == "down":
    #down
    print("you crowl down a tight whole leading to an other room.")
else: 
    #stay
    print("you can't desided maybey take another look.")














playerName = ""