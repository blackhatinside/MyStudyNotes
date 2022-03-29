try:
    import time
    import threading
except Exception as err:
    print("Import Error : ", err)
    pass

lock = threading.Lock()     # lock is implemented using a semphore object provided by OS
def three(arr, lock):
    lock.acquire()  # prevents access of the code to other threads
    for x in arr:
        if x % 3 == 0:
            print(x)
        # time.sleep(0.1)
    lock.release()


def main():
    start = time.perf_counter()
    t1 = threading.Thread(target = three, args = (range(1, 100), lock)) # Thread(target_function, parameters_tuple)
    t2 = threading.Thread(target = three, args = (range(101, 200), lock))   
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    three(range(201, 300), lock)    # join() will wait for previous threads to finish before going to main thread
    stop = time.perf_counter()
    print(stop - start)
    return

if __name__ == '__main__':
    try:
        main()
        stop = time.time()
        print("Seconds used: ", stop - start)
    except Exception as err:
        print("Program crashed: ", err)
        pass
