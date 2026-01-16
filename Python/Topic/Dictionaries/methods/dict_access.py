# Dictionary access methods
student_info = {
    'Name':'Harsh Kumar',
    'COllege':'AIIT',
    'Roll_no':'A45349524003',
    '1sem. marks':'8.33 SGPA',
    'Overall performance':'Good'
}

# access key 
print(student_info['Name'])
print(student_info.get('Name'))

# Access all keys
for key, value in student_info.items():
  print(f"The value corresponding to the key {key} is {value}")
