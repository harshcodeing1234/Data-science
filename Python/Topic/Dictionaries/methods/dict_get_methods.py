# Dictionary get(), keys(), values(), items() methods
student_info = {
    'Name':'Harsh Kumar',
    'COllege':'AIIT',
    'Roll_no':'A45349524003',
    '1sem. marks':'8.33 SGPA',
    'Overall performance':'Good',
}

# get()
print(student_info.get('Name'))

# keys()
print(student_info.keys()) # return all keys

# value()
print(student_info.values()) # return all values

# items 
print(student_info.items()) # return value in [(key:value)]
