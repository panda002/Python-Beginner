c = int(input('Enter No :'))
for num in range(0,c):
   if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               print(num,'is not prime')
               break
       else:
           print(num, 'is prime')


print('enter the range')
lower = int(input("lower range"))
upper = int(input("Upper range"))

for a in range(lower, upper + 1):
    if a > 1:
        for b in range(2, a):
            if a % b == 0:
                print(a, 'number is not prime')
                break
        else:
            print(a, 'number is prime')
