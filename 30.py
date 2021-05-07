m = int(input("小明身上有幾元:"))
n = int(input("販賣機有幾種飲料:"))
list1 = []
sum = 0
for i in range(n):
    price = input(":")
    list1.append(price)
for x in range(n):
    if int(list1[x])<=m:
        sum+=1
    else:
        sum = sum
print(sum)