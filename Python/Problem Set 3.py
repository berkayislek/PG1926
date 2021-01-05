n = int(input("Enter number of elements: "))
finalList=[]
numList=[]

for i in range(0,n):
    numList.append(int(input("Enter number: ")))

for i in numList:
    if i==0:
        finalList.insert(0,0) #If the value from user is 0, insert 0 to left of the list
    else:
        finalList.append(i)

print(numList)
print("Carrying 0s to the beginning:")
print(finalList)