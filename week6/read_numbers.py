def main():
    infile = open('week6/numbers.txt','r')
    
    num1 = int(infile.readline())
    num2 = int(infile.readline())
    num3 = int(infile.readline())

    infile.close()

    total = num1 + num2 + num3

    print('The numbers are:',num1,num2,num3)
    print('Their Total is:',total)

main()