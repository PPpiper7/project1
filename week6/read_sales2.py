def main():
    sales_file = open('week6/sales.txt', 'r')

    

    for line in sales_file:
        amount = float(line)

        print(format(amount,'.2f'))
        

    sales_file.close()

main()