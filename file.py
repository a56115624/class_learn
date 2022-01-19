# 儲存檔案
# file = open("date.txt",mode = "w",encoding="utf_8") # 開啟
# file.write("Hello File \nSecond line \n我來玩看看") #操作
# file.close # 關閉

# with open("data.txt",mode="w",encoding="utf-8") as file:
#     file.write("Hello File \nSecond line \n我來玩看看")

# 讀取檔案
# 把檔案中的數字資料,一行一行讀取出來,計算它的總和
# sum = 0
# with open("data.txt",mode="r",encoding="utf-8") as file:
#     # 全部一起讀取 data = file.read()
#     for i in file: # 一行一行的讀取
#         sum = sum+int(i)
# print(sum)


# 使用 json 格式讀取 複寫檔案
import json
# 從檔案中讀取json資料,放入變數data裡面
with open("config.json", mode="r") as file:
    data = json.load(file)
# print(data)
# print("name",data["name"])
# print("version",data["version"])
data["name"] = "New Name" # 修改變數中的資料

#把最新的資料寫入檔案中
with open("config.json", mode="w") as file:
    json.dump(data,file)
