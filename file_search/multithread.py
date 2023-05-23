# Multi Thread Approach
from os import listdir, path
from time import time
from threading import Thread, Lock

matches = []
mutex = Lock()

def file_search(root, filename):
    if "node_modules" in root:
        return
    print("Searching in:", root)
    
    child_threads = []
    for file in listdir(root):
        full_path = path.join(root, file)
        if filename in file:
            mutex.acquire()
            matches.append(full_path)
            mutex.release()
        if path.isdir(full_path):
            t = Thread(target=file_search, args=([full_path, filename]))
            t.start()
            child_threads.append(t)

    for t in child_threads:
        t.join()


def main():
    start_time = time()
    t = Thread(target=file_search, args=(["/Users/blitzkrieg/Desktop", "README.md"]))
    t.start()
    t.join()
    end_time = time()
    print("Finished %f sec." %(end_time - start_time))
    for m in matches:
        print("Matched:", m)

main()
    