# 使用 + 云算符, 这是最简单和最常用的字符串拼接方法。
name = "Alice"
age = 30
message = "My name is " + name + " and I am " + str(age) + " years old."
print(message)

# 使用join() 方法 ，join() 方法用于将一个可迭代对象（如列表、元组）中的字符串连接成一个单一的字符串。
words = ["Hello", "world", "!"]
message = " ".join(words)
print(message)
