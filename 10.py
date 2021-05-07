a = input("輸入N及M為:").split()
list1 = []
count = 1
while count <= int(a[0]):
    b = input("輸入矩陣數值第"+str(count)+"列為:").split()
    list1.append(b)
    count += 1   
print(list1)

for x in range(int(a[1])):
    tmp = ""
    for y in range(int(a[0])):
        tmp += list1[y][x] + " "
    print("輸出矩陣數值第"+str(x+1)+"列為 :"+tmp)
    



