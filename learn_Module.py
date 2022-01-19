# 載入內建的sys模組並取得資訊
# import sys 
# print(sys.platform)
# print(sys.maxsize)


# 建立 geomrtey 模組,載入使用
import modules.geomrtey as geo
result = geo.distance(1,2,5,5)
print(result)
result = geo.slop(1,1,2,2)
print(result)


# 調整搜索模組的路徑
import sys
sys.path.append("modules") #在模組的搜索路徑列表中[新增路徑]