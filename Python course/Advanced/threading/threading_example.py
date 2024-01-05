from threading import Thread
import os
import time

def square_numbers():
    for i in range(100):
        i * i

if __name__ == "__main__":
    threads = []
    num_threads = 10

#create threads

for i in range(num_threads):
    thread = Thread(target=square_numbers)
    threads.append(thread)

#start
for thread in threads:
    thread.start()

#join
for thread in threads:
    thread.join()

print('end main')

