myList = [10,3,5,11,15,11,13,3,17,11,1,5,7]

target = int(input("what is the item you are looking for?>>"))
if all (num > 0 for num in myList):
    print("All items are positive")
    if any (num <0 for num in myList):
        print("There is a negative number")
