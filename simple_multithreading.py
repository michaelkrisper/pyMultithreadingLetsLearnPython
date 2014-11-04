#!/usr/bin/python3
# coding=utf-8
"""
Simple Thread program
"""

__author__ = "Michael Krisper"
__email__ = "michael.krisper@gmail.com"


import threading
import random


def splitter(words):
    mylist = words.split()
    newList = []
    while mylist:
        newList.append(mylist.pop(random.randrange(0, len(mylist))))
    print(" ".join(newList))

def main():
    sentence = "I am a handsome beast. Word."
    num_threads = 5
    threads = []

    print("Starting...")
    for i in range(num_threads):
        t = threading.Thread(target=splitter, args=(sentence,))
        t.start()
        threads.append(t)

    print("Thread count: {}".format(threading.active_count()))
    print("Exiting")

if __name__ == "__main__":
    main()