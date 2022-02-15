---
title: Basics of Non-Daemon Threads
tags: []
id: '1939'
categories:
  - - Alex Homework
date: 2021-10-07 07:59:34
---

In the world of multi-threading in python, there are two different types of threads - daemon and non-daemon. In this particular article, we will be explaining non-daemon threads. So what makes up a thread? A thread is made up of a main thread, and a sub thread. Here is an example of a basic threading program:

```python
import threading, time

def  start ( num ) :
    time.sleep(num)
    print(threading.current_thread().name)
    print(threading.current_thread().isAlive())
    print(threading.current_thread().ident)

print('start')
thread = threading.Thread(target=start,name='my first thread', args=(1,))

thread.start()
print('stop')
```

The code above will output:

```python
start
stop
my first thread
True
2968
```

This is weird right? We printed out a string containing our thread's name first, then a true/false boolean value to check if the thread is still alive, then a generated id for the thread. Only next have we printed start, then defined the thread that we want to create and run. Next, we started the thread, and we printed stop. That's weird right? We printed the name, the boolean value, and the id of the thread first, but the result indicated the "start" and the "stop" strings being outputted first. That doesn't really work with our natural human logic right? Well that is what a non-daemon thread is - a thread where the main thread finishes running before the sub threads are done. This means that the main thread has to await the completion of execution from the sub threads, and the code will instead go to run the other parts of the program first, which is why the order of the output of that program, is contradicting our normal human logic. That claim is proven by this program:

```python
import threading, time

def target(second):
    print(f'Threading {threading.current_thread().name} is runing')
    print(f'Threading {threading.current_thread().name} sleep {second}s')
    time.sleep(second)
    print(f'Threading {threading.current_thread().name} ended')

print(f'Threading {threading.current_thread().name} is runing')

for  i  in  [ 1 , 5 ] : 
    t = threading.Thread(target=target, args=[i])
    # t = threading.Thread(target=target, args=(i,))
    t.start()
print(f'Threading {threading.current_thread().name} is ended')

# Output
Threading MainThread is runing
Threading Thread-1 is runing
Threading Thread-1 sleep 1s
Threading Thread-2 is runing
Threading Thread-2 sleep 5s
Threading MainThread is ended
Threading Thread-1 ended
Threading Thread-2 ended
```

The program's output above proves our claim because you can see that thread 1 is running, then it sleeps because it's waiting for thread 2 to finish running. After that, thread 2 sleeps too, and the main thread ends, then all the threads end. This shows what a non-daemon thread is - a thread where the main thread sleeps and waits for the other sub threads to finish running, then all the threads end together.