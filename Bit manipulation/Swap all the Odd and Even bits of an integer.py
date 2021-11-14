
def swap_all_odd_and_even_bits(n):
    i=3
    s=n
    while i>=0:
        a=1 if (n&(1<<i)>0) else 0
        b=1 if (n&(1<<(i-1))>0) else 0
        if (a^b)>0:
            s=s^(1<<i)
            s=s^(1<<(i-1))
        i-=2
    return s

def main():
    n = int(input())
    answer = swap_all_odd_and_even_bits(n)
    print(answer)

if __name__ == "__main__":
    main()