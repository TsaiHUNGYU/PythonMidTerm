a=list(input("輸入答案(4位數):"))
b=list(input("please enter your answer :"))
A=0
B=0
while True:
    ending = ""
    for x in range(4):
        ending += b[x]
    if ending == "0000":
        break 
    else:   
        for i in range(len(a)):
            for y in range(len(b)):
                if b[i]==a[y] and i==y :
                    A+=1
                    break
                elif b[i]==a[y] and i!=y:
                    B+=1
                    break
    print(A,"A",B,"B")
    A = 0
    B = 0
    b=list(input("please enter your answer :"))
