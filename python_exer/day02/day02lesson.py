# ord('c') #返回一个字符的十进制ASCII码
# chr(100) #返回一个字符，参数是一个数字
# round(-3.4)  # 四舍五入，负数不产生影响
#
# import math
# math.ceil(3.14)   # 向上取整
# math.floor(3.14)  # 向下取整

# demo14
# 用三角形的三边计算三个角
# a,b,c = eval(input("请输入三角形的三条边:"))
# A = math.acos((a * a - b * b - c * c) / (-2 * b * c))
# B = math.acos((b * b - a * a - c * c) / (-2 * a * c))
# C = math.acos((c * c - b * b - a * a) / (-2 * a * b))
# print("A = ",math.degrees(A))
# print("B = ",math.degrees(B))
# print("C = ",math.degrees(C))


# demo15
# sides = int(input("Enter the number od sides:"))
# side  = float(input("Enter the side:"))
#
# area = (sides * side ** 2) / (4 * math.tan(math.pi / sides))
#
# print("The area of the polygon is ",area)


# demo19
# set1 = [[1,3,5,7],[9,11,13,15],[17,19,21,23],[25,27,29,31]]
# set2 = [[2,3,6,7],[10,11,14,15],[18,19,22,23],[26,27,30,31]]
# set3 = [[4,5,6,7],[12,13,14,15],[20,21,22,23],[28,29,30,31]]
# set4 = [[8,9,10,11],[12,13,14,15],[24,25,26,27],[28,29,30,31]]
# set5 = [[16,17,18,19],[20,21,22,23],[24,25,26,27],[28,29,30,31]]
# count = 0
# print("你的生日在这个集合中吗？y/n")
# for set in set1:
#     print(set)
# if input() == 'y':
#     count += 1
# print("你的生日在这个集合中吗？y/n")
# for set in set2:
#     print(set)
# if input() == 'y':
#     count += 1
# print("你的生日在这个集合中吗？y/n")
# for set in set3:
#     print(set)
# if input() == 'y':
#     count += 4
# print("你的生日在这个集合中吗？y/n")
# for set in set4:
#     print(set)
# if input() == 'y':
#     count += 8
# print("你的生日在这个集合中吗？y/n")
# for set in set5:
#     print(set)
# if input() == 'y':
#     count += 16
# print("你的生日是 ",count)


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
# a,b,c = eval(input("Enter a,b,c:"))
# dst = b ** 2 - 4 * a * c
# if dst < 0:
#     print("The equation has no real roots!")
# elif dst == 0:
#     r = -1 * (b / (2 * a))
#     print("The root is ",r)
# else:
#     r1 = (-b + dst ** 0.5) / (2 * a)
#     r2 = (-b - dst ** 0.5) / (2 * a)
#     print("The roots is %f and %f"%(r1,r2))
