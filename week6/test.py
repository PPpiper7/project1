AREA_CIRCLE_CHOICE = 1 
CIRCUMFERENCE_CHOICE = 2 
DR = 3
QUIT_CHOICE = 4
def main():
    choice = 0 
    while choice != QUIT_CHOICE:
        display_menu() 
        choice = int(input('Enter your choice: ')) 
        if choice == AREA_CIRCLE_CHOICE:
                infile = open('week6/frind.txt','r')
                file_contents = infile.read()
                infile.close()
                print(file_contents)
        elif choice == CIRCUMFERENCE_CHOICE:
            f = open('week6/frind.txt','a+')
            f.write(str(input('add frind name: ')))
            f.close()
            print('Your data add list')
        elif choice == DR:
                emp_file = open('week6/employees.txt','w')
                for count in range(1,emp_file + 1):
                    print('',count,sep='')
                emp_file.close()
                print(emp_file)
        elif choice == QUIT_CHOICE:
            print('Quit')
        else:
            print('Error: invalid selection.')
def display_menu(): 
    print('MENU')
    print('1) open file') 
    print('2) add') 
    print('3) Delete')
    print('4) Quit')
main()