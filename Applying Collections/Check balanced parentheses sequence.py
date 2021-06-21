# Implement your solution here
def isValid(s):
    stack=[]
    print(s)
    for i in s:
        #print(i)
        if i in ['{','[','(']:
            stack.append(i)
            #print(stack)
        else:
            #print('else',cur_char)
            if not stack:
                return 'false'
            cur_char=stack.pop()
            
            if cur_char=='[' and i!=']':
                return 'false'
            if cur_char=='(' and i!=')':
                return 'false'
            if cur_char=='{' and i!='}':
                return 'false'
    if stack:
        return 'false'
    return 'true'

if __name__ == '__main__':
    s = input().strip()
    result = isValid(s)
    print(result)
