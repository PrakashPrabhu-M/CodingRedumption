# TODO: Implement this method
def countVowels(s):
    s=s.lower()
    vowels=list('aeiou')
    count=0
    for i in s:
        if i in vowels:
            count+=1
    return count


def main():
    s = input()
    res = countVowels(s)
    print(res)


if __name__ == "__main__":
    main()
