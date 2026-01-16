# Avoid space in string length
str = "   hello    "
print(len(str))
print(str.strip())
print(len(str.strip()))

# 2nd method
s = "    hello   "
res = len(s.replace(" ", ""))
print(res)
