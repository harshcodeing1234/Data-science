# WAF to find greatest of three

def check_greatest(a,b,c):
    if a>b and a>c:
        print("A is greatest")
    elif b>a and b>c:
        print("B is greatest")
    elif a ==b and a ==c:
        print("All are equal")
    else:
        print("C is greatest")
check_greatest(12,13,56)
check_greatest(1234523456345665,234567876543,3456789876543)
