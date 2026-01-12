# 9. Create a multiprocessing program that demonstrates inter-process
# communication using a Queue. 

import multiprocessing

def sender(q):
    q.put('Hello from sender')

def reciver(q):
   message = q.get()
   print(f"Message: {message}")

if __name__ == '__main__':
    q = multiprocessing.Queue()

    p1 = multiprocessing.Process(target=sender,args=(q,))
    p2 = multiprocessing.Process(target=reciver,args=(q,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()


