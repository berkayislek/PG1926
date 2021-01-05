n = int(input("Enter number of elements: "))
numList=[]

for i in range(0,n):
    numList.append(int(input("Enter number: ")))

numList.sort()
print("The biggest number in your list is:",numList[-1])