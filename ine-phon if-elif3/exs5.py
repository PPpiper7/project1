x = (input('Enter a string: '))
print('This is what I found about that string:')
if x.isalnum():
  print('The string is alphanumeric.')
if x.isalpha():
  print('The string contains only alphabetic characters.')
if x.islower():
  print('The letters in the string are all lowercase.')
if x.isnumeric():
  print('The string contains only digits.')
if x.isupper():
  print('The letters in the string are all uppercase.')
