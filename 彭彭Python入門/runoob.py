# print("Hello World!")

# 数字求和
    # num1 = input("請輸入第一個數字: ")
    # num2 = input("請輸入第二個數字: ")
    # sum = float(num1) + float(num2)
    # print("數字{0}和{1}相加結果為:{2}".format(num1, num2, sum))

# 计算实数和复数平方根
    # 导入复数数学模块
    # num = float(input('请输入一个数字： '))
    # num_sqrt = num ** 0.5
    # print(' %0.3f 的平方根为 %0.3f'%(num ,num_sqrt))
    # a = '%6.1f%%'% 100   #100.0%
    # 小数点前面的数字对产生的结果没有任何影响，小数点后面的数字表示保留小数点几位。

    # import cmath
    # num = int(input("请输入一个数字: "))
    # num_sqrt = cmath.sqrt(num)
    # print('{0} 的平方根为 {1:0.3f}+{2:0.3f}j'.format(num ,num_sqrt.real,num_sqrt.imag))
    # # cmath.sqrt(z)  Return the square-root of z
    # # C==c.real+c.imag*j的複數表示方法為複數的笛卡爾表示法

# 一元二次方程式(主要特點是未知項的最高次數是2)
    # 二次方程式 ax**2 + bx + c = 0
    # a、b、c 用户提供，为实数，a ≠ 0
    # 导入 cmath(复杂数学运算) 模块
    # import cmath 
    # a = float(input('输入 a: '))
    # b = float(input('输入 b: '))
    # c = float(input('输入 c: '))
    # 计算一元二次方程式根的判別式為  ∆ = b^2-4ac。
    # d = (b**2) - (4*a*c) 
    # 两种求解方式
    # sol1 = (-b-cmath.sqrt(d))/(2*a) # ∆ > 0 , X(1,2) = -b + (b^2-4ac)**0.5
    # sol2 = (-b+cmath.sqrt(d))/(2*a) # ∆ < 0 , X(1,2) = -b + (4ac-b^2)**0.5
    # print('结果为 {0} 和 {1}'.format(sol1,sol2))

# 計算三角形的面積
    #海龍公式：設∆ABC 的三邊長分別為a, b, c，且s = a + b + c 2 ， 
             #則∆ABC = √ s(s - a)(s - b)(s - c)
    # a = float(input('输入三角形第一边长: '))
    # b = float(input('输入三角形第二边长: '))
    # c = float(input('输入三角形第三边长: '))
    # 计算半周长
    # s = (a + b + c) / 2
    # 计算面积
    # area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
    # print('三角形面积为 %0.2f' %area)

# 計算圓的面積
    # 定义一个方法来计算圆的面积
    # def findArea(r):
    #     PI = 3.141592
    #     return PI * (r*r)
    # 调用方法
    # print("圆的面积为 %.6f" % findArea(9))

# 隨機數生成
    # import random
    # print(random.randint(0,9))

# 攝氏溫度轉華氏溫度 公式为 celsius * 1.8 = fahrenheit - 32。
    # 用户输入摄氏温度
    # celsius = float(input('输入摄氏温度: '))
    # 计算华氏温度
    # fahrenheit = (celsius * 1.8) + 32
    # print('%0.1f 摄氏温度转为华氏温度为 %0.1f ' %(celsius,fahrenheit))

# 交換變量
    # x = input('输入 x 值: ')
    # y = input('输入 y 值: ')
    # 不使用臨時變量，並交換
    # x,y = y,x
    # 使用臨時變量，並交換
    # temp = x
    # x = y
    # y = temp
    # print('交换后 x 的值为: {}'.format(x))
    # print('交换后 y 的值为: {}'.format(y))

# 判断字符串是否为数字
    # def is_number(s):
    #     try:
    #         float(s)
    #         return True
    #     except ValueError:
    #         pass
    #     try:
    #         import unicodedata
    #         unicodedata.numeric(s) #將unicode 轉換為數字
    #         return True
    #     except (TypeError, ValueError):
    #         pass
    #     return False
    # 测试字符串和数字
    # print(is_number('foo'))   # False
    # print(is_number('1.3'))   # True
    # print(is_number('-1.37')) # True
    # print(is_number('1e3'))   # True
    # 测试 Unicode
    # 阿拉伯语 5
    # print(is_number('٥'))  # True
    # 泰语 2
    # print(is_number('๒'))  # True
    # 中文数字
    # print(is_number('四')) # True
    # 版权号
    # print(is_number('©'))  # False

# 判断闰年
    # year = int(input("输入一个年份: "))
    # if (year % 4) == 0:
    #    if (year % 100) == 0:
    #        if (year % 400) == 0:
    #            print("{0} 是闰年".format(year))   # 整百年能被400整除的是闰年
    #        else:
    #            print("{0} 不是闰年".format(year))
    #    else:
    #        print("{0} 是闰年".format(year))       # 非整百年能被4整除的为闰年
    # else:
    #    print("{0} 不是闰年".format(year))

# 程序用于检测用户输入的数字是否为质数
    # num = int(input("请输入一个数字: "))
    # if num > 1: # 质数大于 1
    #    # 查看因子
    #    for i in range(2,num):
    #        if (num % i) == 0:
    #            print(num,"不是质数")
    #            print(i,"乘于",num//i,"是",num)
    #            break
    #    else:
    #        print(num,"是质数")
    # else:
    #    print(num,"不是质数") # 如果输入的数字小于或等于 1，不是质数

# 输出指定范围内的質数
    # lower = int(input("输入区间最小值: "))
    # upper = int(input("输入区间最大值: "))
    # for num in range(lower,upper + 1):
    #     # 質數大於 1
    #     if num > 1:
    #         for i in range(2,num):
    #             if (num % i) == 0:
    #                 break
    #         else:
    #             print(num)

# 階乘 整数的阶乘（英语：factorial）即：n!=1×2×3×...×n。
    # num = int(input("请输入一个数字: "))
    # factorial = 1
    # 查看数字是负数，0 或 正数
    # if num < 0:
    #    print("抱歉，负数没有阶乘")
    # elif num == 0:
    #    print("0 的阶乘为 1")
    # else:
    #    for i in range(1,num + 1):
    #        factorial = factorial*i
    #    print("%d 的阶乘为 %d" %(num,factorial))

# 九九乘法表
    # for i in range(1, 10):
    #     for j in range(1, i+1):
    #         print('{}x{}={}\t'.format(j, i, i*j), end='') # \t	水平制表（Tab=4個空格）end=' '意思是末尾不换行，加空格。
    #     print()

# 斐波那契数列
    # 指的是这样一个数列 0, 1, 1, 2, 3, 5, 8, 13,特别指出：
    # 第0项是0，第1项是第一个1。从第三项开始，每一项都等于前两项之和。
    # nterms = int(input("你需要几项？"))
    # # 第一和第二项
    # n1 = 0
    # n2 = 1
    # count = 2 
    # 判断输入的值是否合法
    # if nterms <= 0:
    #    print("请输入一个正整数。")
    # elif nterms == 1:
    #    print("斐波那契数列：")
    #    print(n1)
    # else:
    #    print("斐波那契数列：")
    #    print(n1,",",n2,end=" , ")
    #    while count < nterms:
    #        nth = n1 + n2
    #        print(nth,end=" , ")
    #        # 更新值
    #        n1 = n2
    #        n2 = nth
    #        count += 1
# 阿姆斯壯數 (指定期间内的)
    # 如果一个n位正整数等于其各位数字的n次方之和,则称该数为阿姆斯壯數。 
    # 例如1^3 + 5^3 + 3^3 = 153。
    # 1000以内的阿姆斯特朗数： 1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407。
    # lower = int(input("最小值: "))
    # upper = int(input("最大值: "))
    # for num in range(lower,upper + 1):
    #    # 初始化 sum
    #    sum = 0
    #    # 指数
    #    n = len(str(num))
    
    #    # 检测
    #    temp = num
    #    while temp > 0:
    #        digit = temp % 10 # 餘數
    #        sum += digit ** n # 次方
    #        temp //= 10       # 取整除-返回商的整數部分（向下取整）
    #    if num == sum:
    #        print(num)

# 進制轉二進制、八進制、十六進制
    # dec = int(input("输入数字："))
    # print("十进制数为：", dec)
    # print("转换为二进制为：", bin(dec))
    # print("转换为八进制为：", oct(dec))
    # print("转换为十六进制为：", hex(dec))

#  ASCII碼與字符相互轉換
    # c = input("请输入一个字符: ")
    
    # # 用户输入ASCII码，并将输入的数字转为整型
    # a = int(input("请输入一个ASCII码: "))
    
    # print( c + " 的ASCII 码为", ord(c))
    # print( a , " 对应的字符为", chr(a))

# 最大公約數算法
    # def hcf(x, y):
    #    """该函数返回两个数的最大公约数"""
    #    if x > y:
    #        smaller = y
    #    else:
    #        smaller = x
    
    #    for i in range(1,smaller + 1):
    #        if((x % i == 0) and (y % i == 0)):
    #            hcf = i
    #    return hcf

    # num1 = int(input("输入第一个数字: "))
    # num2 = int(input("输入第二个数字: "))
    # print( num1,"和", num2,"的最大公约数为", hcf(num1, num2))

# 最小公倍數算法
    # def lcm(x, y):
    #    if x > y:
    #        greater = x
    #    else:
    #        greater = y
    
    #    while(True):
    #        if((greater % x == 0) and (greater % y == 0)):
    #            lcm = greater
    #            break
    #        greater += 1
    #    return lcm

    # num1 = int(input("输入第一个数字: "))
    # num2 = int(input("输入第二个数字: "))
    # print( num1,"和", num2,"的最小公倍数为", lcm(num1, num2))

# 生成日曆
    # import calendar
    # # 输入指定年月
    # yy = int(input("输入年份: "))
    # mm = int(input("输入月份: "))
    # print(calendar.month(yy,mm))

# 写文件
    # with open("test.txt", "wt") as out_file:
    #     out_file.write("該文本會寫入到文件中\n看到我了吧！")
    # # Read a file
    # with open("test.txt", "rt") as in_file:
    #     text = in_file.read()
    # print(text)

# 字符串判斷
    # print("測試實例")
    # str = "runoob.com"
    # print(str.isalnum()) # 判断所有字符都是数字或者字母
    # print(str.isalpha()) # 判断所有字符都是字母
    # print(str.isdigit()) # 判断所有字符都是数字
    # print(str.islower()) # 判断所有字符都是小写
    # print(str.isupper()) # 判断所有字符都是大写
    # print(str.istitle()) # 判断所有单词都是首字母大写，像标题
    # print(str.isspace()) # 判断所有字符都是空白字符、\t、\n、\r

# 字符串大小寫轉換
    # str = "www.runoob.com"
    # print(str.upper())          # 把所有字符中的小写字母转换成大写字母
    # print(str.lower())          # 把所有字符中的大写字母转换成小写字母
    # print(str.capitalize())     # 把第一个字母转化为大写字母，其余小写
    # print(str.title())          # 把每个单词的第一个字母转化为大写，其余小写 

# 計算每個月天數
    # import calendar
    # monthRange = calendar.monthrange(2021,6) #年份, 月份
    # print(monthRange)  #(1,30)
    # 输出的是一个元组，第一个元素是所查月份的第一天对应的是星期几（0-6），
    # 第二个元素是这个月的天数。输出为 2021年6月份的第一天是星期四，该月总共有 30 天。

# 獲取昨天日期
    # import datetime
    # def getYesterday(): 
    #     today=datetime.date.today() 
    #     oneday=datetime.timedelta(days=1) 
    #     yesterday=today-oneday  
    #     return yesterday

    # print(getYesterday())

# 亂數與階層
    # #產生介於0~10的亂數
    # x = random.randrange(10) 
    # #20~40亂數
    # y = random.randrange(20,40)
    # #0~60亂數,  除了0以外只是6的倍數
    # z = random.randrange(0,60,6)
    # import math
    # # 5的階乘為:120
    # # 5!=5*4*3*2*1=120
    # x = math.factorial(5)

# 身分證檢查器
    # 公式:查代碼代入公式
    # 1+9x0+8x1+7x2+6x3+5x4+4x5+3x6+2x7+8+9
    # 加總的數之後除以10整除(餘數為0)的話是身分證正確
    # import numpy as np
    # idcheck= [10,11,12,13,14,15,16,17,34,18,19,20,21,22,35,23,24,25,26,27,28,29,32,30,31,33]
    # len(idcheck)
    # idcap = []
    # # np_idcheck = np.array(idcheck)
    # for index,item in enumerate(idcheck):
    #     print(item)
    #     print(chr(index + 65))
    #     idcap.append(chr(index + 65))

    # #代碼表
    # idcheck= [10,11,12,13,14,15,16,17,34,18,19,20,21,22,35,23,24,25,26,27,28,29,32,30,31,33]
    # TotalVal=0
    # idcode=""
    # while (len(idcode)!=10):
    #     idcode=input("輸入身分證號:")   #A123456789

    # print ("身分證:" + idcode)
    # CapVal = idcheck[ord(idcode[0])-65]         #查表
    # idcode11 = str (CapVal) + idcode[1:10] 
    # TotalVal = int(idcode11[0])     #10123456789

    # for index,item in enumerate(idcode11[1:10]):
    #     m = int(item) * (9 - index)
    #     TotalVal = TotalVal + m
        
    # TotalVal = TotalVal + int(idcode11[10])
    # print ("身分證是",end='')
    # if TotalVal % 10 == 0:
    #     print ("正確的")
    # else:
    #     print ("錯誤的")
#numpy 模組
    # import numpy as np
    # name = np.array(["張三","李四","石蓉","龍六"])
    # gender = np.array(["M","M","F","M"])
    # height = np.array([172,166,158,189])
    # weight = np.array([90,78,55,87])
    # scrore_math = np.array([45,74,88,61])
    # scrore_chinese = np.array([99,84,98,41])
    # scrore_english = np.array([66,84,68,31])
    # print ("班上男生的數學平均")
    # print (scrore_math[gender=="M"].mean())

# 樂透實際抽法49彩球
    # import random
    # import numpy as np
    # biglottery = np.array(range(1,50))
    # for item in biglottery:
    #     roll = int (random.random() * 49 )          #找1顆球
    #     roll2 = int (random.random() * 49  )        #找另1顆球
    #     temp = biglottery[roll]
    #     biglottery[roll] = biglottery[roll2]
    #     biglottery[roll2] = temp                    #滾動交換
    # print("大樂透號:")
    # print(biglottery[0:6])
    # print("特別號:")
    # print(biglottery[6])

# 约瑟夫生者死者小游戏
# 30 个人在一条船上，超载，需要 15 人下船。
# 于是人们排成一队，排队的位置即为他们的编号。
# 报数，从 1 开始，数到 9 的人下船。
# 如此循环，直到船上仅剩 15 人为止，问都有哪些编号的人下船了呢？
    # people={}
    # for x in range(1,31):
    #     people[x]=1
    # # print(people)
    # check=0
    # i=1
    # j=0
    # while i<=31:
    #     if i == 31:
    #         i=1
    #     elif j == 15:
    #         break
    #     else:
    #         if people[i] == 0:
    #             i+=1
    #             continue
    #         else:
    #             check+=1
    #             if check == 9:
    #                 people[i]=0
    #                 check = 0
    #                 print("{}号下船了".format(i))
    #                 j+=1
    #             else:
    #                 i+=1
    #                 continue


# 說明
# 一個簡單的賭博遊戲，遊戲規則如下：玩家擲兩個骰子，點數為1到6，如果第一次點數和為7或11，則玩家勝，
# 如果點數和為2、3或12，則玩家輸，如果和 為其它點數，則記錄第一次的點數和，然後繼續擲骰，
# 直至點數和等於第一次擲出的點數和，則玩家勝，如果在這之前擲出了點數和為7，則玩家輸。
    # from random import randint

    # class Status:
    #     LOST = 0
    #     WON = 1
    #     CONTINUE = 2
        
    # def initialRoll(firstPoint):
    #     return Status.WON if firstPoint in [7, 11] else \
    #     (Status.LOST if firstPoint in [2, 3, 12] else Status.CONTINUE)

    # def reRoll(firstPoint, point):
    #     return Status.WON if firstPoint == point else \
    #     (Status.LOST if 7 == point else Status.CONTINUE)

    # def dice():
    #     return randint(1, 6) + randint(1, 6)

    # firstPoint = dice()
    # print("玩家點數：[%d]" % firstPoint)
    # status = initialRoll(firstPoint)

    # while status == Status.CONTINUE:
    #     point = dice()
    #     print("玩家點數：%d" % point)
    #     status = reRoll(firstPoint, point)

    # print("玩家勝" if status == Status.WON else "玩家輸")
