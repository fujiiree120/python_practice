from multiprocessing import (
    Process,
    Lock, RLock, Semaphore, Queue, Event, Condition, Barrier,
    Value, Array, Pipe, Manager
)

import logging
import multiprocessing
import time

logging.basicConfig(
    level=logging.DEBUG, format='%(processName)s: %(message)s'
)

def worker1(i):
    logging.debug('start')
    logging.debug(i)
    logging.debug('end')

def worker2(i):
    logging.debug('start')
    logging.debug(i)
    logging.debug('end')

def f(conn):
    conn.send(['test'])
    conn.close()

if __name__ == "__main__":
    """
    i = 10
    t1 = multiprocessing.Process(target=worker1, args=(i, ))
    t2 = multiprocessing.Process(name='renamed worker', target=worker1, args=(i,))
    t1.start()
    t2.start()
    """
    parent_conn, child_conn = multiprocessing.Pipe()
    p = multiprocessing.Process(target=f, args=(parent_conn, ))
    p.start()
    logging.debug(child_conn.recv())