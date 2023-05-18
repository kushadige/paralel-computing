from threading import Thread
from time import sleep

def do_work():
    print("Staring work")
    # i = 0
    # for _ in range(2000000): #CPU Bound
    #     i += 1
    sleep(1)
    print("Finished work")

for _ in range(5):
    t = Thread(target=do_work, args=())
    t.start()