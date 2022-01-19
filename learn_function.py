# 定義函示
# def multiply():
#     print(3*4)
# # 呼叫函示
# multiply()


# 定義函示
# def multiply(num1,num2):
#     print(num1*num2)
#     return num1*num2
# # # 呼叫函示
# value = multiply(5,6)
# print (value)


# # 定義函示
# def multiply(num1,num2):
#     return num1*num2
# # # 呼叫函示
# value = multiply(5,6)+multiply(10,5)
# print (value)

#函示可以用來做程式的包裝: 同樣的邏輯可以重複利用

# 1+到  max 代表可以加到任意數
def calculate(max):
    sum = 0
    for i  in range(1,max):
        sum = sum+i
    print(sum)

calculate(40)
