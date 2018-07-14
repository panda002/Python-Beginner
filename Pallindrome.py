num=str(input('enter a number : '))
print('the number entered is - ',num)
#print (len(num))
j=len(num)
#a= (list(range(j-1,-1,-1)))
#print (a)
for i in (list(range(j-1,-1,-1))):
    num2 = num[i]
    print (num2)
for a in (list(range(0,j))):
    num3=num[a]
    print("reverse is : ",num[a])
if num3==num2:
    print('Number is Pallindrome')
else:
    print('Number is NOT Pallindrome')
