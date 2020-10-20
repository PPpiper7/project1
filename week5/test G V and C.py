import random
HEADS = 1 
TAILS = 2 
TOSSES = 10
print('TOSSES :',TOSSES)
def asd() : 
 for toss in range (TOSSES):
  if random.randint (HEADS, TAILS) == HEADS :
    print('Heads')
  else: 
    print('Tails')
asd()
def main() : 
    total = 0
    tota = 0

    for pp in range(TOSSES):
        if (HEADS,TAILS) == HEADS:
            total = total

        else:
            tota = tota 
    print('Total Heads',total)
    print('Total Tails',tota)
main()

