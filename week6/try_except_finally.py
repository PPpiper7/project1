def main():
    try:
        a , b = map(int,input('Input 2 integer values: ').split())
        p = divide(a,b)  
           
    except Exception as err:
        print(err)
    else:
        print("result is",p)
    finally:
        print('executing finally clause')
    

def divide(x, y):
    result = x / y
    return result
    
main()