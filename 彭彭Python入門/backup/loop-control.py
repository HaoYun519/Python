# break
# n=0
# while n<5:
#     if n == 3:
#         break
#     print(n)
#     n += 1
# print("最後的 n:", n)

# continue
# n=0
# for x in [0,1,2,3]:
#     if x%2 == 0:
#         continue
#     print(x)
#     n += 1
# print("最後的 n:", n)

#else 
# sum = 0
# for n in range(11):
#     sum += n
# else:
#     print(sum) # 印出跑完迴圈後的結果

#綜合範例: 找出平方根
n = int(input("請輸入一數字: "))
for i in range(n): # i 從 0 ~ n-1
    if i*i ==n:
        print("整數平方根", i) 
        break # 強制結束迴圈時,不會執行 else 區塊
else:
    print("沒有整數平方根")