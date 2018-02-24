import logging
import threading
import time

logging.basicConfig(level=logging.DEBUG, format='[%(levelname)s] (%(threadName)-10s) %(message)s')

def worker (num) :
    print ("Worker: %s" % num)
    return


threads = []
'''
for i in range(5) :
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)
    t.start()
'''

def worker_thread() :
    logging.debug(' begins')
    time.sleep(2)
    logging.debug( ' ends')


def server_thread() :
    logging.debug(' begins')
    time.sleep(3)
    logging.debug( ' ends')
    time.sleep(2)
    logging.debug( ' ends')


w = threading.Thread(name='worker_thread', target=worker_thread)
w1 = threading.Thread(target=worker_thread)
s = threading.Thread(name='server_thread', target=server_thread)

w.start()
w1.start()
s.start()
