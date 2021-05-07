s = input("檢測的字串(end結束):")
st = input("檢測的單一字元 :")
while s != "end":
    if st in s :
        count = s.count(st)
        print("字元"+str(st)+"出現次數為:"+str(count))
    else:
        print("沒有該字元!")
    s = input("檢測的字串(end結束):")
    if s == "end":
        break
    st = input("檢測的單一字元 :")
    