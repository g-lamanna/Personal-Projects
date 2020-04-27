import json
file = "$PATH_TO_FILE"
print('''
    *******Master Password Manager*******
    Please Enter Your Password to Continue....
    ''')
userPass = input()

def master():
    masterPass = 'xxxx'
    if userPass == masterPass:
        password_introduction()
def password_introduction():
    print('''
        ***** What would you like to do? ******
        -(A)dd new password and username
        -(S)earch passwords by service
        -Editing option available here
        -(R)andom password
        -(V)iew all credentials
        -(Q)uit
        ''')
    user_answer = input()
    if user_answer == "R":
        random_password_generator()
    elif user_answer == "A":
        add()
    elif user_answer =="S":
        search_pass()
    elif user_answer =="V":
        expand_file()
    elif user_answer =="Q":
        exit()
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
    with open(file, 'r+') as f:
        data = json.load(f)
        service = input("Enter Service ")
        username = input("Enter Username ")
        rando = input("Would you like to randomize password?" )
        if rando == "yes":
            password = random_password_generator()
        elif rando == "no":
            password = input("Enter Password ")
        vals=[]
        vals.append(username)
        vals.append(password)
        data[service] = vals # <--- add `service` value.
        f.seek(0)        # <--- should reset file position to the beginning.
        json.dump(data, f, indent=4)
        f.truncate()
        quitt = input("'N' to quit")
        if quitt =="N":
            exit()
        else:
            master()
def search_pass():
    with open(file,"r+") as fp:
        data = json.load(fp)
        user = input("What service do you wish to find? ")
        for i in data:
            if user in i:
                print(i,data[i])
        edit_req = input("Edit? ")
        if edit_req == "Y":
            new_data = data.get(i,"")
            print("[Username,Password]")
            print(new_data)
            user_or_pass = input("Edit username or password?")
            if user_or_pass == "user":
                new_user = input("New Username: ")
                new_data[0] = new_user
                data[i] = new_data
                print("Success! Password changed")
                fp.seek(0)        # <--- should reset file position to the beginning.
                json.dump(data, fp, indent=2)
                fp.truncate()
            elif user_or_pass == "pass":
                new_user = input("New Password: ")
                new_data[1] = new_user
                data[i] = new_data
                print("Success! Password changed")
                fp.seek(0)        # <--- should reset file position to the beginning.
                json.dump(data, fp, indent=2)
                fp.truncate()
        else:
            exit()
def expand_file():
    with open(file) as file_container:
        print(file_container.read())
master()


