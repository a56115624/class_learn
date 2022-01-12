#  類別 class,物件object
class phone:
    def __init__(self,os,number,is_waterproof):
        self.os= os
        self.number = number
        self.is_waterproof = is_waterproof

# phone1 就是我們的物件
phone1 = phone("ios",123,True)
phone2 = phone("andriod",456,False)
print(phone1.os)
print(phone1.number)
print(phone2.number)

