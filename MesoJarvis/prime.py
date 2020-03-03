from builtins import sum

prices = [1, 3, 3, 2, 5]


def finalPrice(prices):
    # Write your code here
    stack = []
    res = 0

    for i in prices:
        if stack:
            if i > stack[-1]:
                stack.append(i)
            else:
                while stack and i <= stack[-1]:
                    res += stack[-1] - i
                    stack.pop(-1)
                stack.append(i)
        else:
            stack.append(i)
    return res + sum(stack)


if __name__ == '__main__':
    prices_count = 5

    prices = [1, 3, 3, 2, 5]

    for _ in range(prices_count):
        prices_item = prices_count
        prices.append(prices_item)

    finalPrice(prices)
