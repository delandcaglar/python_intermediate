from threading import Thread, Lock, current_thread
from multiprocessing import Process
import os
import time
from queue import Queue


def worker(q, lock):
    while True:
        value = q.get()
        # processing..
        with lock:
            print(f'in {current_thread().name} got {value}')
        q.task_done()


if __name__ == "__main__":
    q = Queue()
    lock = Lock()
    num_threads = 10

    for i in range(num_threads):
        thread = Thread(target= worker, args=(q,lock))
        thread.daemon = True
        # while loop bitmez daemon threadi False yaparsan defaultu false
        thread.start()

    for i in range(0,21):
        q.put(i)

    q.join()

    print('end main')












# database_value = 0
#
# def increase(lock):
#     global database_value
#     # lock.acquire()
#     with lock:
#         local_copy = database_value
#
#         local_copy += 1
#         time.sleep(0.1)
#         database_value = local_copy
#     # with lock ayni sey
#     # lock.release()
#
# if __name__ == "__main__":
#     lock = Lock()
#     print('start value', database_value)
#     thread1 = Thread(target=increase, args=(lock,))
#     thread2 = Thread(target=increase, args=(lock,))
#
#     thread1.start()
#     thread2.start()
#
#     thread1.join ()
#     thread2.join ()
#
#     print('end value' , database_value)


# def square_numbers():
#     for i in range(100):
#         a = i * i
#         print(a)
#         time.sleep(0.1)
#
#
# threads = []
# num_threads = 10
#
# # Create processes.
# for i in range( num_threads ):
#     t = Thread( target=square_numbers )
#     threads.append( t )
#     print("1")
#
# # Start.
# for t in threads:
#     t.start()
#
# # Join.
# for t in threads:
#     t.join()
#
# print("end main")