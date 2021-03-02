from multiprocessing import Process, Value, Array, Lock, Queue, Pool
import os
import time


def add_100(numbers,lock):
    for i in range(100):
        time.sleep(0.01)
        # lock.acquire()
        for i in range(len(numbers)):
            with lock:
                numbers[i] += 1

        # with lock:
        #     numbers.value += 1
        # lock.release()

def square(numbers, queue):
    for i in numbers:
        queue.put(i*i)

def make_negative(numbers, queue):
    for i in numbers:
        queue.put(-1*i)


if __name__ == "__main__":
    # main program oldugunu belirtiyor
    numbers = range(1,6)
    q = Queue()
    p1 = Process(target=square, args=(numbers,q))
    p2 = Process(target=make_negative, args=(numbers,q))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    while not q.empty():
        print(q.get())