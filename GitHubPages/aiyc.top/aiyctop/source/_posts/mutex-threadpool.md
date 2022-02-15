---
title: Mutex/Threadpool
tags: []
id: '1999'
categories:
  - - Alex Homework
date: 2021-10-23 09:42:13
---

There is a concept called a "lock" in multithreading. A lock is basically just an extra step of code that you will add to a multi-threaded program to prevent each thread from sharing resources, since this makes the program take longer to solve, as each item will be running constantly, thus lowering the efficiency of running each part of a script. For example, this is a code that does not use locks:

```python
import threading, time

count = 0

class MyThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        global count
        temp = count + 1
        time.sleep(0.001)
        count = temp
threads = []
for  _  in  range ( 1000 ) :
    thread = MyThread()
    thread.start()
    threads.append(thread)
for thread in threads:
    thread.join()
# print(len(threads))
print(f'Final count: {count}')
```

In the code above, you will see that the output is "Threads: 69", or something that is not 1000, as we wanted to achieve in the for loop that looped through the creation of threads. This is because multi-threads share resources, thus not needing 1000 threads to be created, however this slows down the execution process drastically. Here is a code that uses lock control:

```python
import threading
import  time

lock  =  threading . Lock ( ) # Create a simple read-write lock 
number = 0

def addNumber():
    global number
    for  i  in  range ( 1000000 ) :
        lock . acquire ( ) # Get first 
        number += 1
        # The process in the middle forced him to have this calculation and assignment process, that is, let him perform these two operations, and then switch.
        # In this way, the calculation will not be completed, and the assignment will go to the next one before it comes.
        # This prevents thread insecurity
        lock . release ( ) # Release again 

def downNumber():
    global number
    for  i  in  range ( 1000000 ) :
        lock.acquire()
        number -= 1
        lock.release()

print ( "start" ) # print a start 
thread  =  threading . Thread ( target  =  addNumber ) #Open a thread (declaration) 
thread2  =  threading . Thread ( target  =  downNumber ) # Start the second thread (declaration) 
thread . start ( ) # start 
Thread2 . Start ( ) # start 
thread.join()
thread2.join()
# join is blocked here, until we have to block the thread execution will be executed downward
print("外", number)
print("stop")

# Output
start
Outside  0
stop
```

The code above is more efficient than the previous code, because it controls the process of handing down the lock to another thread to run, and the thread will only execute if the previous thread that was running hands the lock to the next thread to run. This code is more efficient than the previous one, because instead of sharing resources with other threads, it runs one by one, causing the program to run each part before the next, which increases speed. Here is another example of locks with multi-threading:

```python
import threading, time

count = 0

class MyThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        global count
        lock . acquire ( ) # Acquire the lock 
        temp = count + 1
        time.sleep(0.001)
        count = temp
        lock . release ( ) # Release the lock 

lock = threading.Lock()
threads = []
for  _  in  range ( 1000 ) :
    thread = MyThread()
    thread.start()
    threads.append(thread)
for thread in threads:
    thread.join()
print(f'Final count: {count}')
```

Apart from GIL (Global Interpreter Lock), there is also a lock called a R-Lock (Recursive Lock). This is a lock that uses a algorithm to pass the lock down to another thread, which is slightly different from a GIL. Here is an example of a R-Lock:

```python
import threading
import  time

class Test:
    rlock = threading.RLock()
    def __init__(self):
        self.number = 0

    def execute(self, n):
        # Originally is to acquire and release locks, then if you forget to write lock.release() sometimes, it becomes a deadlock.
        # And with can solve this problem.
        with Test.rlock:
            # with There is a mechanism for releasing resources inside
            self.number += n

    def add(self):
        with Test.rlock:
            self.execute(1)

    def down(self):
        with Test.rlock:
            self.execute(-1)

def add(test):
    for  i  in  range ( 1000000 ) :
        test.add()

def down(test):
    for  i  in  range ( 1000000 ) :
        test.down()

if __name__ == '__main__':
    thread  =  Test ( ) # instantiation 
    t1 = threading.Thread(target=add, args=(thread,))
    t2 = threading.Thread(target=down, args=(thread,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(t.number)
```

Big question --- If GIL is such an efficient process to run code, why would there be any problems....right? Well, actually no. There are a few problems with using a GIL. Three of them are that using a GIL is slow, it's also resource consuming, and it's not the MOST efficient way to multi-thread. In certain scenarios, it's better to just use sync even. So how can we avoid GILs, since there typically is only one throughout the course of one program? This means that using multi-threading even with a multi-core cpu, would not be very much of a benefit, and rather slower than a synchronous program. We can bypass GILs using threadpooling, which is implemented in a python module, that you can install through pip like this:

```python
pip install threadpool
```

Here is an example of a code that bypasses GIL:

```python
import  time
import threadpool

# To execute more time-consuming functions, you need to open multiple threads
def get_html(url):
    time.sleep(3)
    print(url)
# According to the original single-threaded running time: 300s
# And the transformation of multi-threaded pool: 30s
# Use multiple threads to execute the telent function
urls = [i for i in range(100)]
pool  =  threadpool . ThreadPool ( 10 ) # Create a thread pool 

# Submit tasks to the thread pool
requests = threadpool.makeRequests(get_html, urls)

# Start the task
for req in requests:
    pool.putRequest(req)
pool.wait()
```

This code basically just generates a "pool" of threads, and makes requests to call the get\_html function that was defined and passes the urls list comprehension list as an argument to the get\_html function. Then we put the request by iterating through the actual requests that were made, and we waited for the results. That is the basic process of bypassing a GIL, and thus making your program much more efficient.