keep_going = 'y'
comm_rate = 2.5
while keep_going == 'y' or keep_going == 'Y' :
    sales = float(input('Enter the item`s wholesale cost: '))

    commission = sales * comm_rate

    print('Retail price: $', \
    format(commission, ',.2f'), sep='')

    keep_going = input('Do you want to calulast another' + \
                       'commission (Enter y for yes): ')