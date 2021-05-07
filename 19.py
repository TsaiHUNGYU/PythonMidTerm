times = int(input("組數為:"))
count = 1
while count<=times:
    guest = input("第"+str(count)+"組:").split()
    price = int(guest[0])*250 + int(guest[1])*175
    print("第"+str(count)+"組應收費用:"+str(price))
    count += 1