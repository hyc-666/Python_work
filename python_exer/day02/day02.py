# python实训第二天作业题

# demo11
import time
currentTime = time.time()
totalSeconds = int(currentTime)
currentSecond = totalSeconds % 60
totalMinutes = totalSeconds // 60
currentMinute = totalMinutes % 60
totalHours = totalMinutes // 60
currentHour = totalHours % 24
d = int(input("Enter the time zone offset to GMT:"))  # 时差
offset = currentHour + d  # 偏移量
now = 0
if offset < 0:
    now = 24 - offset
elif offset > 24:
    now = offset - 24
print("The current time is",now,":",currentMinute,":",currentSecond,)


# demo12
import math
amount = float(input( "Enter the monthly saving amount:"))
amount = 100 * (1 + 0.00417)
i = 0
while i < 5:
    amount = (100 + amount) * (1 + 0.00417)
    i = i + 1
print("After the sixth month, the account value is ",amount)


# demo13
account = float(input("Enter investment amount:"))
rate = float(input("Enter annual interest rate:")) / 100
monthRate = rate / 12
years = int(input("Enter number of years:"))
month = math.floor(years * 12)
future = account * (1 + monthRate) ** month
print("Accumulated value is ",future)


# demo14
# 用三角形的三边计算三个角
a,b,c = eval(input("请输入三角形的三条边:"))
A = math.acos((a * a - b * b - c * c) / (-2 * b * c))
B = math.acos((b * b - a * a - c * c) / (-2 * a * c))
C = math.acos((c * c - b * b - a * a) / (-2 * a * b))
print("A = ",math.degrees(A))
print("B = ",math.degrees(B))
print("C = ",math.degrees(C))


# demo15
sides = int(input("Enter the number od sides:"))
side  = float(input("Enter the side:"))
area = (sides * side ** 2) / (4 * math.tan(math.pi / sides))
print("The area of the polygon is ",area)


# demo16
number = input("Enter a integer:")
print("The reversed number is ",end = "")
for num in reversed(number):
    print(num,end = "")
print()


# demo17
money = int(float(input("Enter a number of money:")) * 100)
yuan = money // 100  # 美元个数
other = money % 100
fen25 = other // 25  # 两角五分硬币个数
other = other % 25
fen10 = other // 10  # 一角硬币个数
other = other % 10
fen5 = other // 5  # 五分硬币个数
fen1 = other % 5  # 一分硬币个数
print("美元个数 = %d,两角五分硬币 = %d 一角硬币 = %d,五分硬币 = %d, 一分硬币 = %d"%(yuan,fen25,fen10,fen5,fen1))


# demo18
name = input("Enter employee's name:")
workTime = int(input("Enter number of hours worked in a week:"))  # 每周工作时间
hourFee = float(input("Enter hourly pay rate:"))  # 每小时报酬
lRate = float(input("Enter federa1 tax withholding rate:"))  # 联盟扣税率
zRate = float(input("Enter state tax withholding rate:"))  # 州扣税率
salary = workTime * hourFee  # 总薪水
print()
print("Employee name:",name)
print("Hours worked:",workTime)
print("Pay rate:$",hourFee,sep = "")
print("Gross by:$",salary,sep = "")
print("Deductions:")
print("  Federal Withholding(%.2f):$%f"%(lRate,salary * lRate))
print("  State Withholding(%.2f):$%f"%(zRate,salary * zRate))
print("  Total Deduction:$%f"%(salary * zRate + salary * lRate))
print("Net Pay:$",salary - (salary * zRate + salary * lRate),sep = "")


# demo19
set1 = [[1,3,5,7],[9,11,13,15],[17,19,21,23],[25,27,29,31]]
set2 = [[2,3,6,7],[10,11,14,15],[18,19,22,23],[26,27,30,31]]
set3 = [[4,5,6,7],[12,13,14,15],[20,21,22,23],[28,29,30,31]]
set4 = [[8,9,10,11],[12,13,14,15],[24,25,26,27],[28,29,30,31]]
set5 = [[16,17,18,19],[20,21,22,23],[24,25,26,27],[28,29,30,31]]
count = 0
print("你的生日在这个集合中吗？y/n")
for set in set1:
    print(set)
if input() == 'y':
    count += 1
print("你的生日在这个集合中吗？y/n")
for set in set2:
    print(set)
if input() == 'y':
    count += 1
print("你的生日在这个集合中吗？y/n")
for set in set3:
    print(set)
if input() == 'y':
    count += 4
print("你的生日在这个集合中吗？y/n")
for set in set4:
    print(set)
if input() == 'y':
    count += 8
print("你的生日在这个集合中吗？y/n")
for set in set5:
    print(set)
if input() == 'y':
    count += 16
print("你的生日是 ",count)


# demo20
weight = float(input("以千克（kg）为单位输入体重："))
height = float(input("以米为单位输入身高："))
BMI = weight / (height ** 2)
if BMI < 18.5:
    print("超轻")
elif BMI >= 18.5 and BMI < 25.0:
    print("标准")
elif BMI >= 25.0 and BMI < 30.0:
    print("超重")
else:
    print("痴肥")


# demo21 判断闰年
# 闰年的判定方法是：4年一润，百年不润，400年一润
year = int(input("输入一个年份："))
if year % 4 == 0 and year % 100 != 0:
    print("%d年是个闰年"%(year))
elif year % 400 == 0:
    print("%d年是个闰年"%(year))
else:
    print("%d年不是个闰年"%(year))


# demo22
# 生成随机的两位数
import random
luckyNum = random.randint(10,99)
key = str(luckyNum)
guess = input("输入你猜的数字：")
if guess == str(luckyNum):
    print("恭喜你中奖了，奖金为 10 000 美元")
elif guess == reversed(str(luckyNum)):
    print("恭喜你中奖了，奖金为 3 000 美元")
elif guess[0] == key[0] or guess[0] == key[1] or guess[1] == key[0] or guess[1] == key[1]:
    print("恭喜你中奖了，奖金为 1 000 美元")
else:
    print("很遗憾，没有中奖！")
print("本次开奖为: ", key)


# demo23
# 解一元二次方程
a,b,c = eval(input("Enter a,b,c:"))
dst = b ** 2 - 4 * a * c
if dst < 0:
    print("The equation has no real roots!")
elif dst == 0:
    r = -1 * (b / (2 * a))
    print("The root is ",r)
else:
    r1 = (-b + dst ** 0.5) / (2 * a)
    r2 = (-b - dst ** 0.5) / (2 * a)
    print("The roots is %f and %f"%(r1,r2))


# demo24
a,b,c,d,e,f = eval(input("Enter a,b,c,d,e and f:"))
dst = a * d - b * c
if dst == 0:
    print("The equation has no solution!")
else:
    x = (e * d - b * f) / (a * d - b * c)
    y = (a * f - e * c) / (a * d - b * c)
    print("x = %f and y = %f"%(x,y))


# demo25
today = int(input("Enter today's day:"))
step = int(input("Enter the number of days elapsed since today:"))
# 定义一周内的天数
weeks = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
future = today + step
print("Today is " + weeks[today] + " and the future day is " + weeks[future % 7])


# demo26
weight1,price1 = eval(input("Enter weight and price for package 1:"))
weight2,price2 = eval(input("Enter weight and price for package 2:"))
unitPrice1 = weight1 / price1
unitPrice2 = weight2 / price2
if unitPrice1 < unitPrice2:
    print("Package 1 has the better price.")
elif unitPrice1 > unitPrice2:
    print("Package 2 has the better price.")
else:
    print("Package 2 and packge 1 have same price.")
