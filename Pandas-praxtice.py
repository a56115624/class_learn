# 載入 pandas
import pandas as pd
# 建立 Series
data = pd.Series([20,10,15])

# 基本 Series操作
# print(data)
# print("max",data.max())
# print("median",data.median())
# data = data*2
# print(data)
# data = data ==20
# print(data)
# 建立 DataFrame
data = pd.DataFrame({
    "name":["Amy","Jhon","Bob"],
    "salary":[30000,50000,40000]
})
# print(data)
# 基本 DataFrame 操作
# 取得特定的欄位
# print(data["name"])
# 取得特定的列
print(data)
print("===========")
print(data.iloc[0])