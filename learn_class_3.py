#FullName 實體物件的設計: 分開紀錄姓, 名資料的全名
class FullName:
    def __init__(self,frist,last):
        self.first = frist
        self.last = last
name1=FullName("C W","Peng")
print(name1.first,name1.last)
name2 = FullName("H S","shane")
print(name2.first,name2.last)