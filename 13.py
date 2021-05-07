s = list(input("輸入一字元為 :"))
a = reversed(list(s))
if list(a) == list(s) :
    print("YES!")
else:
    print("NO!")
