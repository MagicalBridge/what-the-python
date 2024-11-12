"""
演示 py 的 input 语句
"""
print("请告诉我你是谁？")

name = input()

print("我知道你你是 %s" % name)


# input 默认接收的类型是字符串类型，如果想要数字，需要手动转换一下：
num = input("bank card password:")
# 数据类型转换
num = int(num)

print("银行卡密码:", type(num))
