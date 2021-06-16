# TODO: Create your data structure here after importing the right module

queue=[]
def insert(num):
    queue.append(num)
    queue.sort()

def getMax():
    return queue.pop(-1)
