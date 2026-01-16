# create a square of a number using multiprocessing
import multiprocessing
import time

def square(n):
    print(f"Square of {n} is {n*n}")
    time.sleep(2)

def main():
    numbers = [2,4,6,9,34,2,67]

    # create process for each number
    processes = []

    for num in numbers:
        p = multiprocessing.Process(target=square, args=(num,))
        processes.append(p)
        p.start()
    
    # Wait for all process to finished
    for p in processes:
        p.join()
    
    print("Done")

if __name__ == "__main__":
    main()