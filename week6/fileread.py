def main():
    infile = open('week6/philosophers.txt','r')

    file_contents = infile.read()

    infile.close()

    print(file_contents)

main()