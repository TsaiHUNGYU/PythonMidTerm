x = int(input("X 軸座標 :"))
y = int(input("Y 軸座標 :"))
sum = x*x + y*y 
if x > 0 and y > 0 :
    print("該點位於第一象限，離原點距離為根號" ,sum)
elif x < 0 and y > 0 :
    print("該點位於第二象限，離原點距離為根號" , sum)
elif x < 0 and y < 0 :
    print("該點位於第三象限，離原點距離為根號" , sum) 
elif x > 0 and y < 0 :
    print("該點位於第四象限，離原點距離為根號" , sum)
elif x == 0 and y == 0 :
    print("該點位於原點")
elif x == 0 :
    if y > 0 :
        print("該點位於上半平面 Y 軸上，離原點距離為根號" , sum)
    else :
        print("該點位於下半平面 Y 軸上，離原點距離為根號" , sum)
elif y == 0 :
    if x > 0:
        print("該點位於右半平面 X 軸上，離原點距離為根號" , sum)
    else :
        print("該點位於左半平面 X 軸上，離原點距離為根號" , sum)