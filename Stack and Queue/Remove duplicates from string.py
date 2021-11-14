def removeAdjacentDuplicates(s):
    i=0
    s=list(s)
    while i<len(s)-1 and len(s)>1:
        if s[i]==s[i+1]:
            s.pop(i)
            s.pop(i)
            if i!=0:
                i-=2
            else:
                i-=1
        i+=1
    return ''.join(s)


def main():
    s = input().strip()

    finalString = removeAdjacentDuplicates(s)
    print(finalString)

if __name__=="__main__":
    main()
