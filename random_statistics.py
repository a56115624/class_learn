# uniform 機率相同
# 隨機模組
import random
# 隨機選取
# data = random.choice([1,5,6,10,20])
# print(data)
# data = random.sample([1,5,6,10,20],3)
# print(data)
# 隨機調換順序
# data = [1,5,8,20]
# random.shuffle(data)
# print(data)


# 隨機取得亂數
# data = random.random() # 0~1之間的隨機亂數
# print(data)

# 取得常態分配亂數
# 平均數 100 標準差 10 的到的資料多在90~100之間
# data = random.normalvariate(100,10)
# print(data)

# 統計模組
import statistics as stat
# 平均數
# data = stat.mean([1,4,5,8])
# print(data)
#中位數
# data = stat.median([1,4,5,8,20])
# print(data)
# 標準差
data = stat.stdev([1,4,5,8,20])
print(data)
