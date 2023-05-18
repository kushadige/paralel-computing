from multiprocessing import Process, set_start_method
from time import sleep

def do_work():
    print("Staring work")
    i = 0
    for _ in range(2000000):
        i += 1
    print("Finished work")

if __name__ == "__main__":
    set_start_method("spawn")
    for _ in range(5):
        p = Process(target=do_work, args=())
        p.start()