import random
import os

def roll():
    ran = random.randint(0, 1000)
    return ran

def save(number, file1):
    file1.write(str(number))
    file1.write('\n')
    path = os.path.abspath(os.getcwd())
    return path

def create(location):
    file1 = open('python_rolls.txt', 'w+')
    return file1, 'python_rolls.txt'

def check_size(file1):
    size = os.stat(file1).st_size
    return size

def loop(location):
    file1, name = create(location)
    size = 0
    while size < 1048576:
        number = roll()
        save(number, file1)
        size = check_size(name)
        print(size)

loop('/')
