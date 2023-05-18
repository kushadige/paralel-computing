from urllib import request
from json import dumps
from time import time, sleep
from threading import Thread, Lock

finished_count = 0

def count_letters(url, frequency, mutex):
    response = request.urlopen(url)
    txt = str(response.read())
    mutex.acquire()
    for l in txt:
        letter = l.lower()
        if(letter in frequency):
            frequency[letter] += 1
    global finished_count
    finished_count += 1
    mutex.release()

def main():
    frequency = {}
    mutex = Lock()
    for c in "abcdefghijklmnopqrstuvwxyz":
        frequency[c] = 0
    
    start_time = time()
    for i in range(1000, 1020):
        Thread(target=count_letters, args=(f"https://www.rfc-editor.org/rfc/rfc{i}.txt", frequency, mutex)).start()


    while True:
        mutex.acquire()
        if finished_count == 20:
            break
        mutex.release()
        sleep(0.5)

    end_time = time()
    print(dumps(frequency, indent=4))
    print("Done, time taken", end_time - start_time)
        
main()