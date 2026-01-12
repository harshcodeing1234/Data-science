# 1. Write a Python program using multiprocessing to create two processes that print
# their process IDs. 
import multiprocessing
import os

def print_pid():
    print('Process Id',os.getpid())

if __name__ == "__main__":
    p1 = multiprocessing.Process(target=print_pid)
    p2 = multiprocessing.Process(target=print_pid)

    p1.start()
    p2.start()

    p1.join()
    p2.join()
