myList = [10,3,5,11,15,11,13,3,17,11,1,5,7, -2]

if all (num > 0 for num in myList):
    print("All items are positive")
if any (num <0 for num in myList):
        print("There is a negative number")
print("")


myList.sort()
print(myList)
print ("")

print ("the biggest number is", myList [13])
print("")


myList = [10,3,5,11,15,11,13,3,17,11,1,5,7, -2]
first_element = myList [0]
myList.remove(first_element)
myList.append(first_element)
print (myList)

print("")
def multiplyList(inList, multFactor):
      for i in range (len(inList)):
            inList[i] = inList[i] * multFactor
      return inList


newList = multiplyList(myList, 100)
print(newList)