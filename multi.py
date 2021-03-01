from multiprocessing import Process
import os
import time




def square_numbers():
    for i in range(100):
        a = i * i
        print(a)
        time.sleep(0.1)


if __name__ == "__main__":
    processes = []
    num_processes = os.cpu_count()

    # Create processes.
    for i in range(num_processes):
        process = Process( target=square_numbers )
        processes.append( process )
        print("1")

    # Start.
    for process in processes:
        process.start()

    # Join.
    for process in processes:
        process.join()

    print("end main")