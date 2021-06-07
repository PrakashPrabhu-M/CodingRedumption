def findQuadrant(x, y):
    if x<0:
        return 3 if y<0 else 2
    if x>0:
        return 4 if y<0 else 1


def main():
    x, y = map(float, input().split(' '))
    quadrant = findQuadrant(x, y)
    print(quadrant)


if __name__ == "__main__":
    main()
