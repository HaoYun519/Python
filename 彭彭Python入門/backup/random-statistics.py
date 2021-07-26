# 隨機模組
import random
# data=random.choice([1,5,6,10,20])   # 隨機一筆
# data=random.sample([1,5,6,10,20],3) # 隨機三筆

# 隨機調換順序
# data=[1,5,8,20]
# random.shuffle(data) 

# 隨機取得亂數
# data=random.random() # 0.0 ~ 1.0 之間的隨機亂數
# data=random.uniform(60, 100) # 60 ~ 100 之間的隨機亂數 

# 取得常態分配亂數
# 平均數 100, 標準差 10, 得到的資料【多數】在 90~110 之間
# data=random.normalvariate(100, 10)
# 平均數 0, 標準差 5, 得到的資料【多數】在 90~110 之間
# data=random.normalvariate(0, 5)
# print(data)

# 統計模組
# import statistics as stat
# data=stat.mean([1,4,5,8]) # 平均數
# data=stat.median([1,2,3,4,5,8,100]) # 中位數
# data=stat.stdev([1,2,3,4,5,8,10])  # 標準差
# print(data)