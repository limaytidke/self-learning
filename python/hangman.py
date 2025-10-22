from random import choice as c
import time as t

def entry():
    print('\nWelcome to Hangman!\n')
    t.sleep(1)
    try:
        user=int(input('Selcect difficulty:\n1.Easy\n2.Medium\n3.Hard\n\n'))
    except:
        print('Please enter the corresponding index number')
        t.sleep(1)
        entry()
    else:
        word(user)

def word(d):
    words=c(('apple','banana','cherry','pineapple'))
    word=list('_'*len(words))
    guess=list()
    diff=(2,1,0)
    left=len(words)+diff[d-1]
    game(word,guess,left,words)

def game(word,guesses,left,words):
    timestart=t.time()
    print(' ',word,'incorrect guesses: %s'%guesses,'incorrect guesses left: %s'%left,sep='\n')
    guessed=[]
    while left>0 and ('_' in word):
        guess = input('guess a letter: ')
        if guess=='~iquit':
            break
        if guess == words:
            return status('win',guess,timestart)
        elif len(guess)>1:
            print("Type one characters only! Unless you know the whole word in which case type the word")
            left-=1
            continue
        elif (guess in guessed) or (guess in guesses):
            print('Already guessed')
            continue
        elif guess in words:
            for i in range(len(words)):
                if guess == words[i]:
                    word[i]=guess
            guessed.append(guess)
            print(' ',word,'incorrect guesses: %s'%guesses,'incorrect guesses left: %s'%left,sep='\n')
        elif guess not in words:
            left-=1
            guesses.append(guess)
            print(' ',word,'incorrect guesses: %s'%guesses,'incorrect guesses left: %s'%left,sep='\n')
    if '_' not in word:
        status('win',words,timestart)
    else:
        status('lost',words,timestart)

def status(status,word,timestart):
    timeend=t.time()
    if status=='win':
        print('',word,'You won!','Time taken: %0.1f seconds'%(timeend-timestart),sep='\n')
        t.sleep(1)
    else:
        print('\nYou lost!. The word was: ',word,'Time taken: %0.1f seconds'%(timeend-timestart),sep='\n')
        t.sleep(1)

entry()