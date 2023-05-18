# waiting tasks using joins

"""join operation blocks until the child thread completes its work"""
"""during this time parent thread will go to sleep and it will not be runnable"""
"""once the child thread completes its work and it terminates, the join will release.. and the parent thread will wake up (or unblock) and continue with its execution"""

from threading import Thread
from time import sleep

def child():
    print("Child Thread doing work...")
    sleep(5)
    print("Child Thread done...")

def parent():
    t = Thread(target=child, args=([]))
    t.start()
    print("Parent Threat is waiting...")
    t.join() # this particular line will be block the parent thread until the child thread finishes (until the child thread terminates)
    print("Parent Thread is unblocked...")

    """we can also specify a timeout value inside join()""" # t.join(5)
    """it means we can wait for a number of seconds until the child terminates"""
    """if the child doesn't terminate within those seconds, the duration will also unblock and the parent thread will continue"""

parent()