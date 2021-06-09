def decimalToBaseConversion(num, base):
    res=[]
    while num:
        res.append(num%base)
        num//=base
    
    hexa={}
    for n,i in enumerate(list('0123456789ABCDEF')):
        hexa[n]=i
    return ''.join(str(x) for x in [hexa[a] for a in res][::-1])
  
def main():
    num, base = map(int, input().split(' '))
    ans = decimalToBaseConversion(num, base)
    print(ans)


if __name__ == "__main__":
    main()