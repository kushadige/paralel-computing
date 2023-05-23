# searching a particular file in a particular directory location.

# e.g Search("/", "cat.jpg")

# Single Thread Approach
from os import listdir, path
from time import time

matches = [] # contain a list of paths of where the file is located.

def file_search(root, filename):
    if "node_modules" in root:
        return
    print("Searching in:", root)
    for file in listdir(root):
        full_path = path.join(root, file)
        if filename in file:
            matches.append(full_path)
        if path.isdir(full_path):
            file_search(full_path, filename)


def main():
    start_time = time()
    file_search("/Users/blitzkrieg/Desktop", "README.md")
    end_time = time()
    print("Finished %f sec." %(end_time - start_time))
    for m in matches:
        print("Matched:", m)

main()
    