def power(a, b):
    product = 1
    x = a
    while b > 0:
        if b % 2 == 1:
            product *= x
            if product > 10**9:
                return product
        b //= 2
        x **= 2
    return product

power(2,5)