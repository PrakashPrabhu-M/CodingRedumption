from collections import Counter

def length_of_substring(s, k):
    window_left=0
    window_right=0
    max_str=0
    d={}
    while window_right<len(s):
        if s[window_right] in d.keys():
            d[s[window_right]]+=1
        else:
            d[s[window_right]]=1
        if len(d.keys())<=k:
            window_right+=1
        else:
            if d[s[window_left]]<=1:
                d.pop(s[window_left])
            else:
                d[s[window_left]]-=1
            window_left+=1
        if max_str<window_right-window_left+1:
            max_str=window_right-window_left+1        

    return max_str


def main():
    n, k = map(int, input().split())    
    s = input()
    answer = length_of_substring(s, k)
    print(answer)

if __name__ == "__main__":
    main()
