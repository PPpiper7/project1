print('Please select operation')
print('1.add')
print('2.Subtract')
print('3.Multiply')
print('4.Divide')
operation = int(input('Select opration form 1, 2, 3, 4 : '))
n = int(input('Enter first number :'))
m = int(input('Enter second number :'))
if  operation == 1 :
    print( n,'+',m,'=',n + m )
elif operation == 2 :
    print( n,'-',m,'=',n - m )
elif operation == 3 :
    print( n,'*',m,'=',n * m )
elif operation == 4 :
    print( n,'/',m,'=',n / m )
