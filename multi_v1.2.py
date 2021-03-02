from multiprocessing import Process, Value, Array, Lock, Queue, Pool
import os
import time

def cube(number):
    return number*number*number


if __name__ == "__main__":
    # main program oldugunu belirtiyor
    numbers = range(10)
    print(numbers)
    pool = Pool()

    result =  pool.map(cube, numbers)


    pool.close()
    pool.join()
    print(result)
