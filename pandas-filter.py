import pandas as pd
#塞選練習-Series
# data = pd.Series([30,15,20])
# condition= data>18
# print(condition)
# filteredData = data[condition]
# print(filteredData)

# data = pd.Series(["你好","Python","Pandas"])
# condition = data.str.contains("P")
# print(condition)
# filtereData = data[condition]
# print(filtereData)

# 塞選練習
data = pd.DataFrame({
    "name":["Amy","Bob","Charles"],
    "salary":[30000,50000,40000]
})
print(data)
condition = data["name"]=="Amy"
print(condition)
filteredData = data[condition]
print(filteredData)