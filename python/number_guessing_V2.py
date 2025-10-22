from random import randint
from time import sleep,time
from math import log

def menu():
    user=None
    while user!='me' or user!='ai' or user!='AI':
        user=input('''\n    Welcome to number guessing game!
    Do YOU want to guess the number (type "me") or have the AI guess it (type "AI"?
    Type here: ''').lower()
        if user=='me':
            user_guess()
            break
        elif user=='ai':
            game_AI()
            break

def user_guess():
    print('''\n   Now you have to select the range for number and then the difficulty''')
    while True:
        try:
            range=(int(input('     Enter the lower range value: ')),int(input('     Enter the higher range value: ')))
            guess_req=round(log(range[1]-range[0],2))
        except Exception:
            continue
        else:
            break
    AI=randint(range[0],range[1])
    while True:    
        difficulty=input(f'''\n   Enter your difficulty:
      1.Easy ({guess_req+3} guesses)
      2.Medium ({guess_req+1} guesses)
      3.Hard ({guess_req} guesses)
      Type here: ''').lower()
        if difficulty=='easy' or difficulty=='1':
            game_user(guess_req+3,AI)
            break
        elif difficulty=='medium' or difficulty=='2':
            game_user(guess_req+1,AI)
            break
        elif difficulty=='hard' or difficulty=='3':
            game_user(guess_req,AI)
            break
        else:
            continue

#AI is guessing
def game_AI():
    while True:
        try:
            low_limit,up_limit=int(input('Enter your lower limit: ')),int(input('Enter your upper limit: '))
        except Exception:
            continue
        else:
            limit=[]
            for i in range(up_limit-low_limit+1):
                limit.append(i)
            break
    while True:
        AI_guess=limit[round(len(limit)/2)]
        guess=input(f'{AI_guess}\nIs this your number?(yes/no):')
        if guess=='yes':
            print('YAY I WON!')
            break
        elif guess=='no':
            guess=input('Is your number higher or lower than my guess?: ')
            if guess=='higher':
                forbidden=[]
                for i in limit:
                    if i>AI_guess:
                        forbidden.append(i)
                limit=limit and forbidden
            elif guess=='lower':
                forbidden=[]
                for i in limit:
                    if i<AI_guess:
                        forbidden.append(i)
                limit=limit and forbidden
                
        else:
            print('Enter "yes" or "no"')
            continue


#user is guessing 
def game_user(chance,AI):
    print('\n   Ready?...')
    sleep(2)
    left=chance
    start=time()
    while True:
        if left==0:
            status('lost',AI,start)
            break
        try:
            user=int(input('   Guess here (you can quit anytime by typing "~iquit"): '))
        except Exception:
            continue
        else:
            if user=='~iquit':
                left-=1
                status('lost',AI,start)
                break
            if user==AI:
                left-=1
                status('win',chance-left,start)
                break
            elif user>AI:
                left-=1
                print(f'''\n   Lower!
  
   chances left:{left}''')
            elif user<AI:
                left-=1
                print(f'''\n   Higher!
  
   chances left:{left}''')

def status(result,guesses,start):
    if result=='win':
        print(f'''\n   YOU WON!
   It took you:{round(time()-start,2)}
   guesses:{guesses}''')
    elif result=='lose':
        print(f'''\n   YOU LOST!
   It took you:{round(time()-start,2)}
   The number was:{guesses}''')
    sleep(5)
    user=input('Wanna play again?(yes/no): ')
    if user=='yes':
        menu()
    else:
        pass
                
menu()
