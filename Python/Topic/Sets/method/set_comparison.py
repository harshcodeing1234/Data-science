# Set comparison methods
s1 = {12,14,16,10,78,90}
s2 = {12,45,90,78,43}

# isdisjoint()
print(s1.isdisjoint(s2))

# issuperset()
s2 = {12,90,78,}
print(s1.issuperset(s2))

# issubset()
s2 = {12,90,78,10}
print(s2.issubset(s1))
