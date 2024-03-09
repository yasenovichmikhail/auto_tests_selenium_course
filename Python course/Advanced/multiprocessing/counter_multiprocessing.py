from multiprocessing import Process, cpu_count
import time

def counter(num):
    count = 0
    while count < num:
        count += 1

def main():
    print(cpu_count())
    
    a = Process(target=counter, args=(12500000,))
    b = Process(target=counter, args=(12500000,))
    c = Process(target=counter, args=(12500000,))
    d = Process(target=counter, args=(12500000,))
    e = Process(target=counter, args=(12500000,))
    f = Process(target=counter, args=(12500000,))
    g = Process(target=counter, args=(12500000,))
    k = Process(target=counter, args=(12500000,))

    a.start()
    b.start()
    c.start()
    d.start()
    e.start()
    f.start()
    g.start()
    k.start()

    a.join()
    b.join()
    c.join()
    d.join()
    e.join()
    f.join()
    g.join()
    k.join()
    print("finished in:", time.perf_counter(), "seconds")

if __name__ == '__main__':
    main()