myList=[11, 22, -12, 99, 82, 93, 35, -50, 16]
total=0

for i in myList:
    if (i>0) and (i%2==0):
        total=total+i
print("양수이면서 짝수인 요소들의 합 :", total)
