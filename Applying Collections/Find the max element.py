# TODO: Create your data structure here after importing the right module

import queue
que=queue.PriorityQueue()
def insert(num):
    que.put(-num)

def getMax():
    return -1*que.get()

