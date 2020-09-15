def main():
    filename = input('Enter a filename: ')

    try:

        infile = open('week6/'+filename, 'r')

        contens = infile.read()

        print(contens)

        infile.close()

    except IOError:
        print('An error occurred trying to read')
        print('the file','week6/'+filename)

main() 