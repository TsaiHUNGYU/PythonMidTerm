a = str(input("輸入月租費形式及通話時間 :"))
#print(type(a))
#print(a)
b = a.split(" ")
#print(type(b))
#print(b)
sum = 0
print(b[0])
print(type(b[1]))
list1 = []
list1.append(int(b[0]))
list1.append(int(b[1]))
print(list1[0])
if list1[0] == 186:
    if list1[1] * 0.09  <= 372:
        sum = list1[1] * 0.09 * 0.9
    else:
        sum = list1[1] * 0.09 * 0.8
elif list1[0] == 386:
    if list1[1] * 0.08 <= 772:
        sum = list1[1] * 0.08 * 0.8
    else:
        sum = list1[1] * 0.08 * 0.7
elif list1[0] == 586:
    if list1[1] * 0.07 <= 1172:
        sum = list1[1] * 0.07 * 0.7
    else:
        sum = list1[1] * 0.07 * 0.6
elif list1[0] == 986:
    if list1[1] * 0.06 <= 1972:
        sum = list1[1] * 0.06 * 0.6
    else:
        sum = list1[1] * 0.07 * 0.5
sum = round(sum,0)
print("通話費為 :" , sum)