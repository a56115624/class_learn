# class Point:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
#     def show(self):
#         print(self.x,self.y)
# p=Point(1,5) #建立實體物件
# p.show() #呼叫實體方法

# Point 實體物件的設計: 平面座標上的點
class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    # 定義實體方法
    def show(self):
        print(self.x, self.y)
    def distance(self, targetx, targety):
        return (((self.x-targetx)**2)+(self.y-targety)**2)**0.5
p=Point(3,4)
p.show()  # 呼叫實體方法/函式
result = p.distance(0,0) #計算座標 3,4 和座標0,0之間的距離 
print(result)
#File


