use = int(input("請輸入用電度數 :"))
if use <= 120 :
    summer = 2.10 * use
    nonSummer = 2.10 * use
elif use <= 330 and use>120:
    use = use - 120
    summer = 2.10 * 120 + use * 3.02
    nonSummer = 2.10 * 120 + use * 2.68
elif use <= 500 and use > 120 :
    use = use -120 - 210  #121~330區間為210
    summer = 2.10 * 120 + 3.02 * 210 + use * 4.39 
    nonSummer = 2.10 * 120 + 2.68 * 210 + use * 3.61
elif use <= 700 and use > 120 :
    use = use - 120 - 210 - 170 #331~500區間為170
    summer = 2.10 * 120 + 3.02 * 210 + 4.39 * 170 + 4.97 * use
    nonSummer = 2.10 * 120 + 2.68 * 210 + 3.61 * 170 + 4.01 * use
elif use > 701 :
    use = use - 120 - 210 - 170 - 200 #501~700區間為200
    summer = 2.10 * 120 + 3.02 * 210 + 4.37 * 170 + 4.97 * 200 + 5.63 * use
    nonSummer = 2.10 * 120 + 2.68 * 210 + 3.61 * 170 + 4.01 * 200 + 4.50 * use
print("Summer months:",summer)
print("Non-Summer months:",nonSummer)