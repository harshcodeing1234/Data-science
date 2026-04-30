import csv
import json
import os

def write_text():
    file = input('Enter file name:')
    with open(file,'w') as f:
        text = input('Enter text to write in file:')
        f.write(text)
    print('Data write successfully')

try:
    def read_text():
        file = input('Enter file name:')
        with open(file,'r') as f:
            text = f.read()
        print('\nFile Content:')
        print(text)
except:
    print('file not found')
try:
    def append():
        file = input('Enter file name:')
        with open(file,'a') as f:
            text = input('Enter text to append:')
            f.write('\n' + text)
        print('data append successfully')
except:
    print('file not found!')

while True:
    print('1. Write Text file')
    print('2. Read text file')
    print('3. Append text file')
    print("4. Exit")

    choice = int(input('Enter choice:'))

    if choice == 1:
        write_text()
    