PROCESSES AND THREADS
```txt
  Process: Program in execution
  Threads: Lightweight, Faster, Share resources, Single unit of execution
    Threads share: Code section, Data section, Heap memory
    Threads have their own: Stack, Registers, Program counter
  
  Processes communicate through IPC (Pipes, message queues, sockets)
  Threads communicate through shared memory
  
  Processes: Slower context switching
  Threads: Faster context switching
  
  Thread-safe code: uses synchronization (mutexes, semaphores, atomic operations)
  
  User level threads: managed by applications, if one blocked then all blocked
  Kernel level threads: managed by OS, if one blocked then others not blocked
```


Here are the equivalent Python implementations:

1. Thread Creation and Basic Synchronization:
```python
import threading
import queue
import time

# Mutex example
mutex = threading.Lock()

def critical_section():
    with mutex:  # equivalent to mutex.acquire() and mutex.release()
        # Critical section code
        print(f"Thread {threading.current_thread().name} in critical section")
        time.sleep(1)

# Create and start threads
threads = [threading.Thread(target=critical_section) for _ in range(3)]
for t in threads:
    t.start()
for t in threads:
    t.join()
```

2. Semaphore Usage:
```python
import threading
from threading import Semaphore

# Binary semaphore
semaphore = Semaphore(1)

def semaphore_example():
    with semaphore:
        print(f"Thread {threading.current_thread().name} acquired semaphore")
        time.sleep(1)
```

3. Condition Variable:
```python
condition = threading.Condition()
data_ready = False

def producer():
    global data_ready
    with condition:
        data_ready = True
        condition.notify()

def consumer():
    with condition:
        while not data_ready:
            condition.wait()
        print("Data consumed")
```

4. Thread Pool:
```python
from concurrent.futures import ThreadPoolExecutor

def task(n):
    return n * n

with ThreadPoolExecutor(max_workers=3) as executor:
    results = executor.map(task, range(5))
```

5. Race Condition Example:
```python
counter = 0

def increment_counter():
    global counter
    current = counter
    time.sleep(0.1)  # Simulate processing
    counter = current + 1

# Create threads that will cause race condition
threads = [threading.Thread(target=increment_counter) for _ in range(5)]
```

6. Thread-Safe Singleton:
```python
class Singleton:
    _instance = None
    _lock = threading.Lock()
    
    @classmethod
    def get_instance(cls):
        if not cls._instance:
            with cls._lock:
                if not cls._instance:
                    cls._instance = cls()
        return cls._instance
```

7. Process Communication using Pipes:
```python
from multiprocessing import Process, Pipe

def sender(conn):
    conn.send(['hello'])
    conn.close()

def receiver(conn):
    print(conn.recv())
    conn.close()

parent_conn, child_conn = Pipe()
p1 = Process(target=sender, args=(child_conn,))
p2 = Process(target=receiver, args=(parent_conn,))
```

8. Queue for Thread Communication:
```python
from queue import Queue

def producer(queue):
    for i in range(5):
        queue.put(i)
        time.sleep(1)

def consumer(queue):
    while True:
        item = queue.get()
        if item is None:
            break
        print(f"Consumed {item}")
        queue.task_done()

q = Queue()
prod = threading.Thread(target=producer, args=(q,))
cons = threading.Thread(target=consumer, args=(q,))
```

9. Process Pool:
```python
from multiprocessing import Pool

def process_task(x):
    return x * x

if __name__ == '__main__':
    with Pool(processes=4) as pool:
        results = pool.map(process_task, range(10))
```

These implementations demonstrate core concepts of threading and multiprocessing in Python, following Python's "with" context managers for clean resource handling and GIL considerations.
