aa = int(input("輸入第一行正整數 :"))
bb = str(input("第二行數列中的數字為:"))
cc = bb.split(" ")
list1=[]
x = 1
sum = 0
while x <= aa:
    for i in range(len(cc)):
        if int(cc[i]) == x:
            sum += 1
        else:
            sum = sum
    list1.append(sum)
    sum = 0
    x +=1


m = max(list1)


if m == 1:
    print("每個數字剛好只出現一次")

else:
    for y in cc:
        if cc.count(y) == m:
            print("最大出現次數為 :",y)
            print("出現次數為 :",m)
            break