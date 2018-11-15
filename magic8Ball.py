import random

def getAnswer(answerNumber):
    if answerNumber== 1:
        return 'It is certain'
    if answerNumber== 2:
        return 'It is decidedly so'
    if answerNumber== 3:
        return 'Yes'
    if answerNumber== 4:
        return 'Reply hazy try again'
    if answerNumber==5:
        return 'Ask again later'
    if answerNumber== 6:
        return 'Concentrate and ask again'
    if answerNumber== 7:
        return 'My reply is no'
    if answerNumber== 8:
        return 'Outlook not so good'
    if answerNumber== 9:
        return 'Very doubtful'
r = random.randint(1,9)
fortune= getAnswer(r)
print(fortune)

#if you use print('aaa',end = ''), then there will not be another line after
#your print function
#if you use spe=',', then instead of spaces, we will get commas seperating
#each element
