#https://viblo.asia/p/da-luong-trong-python-multithreading-WAyK8MO6ZxX

import threading
import time
 
def TungThread1():
    print (threading.currentThread().getName(), 'Starting')
    time.sleep(2)
    print (threading.currentThread().getName(), 'Exiting')
 
def TungThread2():
    print (threading.currentThread().getName(), 'Starting')
    print (threading.currentThread().getName(), 'Exiting')
 
d = threading.Thread(name='TungThread1', target=TungThread1)
#d.setDaemon(True)
t = threading.Thread(name='TungThread2', target=TungThread2)
 
d.start()
t.start()
