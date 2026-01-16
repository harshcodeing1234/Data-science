# WAF to find fabonacchi sequence
def fabonacchi(n):
    i = 0
    a =0
    b = 1  
    while i < n:
        print(a)
        a,b = b,a+b
        i = i+1
fabonacchi(10)
