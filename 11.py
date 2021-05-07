date = input("輸入月及日為:").split()
sign = ['Aquarius水瓶','Pisces雙魚','Aries牡羊','Taurus金牛','Gemini雙子','Cancer巨蟹','Leo獅子','Virgo處女','Libra天秤','Scorpio天蠍','Sagittarius射手','Capricorn魔羯']
if int(date[0]) == 1:
    if int(date[1])>=21 and int(date[1])<=31:
        print("星座為:"+sign[0])
    elif int(date[1])<=21:
        print("星座為:"+sign[11])
elif int(date[0]) == 2:
    if int(date[1])<=18:
        print("星座為:"+sign[0])
    elif int(date[1])>=19 and int(date[1])<=30:
        print("星座為:"+sign[1])
elif int(date[0]) == 3:
    if int(date[1])<=20:
        print("星座為:"+sign[1])
    elif int(date[1])>=21 and int(date[1])<=31:
        print("星座為:"+sign[2])
elif int(date[0]) == 4:
    if int(date[1])<=20:
        print("星座為:"+sign[2])
    elif int(date[1])>=21 and int(date[1])<=30:
        print("星座為:"+sign[3])
elif int(date[0]) == 5:
    if int(date[1])<=21:
        print("星座為:"+sign[3])
    elif int(date[1])>=22 and int(date[1])<=31:
        print("星座為:"+sign[4])
elif int(date[0]) == 6:
    if int(date[1])<=21:
        print("星座為:"+sign[4])
    elif int(date[1])>=22 and int(date[1])<=30:
        print("星座為:"+sign[5])
elif int(date[0]) == 7:
    if int(date[1])<=22:
        print("星座為:"+sign[5])
    elif int(date[1])>=23 and int(date[1])<=31:
        print("星座為:"+sign[6])
elif int(date[0]) == 8:
    if int(date[1])<=23:
        print("星座為:"+sign[6])
    elif int(date[1])>=24 and int(date[1])<=31:
        print("星座為:"+sign[7])
elif int(date[0]) == 9:
    if int(date[1])<=23:
        print("星座為:"+sign[7])
    elif int(date[1])>=24 and int(date[1])<=30:
        print("星座為:"+sign[8])
elif int(date[0]) == 10:
    if int(date[1])<=23:
        print("星座為:"+sign[8])
    elif int(date[1])>=24 and int(date[1])<=31:
        print("星座為:"+sign[9])
elif int(date[0]) == 11:
    if int(date[1])<=22:
        print("星座為:"+sign[9])
    elif int(date[1])>=23 and int(date[1])<=30:
        print("星座為:"+sign[10])
elif int(date[0]) == 12:
    if int(date[1])<=21:
        print("星座為:"+sign[10])
    elif int(date[1])>=22 and int(date[1])<=31:
        print("星座為:"+sign[11])      