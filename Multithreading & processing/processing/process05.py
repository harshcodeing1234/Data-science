# 2. Create a program using a process pool to perform a CPU-intensive task and
# display the process ID for each task. 

import concurrent.futures
import math

numbers = [5, 7, 10, 12]

def factorial(n):
    result = math.factorial(n)
    print(f"Factorial of {n} is {result}")
    return result
if __name__ == '__main__':
    # Using ProcessPoolExecutor
    with concurrent.futures.ProcessPoolExecutor() as executor:
        executor.map(factorial, numbers)
