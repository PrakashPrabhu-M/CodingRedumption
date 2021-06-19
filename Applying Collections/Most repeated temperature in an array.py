def mostRepeatedTemperature(n, temperature):
    d={}
    for i in temperature:
        if i in d.keys():
            d[i]+=1
        else:
            d[i]=1
    #print(d)
    max_count=max(d.values())
    #print(max_count)
    x=d.keys()
    l=[]
    for i in x:
        if d[i]==max_count:
            l.append(i)
            #print(l)
    return max(l)

def main():
    n = int(input())
    temperature = list(map(int, input().split()))
    res = mostRepeatedTemperature(n, temperature)
    print(res)


if __name__ == "__main__":
    main()
