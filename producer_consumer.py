#!/usr/bin/python3
# coding=utf-8
"""
Producer Consumer Demo
https://www.youtube.com/watch?v=i1SW4q9yUEs&list=WL#t=471
"""
import threading

__author__ = "Michael Krisper"
__email__ = "michael.krisper@gmail.com"

import time
import random
import queue


class Producer(threading.Thread):
    def __init__(self, q):
        super().__init__()
        self.q = q
        self.food = ["ham", "soup", "salad"]
        self.nextTime = 0

    def run(self):
        while time.clock() < 10:
            if self.nextTime < time.clock():
                f = self.food[random.randrange(len(self.food))]
                self.q.put(f)
                print("Adding {}".format(f))
                self.nextTime += random.random()


class Consumer(threading.Thread):
    def __init__(self, q):
        super().__init__()
        self.q = q
        self.nexttime = 0

    def run(self):
        while time.clock() < 30:
            if self.nexttime < time.clock() and not self.q.empty():
                f = self.q.get()
                print("Removing {}".format(f))
                self.nexttime += random.random() * 2


def main():
    q = queue.Queue(10)
    p = Producer(q)
    c = Consumer(q)
    p.start()
    c.start()


if __name__ == "__main__":
    main()