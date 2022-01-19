#定義一個可以做 除法的函式
# def divide(n1,n2):
#     result = n1/n2
#     print(result)
# divide(2,4) #印出 0.5
# divide(n2=2,n1=4) # 印出 2

# 函式接受無限參數 msgs
# def say(*msgs):
#     # 以 Tuple的方式處理
#     for msg in msgs:
#         print(msg)
# # 呼叫函式,傳入三個參數資料
# say("Hello","Arbitrary","Arguments")

# # 參數的預設資料
# def power(base,exp):
#     print(base**exp)  # **為次方
# power(3,2)
# power(4)

# # 參數的名稱對應
# def divide(n1,n2):
#     print(n1/n2)
# divide(2,4)
# divide(n2=2,n1=4)

# 無限/不定 參數資料
# 計算出  avg數值裡面的平均數
def avg(*num):
    sum = 0 
    for n in num:
        sum = sum+n
    print(sum/len(num))

avg(3,4)
avg(3,5,10)
avg(1,4,-1,8)