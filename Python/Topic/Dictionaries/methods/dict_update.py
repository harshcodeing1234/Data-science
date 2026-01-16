# Dictionary update() method
student_info = {
    'Name':'Harsh Kumar',
    'COllege':'AIIT',
    'Roll_no':'A45349524003',
    '1sem. marks':'8.33 SGPA',
    'Overall performance':'Good',
}

student_info.update({'COllege':'Amity university'})
print(student_info)

# Example 2
info = {
    'name':'Harsh kumar',
    'age':18
}

info2 = {
    'Address':'patna,bihar',
}

info.update(info2)
print(info)
