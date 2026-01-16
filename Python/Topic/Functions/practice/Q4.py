# WAF to find factorial of n.

def cal_fact(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    print(fact)
cal_fact(5)
