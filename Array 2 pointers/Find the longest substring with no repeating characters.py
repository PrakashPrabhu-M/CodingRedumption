# LongestSubstringWithoutRepeatingCharacter Solution
def lengthOfLongestSubstring(s):
    longestSubstringLength = 0
    left_ptr=0
    right_ptr=0
    l=[0]*187#-65
    while right_ptr<=len(s) and right_ptr>=left_ptr:
        l[ord(s[right_ptr])]+=1
        if l[ord(s[right_ptr])]>1:
            while s[right_ptr]!=s[left_ptr]:
                left_ptr+=1
            left_ptr+=1
            l[ord(s[right_ptr])]-=1
            right_ptr+=1
        else:
            right_ptr+=1
    return right_ptr-left_ptr

if __name__ == '__main__':
    s = input()
    result = lengthOfLongestSubstring(s)
    print(result)
