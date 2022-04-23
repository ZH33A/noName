print("Привет")
myList = [1, 2, 3, 4, 5, 6, 7]
n2 = 0
nn2 = 0
for i in myList:
    if i %2 == 0:
        n2 +=1
    if i %2 != 0:
        nn2 +=1

n3 = list(i%2 for i in myList).count(0)
nn3 = len(myList) - n3
print(n2, nn2)
print(n3, nn3)
