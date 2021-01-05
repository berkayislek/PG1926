n = int(input("Enter number of elements: "))
numList=[]

for i in range(0,n):
    numList.append(int(input("Enter number: ")))

biggestNumber=numList[0]
for i in numList:
    if i > biggestNumber:
        biggestNumber=i

print("The biggest number in your list is:",biggestNumber)