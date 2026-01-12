# 8. Write a program using multiprocessing to find prime numbers in a given range. 
import multiprocessing

def find_primes(start, end):
    for num in range(start, end + 1):
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                print("Prime:", num)

if __name__ == "__main__":
    p1 = multiprocessing.Process(target=find_primes, args=(1, 50))
    p2 = multiprocessing.Process(target=find_primes, args=(51, 100))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
