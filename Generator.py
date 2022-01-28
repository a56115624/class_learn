# 定義建立生成器函式
# def test():
#     print("階段一")
#     yield 5
#     print("階段二")
#     yield 10
# # 呼叫並回傳生成器
# gen = test()
# # 搭配for迴圈中使用
# for data in gen :
#     print(data)

# 無窮偶數相加
# def generateEven():
#     number = 0
#     while True:
#         yield number
#         number = number+2
# evengenerator = generateEven()
# for dx in evengenerator:
#     print(dx)

# 最大加到10
def generateEven(maxnumber):
    number = 0
    while number<=maxnumber:
        yield number
        number = number+2
        
evengenerator = generateEven(10)
for dx in evengenerator:
    print(dx)