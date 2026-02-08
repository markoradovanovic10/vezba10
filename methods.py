import json
import os

def loadfile(filename):
    with open(filename, 'r') as file:
        products = json.load(file)
        return products

def savefile(filename, data):
    data_new = loadfile(filename)
    data_new.append(data)
    with open(filename, 'w') as file:
        json.dump(data_new, file, indent=4)

def deletefile(filename):
    if os.path.exists(filename):
        os.remove(filename)
    else:
        print("File doesn't exist")
        return 1

def emptyfile(filename):
    if deletefile(filename) != 1:
        with open(filename, 'w') as file:
            json.dump([], file)
