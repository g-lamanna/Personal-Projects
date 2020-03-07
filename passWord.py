#Hello World

print('''*******Master Password Manager*******

Please Enter Your Password to Continue....

''')
userPass = input()

def passManager():
    masterPass = 'fataViamInven1ent'
    if userPass == masterPass:
        password_introduction()
def password_introduction():
    print('''
    ***** What would you like to do? ******
    -(A)dd new password and username 
    -(S)earch Passwords by Service
    -(R)andom Password
    ''')
    user_answer = input()
    options = {"R":random_password_generator()
             #  "A":add_credentials(),
              # "S":search_password()
                }
    if user_answer == options[user_answer]:
        options[user_answer]
def random_password_generator():
    import random
    characters = 'abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_pass = ""
    for i in range(16):
        new_pass += random.choice(characters)
    print (new_pass)
def add_credentials():
    
    
    
    
    
    
    

passManager()
