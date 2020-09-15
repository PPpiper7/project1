def main():
  number1 = int(input('Enter your number 1 :'))
  number2 = int(input('Enter your number 2 :'))
  print('The sum of number 1 and number 2 is')
  show_sum(number1,number2)
def show_sum(num1,num2):
  result = num1 + num2
  print(result)
main()