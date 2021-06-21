from queue import PriorityQueue as pq

def reduceArray(n, arr):
    que=pq()
    for i in arr:
        que.put(i)
    element=que.get()
    return element

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    res = reduceArray(n, arr)
    print(res)


if __name__ == "__main__":
    main()
