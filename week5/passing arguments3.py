def main():
  value = 99
  print('The value is',value)
  change_me(value)
  print('Back in changing the value is',value)
def change_me(arg):
  print('I am changing The value.')
  arg = 0
  print('Now the value is',arg)
main()