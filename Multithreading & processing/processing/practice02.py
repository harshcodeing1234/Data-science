# 7. Create a multiprocessing program where one process calculates the sum of
# numbers from 1 to 100 and another process calculates the factorial of a given
# number. 
import multiprocessing
import math

def calculate_sum():
    sum = 1
    for i in range(1,101):
        sum = sum+i
    print(f'Sum of given num is: {sum}')

def calculate_factorial(n):
    print(f'Factorial of {n} is: {math.factorial(n)}')


if __name__=='__main__':
    p1 = multiprocessing.Process(target=calculate_sum)
    p2 = multiprocessing.Process(target=calculate_factorial,args=(4,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

