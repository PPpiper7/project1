pay1 = int(input('Enter the number of hors worked: '))
pay2 = int(input('Enter the hourly pay rate: '))
pay3 = (pay1 - 40 ) * 1.5
pay4 = (40 * pay2)
if pay1 > 40 :
    print('The gross pay in: ',pay3 * pay2 + pay4)
else :
    print('the geoss pay in: ',pay1 * pay3)
