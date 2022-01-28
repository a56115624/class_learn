def add(n1,n2,cd):
    cd(n1+n2)

def handle1(result):
    print("結果是",result)

def handle2(result):
    print("Result of add is",result)

add(3,4,handle1)
add(3,5,handle2)



# def test(arg):
#     arg(1000) # 呼叫回呼函式

# # 定義一個回呼函式
# def handle(da):
#     print(da)

# test(handle)
