import threading
import time
import queue

def worker1(queue):
    print(threading.current_thread().getName(), 'start')
    while True:
        item = queue.get()
        if item is None:
            break
        print(item)
        queue.task_done()
    print('loggggggggggg')
    print(threading.current_thread().getName(), 'end')

def worker2(queue):
    print(threading.current_thread().getName(), 'start')
    print(queue.get())
    print(queue.get())
    print(threading.current_thread().getName(), 'end')

if __name__ == '__main__':
    #t = threading.Timer(3, worker1)
    # t.start()
    """
    for _ in range(5):
        t1 = threading.Thread(target=worker1)
        t1.setDaemon(True)
        t1.start()
    print(threading.enumerate())

    for thread in threading.enumerate():
        if thread is threading.currentThread():
            print(thread)
            continue
        thread.join()
        """

    queue = queue.Queue()
    for i in range(100000):
        queue.put(i)
    ts = []
    for _ in range(3):
        t1 = threading.Thread(target=worker1, args=(queue, ))
        t1.start()
        ts.append(t1)
    print('task is not done')
    queue.join()
    print('task is done')
    for _ in range(len(ts)):
        queue.put(None)
    [t1.join() for t in ts]
    #t2 = threading.Thread(target=worker2, args=(queue, ))
    #t2.start()

