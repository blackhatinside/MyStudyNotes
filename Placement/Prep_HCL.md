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

Deadlock occurs when two or more threads/processes are waiting indefinitely for resources held by each other.
Conditions for Deadlock:
  Mutual Exclusion: Resources can't be shared
  Hold and Wait: Process holds resources while waiting for others
  No Preemption: Resources can't be forcibly taken
  Circular Wait: Circular chain of processes waiting for resources
```

```
1NF (First Normal Form):

Single value in each cell
Unique column names
Each row uniquely identifiable by primary key

2NF (Second Normal Form):

Must be in 1NF
No partial dependencies (non-key attributes must depend on entire primary key)

3NF (Third Normal Form):

Must be in 2NF
No transitive dependencies (non-key attributes cannot depend on other non-key attributes)
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

```cpp
#include<bits/stdc++.h>
using namespace std;

// struct Car {
// 	string model;
// 	int price;
// } bmw;


/*
	Car* Chevrolet = new Car;
	(*Chevrolet).model = "spark";
	(*Chevrolet).price = 800000;
	cout << Chevrolet->model << endl;
	cout << Chevrolet->price << endl;
*/

class Car {
public:					// by default class vars funcs are pvt.
	string model;
	int price;
} bmw;

/*
	Car* Chevrolet = new Car;
	(*(Chevrolet)).model = "spark";
	(*(Chevrolet)).price = 800000;
	cout << Chevrolet->model << endl;
	cout << Chevrolet->price << endl;
*/

// C++ Templates
template <class T1, class T2>
class Calculator {
public:
	T1 x, y;
	Calculator(T1 a, T2 b) {
		x = a;
		y = b;
	}
	T1 add() {
		return x + y;
	}
	T2 mul(T1 a, T2 b) {
		return a * b;
	}
};

/*
	Calculator <int, int> calc(2, 4);
	cout << calc.add() << endl;
	cout << calc.mul(3, 5) << endl;
*/

// Base Class
class Animal {
public:
	int age;

	// constructor
	Animal() {
		age = 0;
		cout << "Animal Object created..." << endl;
	}

	void eat() {
		cout << "Eating..." << endl;
	}

	virtual void speak() {
		cout << "Speaking..." << endl;
	}	// virtual keyword enables overriding for the method

	// setter functions
	void setAge(int animalAge) {
		age = animalAge;
	}	// const keyword promises that the method wont modify object state

	// getter functions
	int getAge() const {
		cout << "Called Animal::getAge()" << endl;
		return age;
	}

	// destructor
	virtual ~Animal() {
		cout << "ANIMAL killed!" << endl;
	}
};

class Human : public Animal {
// private:
	string name;

public:
	// Overriding
	void speak() override {
		cout << "Talking..." << endl;
	}	// override keyword optional

	// Polymorphism
	void speak(string greeting) {
		cout << "Talking... " + greeting << endl;
	}

	// setter function
	void setName(string humanName) {
		name = humanName;
	}

	// getter function
	string getName() {
		return name;
	}
};

class Cat: protected Animal {
public:
	// Overriding
	void speak() override {
		cout << "Meowing..." << endl;
	}

	// setter function
	void set_catAge(int catAge) {
		setAge(catAge);
	}

	// getter function
	int get_catAge() {
		cout << "Called Cat::getAge()" << endl;
		return getAge();
	}

	~Cat() {
		cout << "CAT killed!" << endl;
	}
};

// private inheritance by default
class Dog : Animal {
public:
	Dog() {
		age = 5;
	}

	// Overriding
	void speak() override {
		cout << "Barking..." << endl;
	}

	// Overriding getter function
	int getAge() {
		cout << "Called Dog::getAge()" << endl;
		return age;
	}
};

class Dummy2 {
public:
	int dummyint = 5;
	~Dummy2() {
		cout << "DUMMY2 killed!" << endl;
	}
};

class Puppy : public Dog {
public:
	int get_puppyAge() {
		cout << "Called Puppy::getAge()" << endl;
		return getAge();
	}
};

class Dummy {
public:
	int dummyint = 5;
	~Dummy() {
		cout << "DUMMY killed!" << endl;
	}
};

int main() {

	Dummy d1;
	Human h;
	Dummy2 d2;
	h.setName("Adithya");
	h.setAge(24);
	cout << h.getName() << endl;
	cout << h.getAge() << endl;
	h.eat();
	h.speak();
	h.speak("Hello");
	// cout << h.name << endl;

	cout << endl;

	Cat c;
	// c.age = 5;	// cant access protected members
	// c.eat();		// cant access protected members
	// cout << c.getAge() << endl;		// cant access protected members
	c.speak();
	c.set_catAge(2);
	cout << c.get_catAge() << endl;

	cout << endl;

	Dog d;
	// d.age = 5;		// cant access private members
	// cout << d.setAge(5) << endl;	// cant access private members
	d.speak();
	cout << d.getAge() << endl;

	cout << endl;

	Puppy p;
	// p.age = 1;		// cant access private members
	cout << p.get_puppyAge() << endl;
}

/*

Classes and Objects: Instances, Data + Methods
Encapsulation: access specifiers
Abstraction: abstract classes
Polymorphism: multiple functions with same name but different parameters

Public:
	accessible from anywhere
Protected:
	accessible within class and derived class
	used to provide access to derived classes, but hidden from external code
Private:
	accessible within class only

Public Inheritance:
	Public members -> Public members
	Protected members -> Protected members
	Private members NOT ACCESSIBLE

Protected Inheritance:
	Public members -> Protected members
	Protected members -> Protected members
	Private members NOT ACCESSIBLE

Private Inheritance:
	Public members -> Private members
	Protected members -> Private members
	Private members NOT ACCESSIBLE

*/
```
