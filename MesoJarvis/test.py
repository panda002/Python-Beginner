a = {1, 2, 3, 4, 5, 6}
print(len(a))


def sum1():
    total = 0
    for i in a:
        total = total + i
    return total


b = sum1()
print(b)


def avg():
    return b / len(a)


c = avg()
print(c)
