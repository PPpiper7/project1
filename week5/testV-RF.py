def main():
    first_name,last_name = get_name()
    print('first name :',first_name,'last name',last_name)
    password(first_name,last_name)

def get_name():
  first = input('Enter your first name: ')
  last = input('Enter your last name: ')
  return first, last 

def password(f,l):
    len(l) // 2
    if len(l) % 2 == 0:
        print (f[:3] + l[(len(l)// 2)-2:(len(l)// 2) + 1])
    else:
        print (f[:3] + l[(len(l)// 2)-1:(len(l)// 2) + 2])


main()

     
     