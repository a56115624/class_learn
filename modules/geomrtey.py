# 在 geometry 模組中定義幾何運算功能
# 計算兩點的距離
def distance(x1,y1,x2,y2):
    return ((x1-x2)**2+(y2-y1)**2)**0.5
# 計算線的斜率
def slop(x1,y1,x2,y2):
    return(y2-y1)/(x2-x1)    