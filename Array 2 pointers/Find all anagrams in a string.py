from collections import Counter


def find_anagrams(p, s):
    d={i:p.count(i) for i in p}
    cp=d.copy()
    res=[]
    window=[]
    right_ptr=0
    left_ptr=0
    while right_ptr<len(s) and right_ptr>=left_ptr:
        window.append(s[right_ptr])
        if s[right_ptr] in cp.keys():
            cp[s[right_ptr]]-=1
        if not any(cp.values()):
            res.append(left_ptr)
        if len(window)>=len(p):
            if s[left_ptr] in cp.keys():
                cp[s[left_ptr]]+=1
            window.pop(0)
            left_ptr+=1
            right_ptr+=1
        else:
            right_ptr+=1
    return res

def main():
    s, p = input().split()
    answer = find_anagrams(p, s)
    print(len(answer))
    print(' '.join([str(i) for i in answer]))


if __name__ == "__main__":
    main()

'''
from collections import Counter


def find_anagrams(p, s):
    window_size=len(p)
    d={i:p.count(i) for i in p}
    cp=d
    res=[]
    left_ptr=0
    right_ptr=0
    temp={}
    #temp[s[0]]=1
    while right_ptr<len(s):
        #temp={j:s[i:i+window_size].count(j) for j in s[i:i+window_size]}
        #print(temp,window_size)
        if sum(temp.values())==window_size:
            if temp[s[left_ptr]]<=1:
                temp.pop(s[left_ptr])
            else:
                temp[s[left_ptr]]-=1
            left_ptr+=1
            #print('left increased')
        else:
            if s[right_ptr] in temp.keys():
                temp[s[right_ptr]]+=1
            else:
                temp[s[right_ptr]]=1
            right_ptr+=1
            #print('right increased')

        if temp==cp:
            res.append(left_ptr)
    return res

def main():
    s, p = input().split()
    answer = find_anagrams(p, s)
    print(len(answer))
    print(' '.join([str(i) for i in answer]))


if __name__ == "__main__":
    main()
'''