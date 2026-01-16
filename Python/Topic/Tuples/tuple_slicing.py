# Tuple slicing operations
animals = ("cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow")

# Range of Index
print(animals[3:7])     #using positive indexes
print(animals[-7:-2])   #using negative indexes

# From given index till the end
print(animals[4:])      #using positive indexes
print(animals[-4:])     #using negative indexes

# From start to a given index
print(animals[:6])      #using positive indexes
print(animals[:-3])     #using negative indexes

# Every 3rd consecutive within given range
print(animals[::2])     #using positive indexes
print(animals[-8:-1:2]) #using negative indexes
