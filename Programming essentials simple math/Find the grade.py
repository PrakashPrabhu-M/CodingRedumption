def gradingSystem(score):
    A,B,C,D,E,F=eval("80<=score"),eval("60<=score"),eval("50<=score"),eval("45<=score"),eval("25<=score"),eval("0<=score")
    grade=list('ABCDEF')
    for n,i in enumerate([A,B,C,D,E,F]):
        if i:
            return grade[n]
    return 'Invalid'

def main():
    score = float(input())
    grade = gradingSystem(score)
    print(grade)

if __name__=="__main__":
    main()
