s = input(":").split()
sum = 0
for x in range(len(s)):
    if s[x]=="A":
        sum += 14
    elif s[x]=="K":
        sum += 13
    elif s[x]=="Q":
        sum += 12
    elif s[x]=="j":
        sum += 11
    else:
        sum += int(s[x])
print(sum)