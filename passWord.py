#Hello World

print('''*******Master Password Manager*******
Please Enter Your Password to Continue....
''')
userPass = input()

def passManager():
    masterPass = 'xxxx'
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
    if user_answer == "R":
        random_password_generator()
    elif user_answer == "A":
        add()
    elif user_answer =="S":
        search_pass()
    else:
        print("Please Try again")
        password_introduction()
    cont = ''
    while cont !="N":
        print("Is there anything else? ")
        cont = input()
        if cont == 'N':
            break
        else:
            return password_introduction()
def random_password_generator():
    import random
    characters = 'abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_pass = ""
    for i in range(16):
        new_pass += random.choice(characters)
    print(new_pass)
    return (new_pass)
def add():
    file = "PATH_TO_FILE"
    with open(file,"a+") as file_container:
        user_pass = []
        print("Add Site/Service")
        site = input()
        print("Add Username ")
        user_name = input()
        print("""
        (N)ew password
        (R)andom password
        """)
        user_password_resp = input()
        if user_password_resp == 'R':
            real_pass = random_password_generator()
        elif user_password_resp == 'N':
            real_pass = input()
        user_pass.append(site)
        user_pass.append(user_name)
        user_pass.append(real_pass)
        string_pass = str(user_pass).replace(",",":")
        file_container.write(string_pass)
        file_container.write('\n')
        cont = ""
        while cont != 'N':
            print("Do you want to continue? 'N' to stop")
            cont = input()
            if cont == "N":
                break
            else:
                add()
                return user_pass 
def search_pass():
    file = "PATH_TO_FILE"
    with open(file,"r") as file_container:
        pass_lines = file_container.readlines()
        char_removed = "[]''"
        target_site = ""
        new_str_site = ""
        while target_site != "N":
            print("What service information would you like to see?'N' to exit")
            target_site = input()
            for site in pass_lines:
                if target_site in site:
                    new_str_site += site
                    for char in char_removed:
                        new_str_site = new_str_site.replace(char," ")
                    print(new_str_site)
                    return new_str_site
            print("Sorry the service/site you have entered does not exist, try again") 
    
passManager()

