from os import listdir, path
from time import time
from threading import Thread, Lock
from wait_group import WaitGroup

matches = []
mutex = Lock()

def file_search(root, filename, wait_group):
    if "node_modules" in root:
        return
    print("Searching in:", root)
    
    for file in listdir(root):
        full_path = path.join(root, file)
        if filename in file:
            mutex.acquire()
            matches.append(full_path)
            mutex.release()
        if path.isdir(full_path):
            wait_group.add(1)
            t = Thread(target=file_search, args=([full_path, filename, wait_group]))
            t.start()

    wait_group.done()

def main():
    wait_group = WaitGroup()
    wait_group.add(1)

    start_time = time()
    t = Thread(target=file_search, args=(["/Users/blitzkrieg/Desktop", "README.md", wait_group]))
    t.start()
    wait_group.wait() # main thread will be waiting on this function 
    end_time = time()

    print("Finished %f sec." %(end_time - start_time))
    for m in matches:
        print("Matched:", m)

main()
    