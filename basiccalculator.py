num1 = int(input('Enter Your First Number : '))
num2 = int(input('Enter Your Second Number : '))
op = input('Enter Your Oparetor : ')


if op == '+':
    print('Your Addition is : ',num1+num2)
elif op =='-':
    print('Your Subtraction is : ',num1-num2)
elif op =='*':
    print('Your Multiflication is : ',num1*num2)
elif op =='/':
    if num2 != 0:
        print('Your Multiflication is : ',abs(num1/num2))
    else:
        print('Error: Division by zero is not allowed!')
    
else:
    print("Invalid Oprator")