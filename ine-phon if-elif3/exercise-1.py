score1 = int(input('Enter the score for test1: '))
score2 = int(input('Enter the score for test2: '))
score3 = int(input('Enter the score for test3: '))
score_all = (score1 + score2 + score3 ) / 3
print("The average score is:  ",score_all)

if score_all >=95:
    print("Congratulaions!/n That is a great average!")