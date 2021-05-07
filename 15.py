num = input("輸入一組四位數字 :").split()
for x in range(len(num)):
    num[x] = (int(num[x])+7)%10

pt = num[0]
num[0] = num[2]
num[2] = pt

pt1 = num[1]
num[1] = num[3]
num[3] = pt1



pw=""
for y in range(len(num)):
    pw = str(pw) + str(num[y])
print("輸出加密後的數字為 :"+pw)
