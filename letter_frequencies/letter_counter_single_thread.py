from urllib import request
from json import dumps
from time import time

def count_letters(url, frequency):
    response = request.urlopen(url)
    txt = str(response.read())
    for l in txt:
        letter = l.lower()
        if(letter in frequency):
            frequency[letter] += 1

def main():
    frequency = {}
    for c in "abcdefghijklmnopqrstuvwxyz":
        frequency[c] = 0
    
    start_time = time()
    for i in range(1000, 1020):
        count_letters(f"https://www.rfc-editor.org/rfc/rfc{i}.txt", frequency)

    end_time = time()
    print(dumps(frequency, indent=4))
    print("Done, time taken", end_time - start_time)
        
main()