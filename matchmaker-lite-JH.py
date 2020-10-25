# Jory Haddad
# Matchmaker Lite

introduction='''
Welcome to Matchmaker Lite

This program determines our relationship.
For each question answer on a scale of 1-5,
1 being strongly disagree, and 5 being strongly agree.

Good luck, we are all counting on you.

'''

print(introduction)

question= [
    'I love Star Wars',
    'I like pets',
    'I am sarcastic all the time',
    'I love video games',
    'I love tacos'
]

desiredresponse= [
    5, # strongly agree
    1, # strongly disagree
    3, # neutral
    5, # strongly agree
    2  # disagree
]

userresponse1=6

while userresponse1>5 or userresponse1<1:
    userresponse1=int(input(question[0]))
    desiredresponse1=desiredresponse[0]
    compatability1=5-abs(userresponse1-desiredresponse1)
    if userresponse1>5 or userresponse1<1:
        print('')
        print('Please try again.')
        print('')
print('Question 1 compatability: ' + str(compatability1))
print('')

userresponse2=6

while userresponse2>5 or userresponse2<1:
    userresponse2=int(input(question[1]))
    desiredresponse2=desiredresponse[1]
    compatability2=5-abs(userresponse2-desiredresponse2)
    if userresponse2>5 or userresponse2<1:
        print('')
        print('Try again.')
        print('')
print('Question 2 compatability: ' + str(compatability2))
print('')

userresponse3=6

while userresponse3>5 or userresponse3<1:
    userresponse3=int(input(question[2]))
    desiredresponse3=desiredresponse[2]
    compatability3=5-abs(userresponse3-desiredresponse3)
    if userresponse3>5 or userresponse3<1:
        print('')
        print('...')
        print('')
print('Question 3 compatability: ' + str(compatability3))
print('')

userresponse4=6

while userresponse4>5 or userresponse4<1:
    userresponse4=int(input(question[3]))
    desiredresponse4=desiredresponse[3]
    compatability4=5-abs(userresponse4-desiredresponse4)
    if userresponse4>5 or userresponse4<1:
        print('')
        print('Why?')
        print('')
print('Question 4 compatability: ' + str(compatability4))
print('')

userresponse5=6

while userresponse5>5 or userresponse5<1:
    userresponse5=int(input(question[4]))
    desiredresponse5=desiredresponse[4]
    compatability5=5-abs(userresponse5-desiredresponse5)
    if userresponse5>5 or userresponse5<1:
        print('')
        print('Fail again and you will be terminated.')
        print('')
print('Question 5 compatability: ' + str(compatability5))
print('')

totalcompatability=((compatability1*3)+(compatability2*2)+(compatability3*1)+(compatability4*3)+(compatability5*1))*2
print('Total Compatability: ' + str(totalcompatability))
print('')

if totalcompatability<=75 and totalcompatability>50:
    print('You shall be my friend. Prepare for sarcastic responses.')

if totalcompatability<=100 and totalcompatability>75:
    print('We are meant to be together. We shall get married in 2 years, no later, no earlier.')

if totalcompatability<=50:
    print('We are incompatible. Prepare to be terminated.')
