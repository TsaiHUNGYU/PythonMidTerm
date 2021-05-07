num = input("請輸入一整數序列為:").split()
sum = 0
list1 = []
for i in range(len(num)):
    sum = num.count(num[i])
    list1.append(sum)
    sum = 0


count = max (list1)

if count >= len(num)/2:
    for x in num:
        if num.count(x) == count:
            print("過半元素為:"+x)
            break

else:
    print("過半元素 : NO")
