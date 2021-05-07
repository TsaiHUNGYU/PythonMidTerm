a = input("甲方的數字:").split()
b = input("乙方的數字:").split()
tmp = 0
result = ["和","贏","輸"]
list1 = []
for i in range(len(a)):
    if a[i]>b[i]:
        tmp += 1
        list1.append(tmp)
    elif a[i]<b[i]:
        tmp += 2
        list1.append(tmp)
    elif a[i] == b[i]:
        tmp = tmp
        list1.append(tmp)
    tmp = 0
gr=""
for x in range(len(list1)):
    gr = str(gr) + str(result[list1[x]])
print("洗刷刷結果:"+gr)

