# 算术运算符
a = 5
b = 3
print("算术运算符:")
print("a + b =", a + b)  # 输出: 8
print("a - b =", a - b)  # 输出: 2
print("a * b =", a * b)  # 输出: 15
print("a / b =", a / b)  # 输出: 1.6666666666666667
print("a // b =", a // b)  # 输出: 1
print("a % b =", a % b)  # 输出: 2
print("a ** b =", a ** b)  # 输出: 125

# 比较运算符
x = 10
y = 20
print("\n比较运算符:")
print("x == y:", x == y)  # 输出: False
print("x != y:", x != y)  # 输出: True
print("x > y:", x > y)  # 输出: False
print("x < y:", x < y)  # 输出: True
print("x >= y:", x >= y)  # 输出: False
print("x <= y:", x <= y)  # 输出: True

# 赋值运算符
z = 5
print("\n赋值运算符:")
z += 3  # 等同于 z = z + 3
print("z += 3:", z)  # 输出: 8
z -= 2  # 等同于 z = z - 2
print("z -= 2:", z)  # 输出: 6
z *= 2  # 等同于 z = z * 2
print("z *= 2:", z)  # 输出: 12
z /= 3  # 等同于 z = z / 3
print("z /= 3:", z)  # 输出: 4.0
z //= 2  # 等同于 z = z // 2
print("z //= 2:", z)  # 输出: 2.0
z %= 2  # 等同于 z = z % 2
print("z %= 2:", z)  # 输出: 0.0
z **= 3  # 等同于 z = z ** 3
print("z **= 3:", z)  # 输出: 0.0

# 逻辑运算符
p = True
q = False
print("\n逻辑运算符:")
print("p and q:", p and q)  # 输出: False
print("p or q:", p or q)  # 输出: True
print("not p:", not p)  # 输出: False

# 位运算符
m = 60  # 二进制: 00111100
n = 13  # 二进制: 00001101
print("\n位运算符:")
print("m & n:", m & n)  # 输出: 12 (二进制: 00001100)
print("m | n:", m | n)  # 输出: 61 (二进制: 00111101)
print("m ^ n:", m ^ n)  # 输出: 49 (二进制: 00110001)
print("~m:", ~m)  # 输出: -61 (二进制: 11000011)
print("m << 2:", m << 2)  # 输出: 240 (二进制: 11110000)
print("m >> 2:", m >> 2)  # 输出: 15 (二进制: 00001111)

# 成员运算符
list_example = [1, 2, 3, 4, 5]
print("\n成员运算符:")
print("3 in list_example:", 3 in list_example)  # 输出: True
print("6 not in list_example:", 6 not in list_example)  # 输出: True

# 身份运算符
a1 = [1, 2, 3]
a2 = a1
a3 = [1, 2, 3]
print("\n身份运算符:")
print("a1 is a2:", a1 is a2)  # 输出: True
print("a1 is a3:", a1 is a3)  # 输出: False
print("a1 is not a3:", a1 is not a3)  # 输出: True