a=input(":")
b=list(a)
c=list(a)
for j in range(len(b)-1):
    for i in range(0,len(b)-1):
        if b[i]>b[i+1]:
            tmp=b[i]
            b[i]=b[i+1]
            b[i+1]=tmp
for j in range(len(b)-1):
    for i in range(0,len(b)-1):
        if c[i]<c[i+1]:
            tmp=c[i]
            c[i]=c[i+1]
            c[i+1]=tmp
d=""
for i in b:
    d+=i
e=""
for i in c:
    e+=i
print(int(e)-int(d))