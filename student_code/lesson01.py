a = 1.0
print(type(a))
type1 = type(a)
print(type1)

str_demo = "Hello AndersonHJB.777282881.1.1.1.*()"
print(str_demo)
print(type(str_demo))

lst = [1, 2, 3, "aiyc", 1.1]
print(lst)
print(type(lst))

tup = (1, 2, 1.1, "aiyc")
"""
1. 不可变
2. 有序
3. 任意数据类型
"""

# d = {key1:vaulue1, key2:value2, key....}
dict1 = {"name": "AndersonHJB", "age": 18}
print(dict1)
"""
1. 无序性
2. key：不可变的数据类型
3. value:任意数据类型
"""

set1 = {1, 2, 3, (1, 2, 3), "string"}
"""
1. 确定性：
2. 互异性：
3. 无序性：
"""
print(set1)

num = 25
gewei = num % 10
shiwei = num // 10
result = shiwei + gewei
print(result)

a = 1
a = a + 10  # a += 10
# I am lilei # I'm lilei
