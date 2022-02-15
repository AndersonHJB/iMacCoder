---
title: Multithreading with programs
tags: []
id: '1930'
categories:
  - - Alex Homework
date: 2021-10-02 08:05:59
---

Multithreading is a big concept when it comes to high efficiency when running bigger tasks. The overall concept of multithreading, is under a topic called "Multi channel acceleration". This is basically when you limit your threads to a certain amount that can be run at one time, and this way, the data that is being proceessed is safe, and it's more efficient than trying to run many things at once, and clashing into each other. This is where a Global Interpreter Lock comes in handy. (GIL) Global Interpreter Lock - This is basically when your computer limits the amount of threads that can be run at one time, to only one. This means that your computer will run one thread at a time, put a lock around the thread that is being run currently, and pass the key to the lock to another thread. This means that if the other thread wants to run, it has to unlock the GIL, therefore it has to wait for the previous thread to finish running. GILs are used in synchronous programs, such as CPython, or Ruby. Keep in mind that this only applies for synchronous programs, and does not apply for multithreaded-programs. Concept of Threading in Python - There are two main concepts and "methods" of multithreading and multiprocessing, called concurrency and parallelism. Concurrency - Concurrency is basically when your computer runs only one thread/instruction at once, but it rotates through all the instructions it needs to go through/run. This means that it's basically rotating through the "list" of instructions/threads it needs to run so quickly, that the raw human eye, can't process, such as hundreds if not millions of times per second. Parallelism - Parallelism is basically just running many processes/threads at once, in a way where each thread that is being run, don't collide with each other, just like in mathematics, where a parallel line won't collide with the line that it's parallel to. This is the biggest difference between Concurrency and Parallelism, as Concurrency still only runs one thread/instruction at a time, just like synchronous programs, however it rotates very quickly through the list of instructions. Parallelism basically just running many processes at once in a way where they don't collide, and this maintains the efficiency and the protection of data with parallelism. Concurrency is multi-threading and parallelism is multi-processing. Another difference between concurrency(multi-threading) and parallelism(multi-processing), is that concurrency doesn't require multi-core cpus, however parallelism does. This is because in order to run many threads at once, you have to have many things to run them with, hence why you have to use each cpu core to run a certain amount of threads, and because concurrency only runs one thread at one time, that is why concurrency doesn't require multi-core cpus, however parallelism does.