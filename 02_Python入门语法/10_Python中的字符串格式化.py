"""
基本语法：formatted_string = "格式化字符串" % (值1, 值2, ...)

格式化符号：
% 运算符支持多种格式化符号，用于指定不同类型的数据：
    - %s：字符串
    - %d：十进制整数
    - %f：浮点数
    - %x：十六进制整数
    - %o：八进制整数
    - %e：科学计数法表示的浮点数
    - %g：根据值的大小自动选择 %f 或 %e
"""

# 1、格式化字符串
name = "Alice"
formatted_string = "我的名字是 %s。" % name
print(formatted_string)

# 2、格式化整数
age = 30
formatted_string = "我今年 %d 岁。" % age
print(formatted_string)

# 3、格式化浮点数
height = 1.68
formatted_string = "我的身高是 %.2f 米。" % height
print(formatted_string)

# 4、格式化多个值
name = "Alice"
age = 30
height = 1.68
formatted_string = "我的名字是 %s，我今年 %d 岁，我的身高是 %.2f 米。" % (name, age, height)
print(formatted_string)
