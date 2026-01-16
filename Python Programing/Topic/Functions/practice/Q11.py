# WAF to takes list and returns sum of its element.

num=input("Enter list number by space:")
num = list(map(int, num.split()))
def list_add(list):
    sum = 0
    for i in range(len(list)):
        sum = sum + list[i] 
    print(f"sum of list is:{sum}")
list_add(num)
