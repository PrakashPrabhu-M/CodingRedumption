def mostFrequent(s):
    d={}
    for i in s:
        if i not in d.keys():
            d[i]=1
        else:
            d[i]+=1
    maxi=max(d.values())
    chars=[]
    #print(list(d.values()).count(max)!=1)
    if list(d.values()).count(max)!=1:
        chars=([x for x in d.keys() if d[x]==maxi])
        #print(chars)
        return min(chars), s.count(min(chars))
    chars=[x for x in d.keys() if d[x]==maxi]
    return chars, s.count(chars)

def main():
    s = input()
    res = mostFrequent(s)
    print(*res)


if __name__ == "__main__":
    main()
