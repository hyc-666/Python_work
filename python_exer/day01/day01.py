# demo01
c = float(input("Enter a degree in Celsius:"))
f = (9 / 5) * c + 32
print("%.2f Celsius is %.2f Fahrenheit"%(c,f))


# demo02
r,l = eval(input("Enter the radius and length of a cylinder:"))
a = r * r * 3.1415926535897
v = a * l
print("There area is ",a)
print("The volume is ",v)


# demo03
num = int(input("Enter a number between 0 and 1000:"))
sum = 0
while num > 0:
    sum += num % 10
    num = num // 10
print("the sum of the digits is ",sum)


# demo04
minutes = int(input("Enter the number of minutes:"))
# 一年的分钟数为 365 * 24 * 60
# 先计算年
year = minutes // (365 * 24 * 60)
# 计算天,先计算出年剩下的分钟数
# 一天的分钟数为 24 * 60
day = minutes % (365 * 24 * 60) // (24 * 60)
print("%d minutes is approximately %d years and %d days"%(minutes,year,day))


# demo05
m = float(input("Enter the amount of water in kilograms:"))
initTemp = float(input("Enter the initial temperature:"))
finalTemp = float(input("Enter the final temperature:"))
q = m * (finalTemp - initTemp) * 4184
print("The energy need is ",q)


# demo06
import math

ta = float(input("Enter the temperature in Fahrenheit between -58 and 41:"))
v = float(input("Enter the wind speed in miles per hour :"))
twc = 35.74 + 0.621 * ta - 35.75 * math.pow(v,0.16) + 0.4275 * ta * math.pow(v,0.16)
print("The wind chill index is %.5f"%(twc))


# demo07
v,a = eval(input("Enter speed and acceleration :"))
length = v * v / (2 * a)
print("The minimum runway length for this airplane is %.3f"%(length))


# demo08
number = input("Enter a integer:")
for num in reversed(number):
    print(num)


# demo09
# import math

x1,y1,x2,y2,x3,y3 = eval(input("Enter three points for a triangle:"))
# 首先计算三条边的长
side1 = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
side2 = math.sqrt((x1 - x3) ** 2 + (y1 - y3) ** 2)
side3 = math.sqrt((x2 - x3) ** 2 + (y2 - y3) ** 2)
# 计算s
s = (side1 + side2 + side3) / 3
area = math.sqrt(s * (s - side1) * (s - side2) * (s - side3))
print("The area of the triangle is ",area)


# demo10
import math

side = float(input("Enter the side:"))
area = (3 * math.sqrt(3)) / 2 * side ** 2
print("The area of the hexagon is ",area)