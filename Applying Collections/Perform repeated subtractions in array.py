import heapq

def reduceArray(n, arr):
    li=[-x for x in arr]
    heapq.heapify(li)
    res=0
    while len(li)!=1:
        element1=heapq.heappop(li)*-1
        element2=heapq.heappop(li)*-1
        res=abs(element1-element2)
        heapq.heappush(li,-res)
        #heapq.heapify(li)
    return -li[0]


def main():
    n = int(input())
    arr = list(map(int, input().split()))
    res = reduceArray(n, arr)
    print(res)


if __name__ == "__main__":
    main()
