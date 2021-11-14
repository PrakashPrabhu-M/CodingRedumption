# def longestValidParentheses(s):
#     stack=[]
#     maxi=float('-inf')
#     temp_sum=0
#     for i in s:
#         if i=='(':
#             stack.append(i)
#         elif len(stack)==0:
#             temp_sum=0
#         else:
#             stack.pop()
#             temp_sum+=1
#             if len(stack)==0:
#                 maxi=max(temp_sum,maxi)
        
#     return max(temp_sum,maxi)*2

# def main():
#     S = input()
#     ans = longestValidParentheses(S)
#     print(ans)

# if __name__=="__main__":
#     main()



def valid(s):
    stack=[]
    for i in s:
        if i=='(':
            stack.append(1)
        else:
            stack.pop()
    if len(stack)==0:
        return True
    return False

def longestValidParentheses(s):
    i=0
    j=2
    maxi=float('-inf')
    while i<j:
        if valid(s[i:j]):
            maxi=max(maxi,len(s[i:j]))
            j+=1
        else:
            i+=1
    return max(maxi,len(s[i:j]))

def main():
    S = input()
    ans = longestValidParentheses(S)
    print(ans)

if __name__=="__main__":
    main()
