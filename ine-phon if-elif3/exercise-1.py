score1 = int(input('Enter the score for test1: '))
score2 = int(input('Enter the score for test2: '))
score3 = int(input('Enter the score for test3: '))
score_all = (test1 + test2 + test3 ) / 3
print("/n 'The average score is: ' ",score_all)

if score_all >= 95:
    print(' Congratulaions! /n That is a great average!')