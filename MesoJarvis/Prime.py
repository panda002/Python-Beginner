a = int(input('Enter No :'))
i = 0
for i in range(1, a):
    if a % i == 0:
        print('Number is not prime')
        break
    i = i + 1
    if a == i:
        print('Number is prime')


