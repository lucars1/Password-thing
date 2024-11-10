import sys
import time
import getpass
def passwordmake(rerun = True):
        
    global password
    
    password = getpass.getpass('enter password: ')
    
    global passwordcount
    
    passwordcount = len(password)
    if passwordcount > 5:
        print('no more then 5 caracters!')
        passwordmake(rerun=True)
        
passwordmake()

print("*" * passwordcount)
trys = 3

def password_guessing(fail = True):

    guess = input('enter guess: ')
    if guess == password:
        print('well done!')
        sys.exit()

    global trys
    trys -= 1
    print('you have:', trys,'trys left')
    if trys == 1:
        #Remove the print function to not show the password if you fail
        print('you fail, it was:', password)
        sys.exit()
password_guessing()
password_guessing()
password_guessing()