# TODO: Implement this method
def capitalise(s):
    words=s.split()
    sentence=[]

    for word in words:
      if word[0].isalpha() and word[0].islower():
        sentence.append(word[0].upper()+word[1:])
      else:
        sentence.append(word)

    return ' '.join(sentence)

def main():
    s = input()
    res = capitalise(s)
    print(res)


if __name__ == "__main__":
    main()