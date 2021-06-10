def bigIntegerAddition(s1, s2):
    carry=0
    add=0
    total=[]
    if len(s1)>len(s2):
        s2='0'*(len(s1)-len(s2))+s2
    else:
        s1='0'*(len(s2)-len(s1))+s1
    for i in range(len(s1)-1,-1,-1):
        #print(f'adding {s1[i]}, {s2[i]} and {carry}')
        add=str(int(s1[i])+int(s2[i])+carry)
        carry=int(add[:-1]) if len(add)>1 else 0
        add=add[-1]
        total.append(add)
        #print('add={}, carry={}, total={}'.format(add,carry,total))
    #print(carry)
    if carry!=0:
        total.append(str(carry))
    return ''.join(total[::-1])


def main():
    s1, s2 = input().split(' ')
    add = bigIntegerAddition(s1, s2)
    print(add)


if __name__ == "__main__":
    main()
