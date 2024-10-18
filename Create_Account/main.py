begining = input("Hey there. Do you want to make an account? ")

account = []

def create_account():
    username = input("Create your username: ")
    password = input("Create your password: ")

    account.append(username)
    account.append(password)

    print("Your account was successfuly created✅")
    login_answer = input("Do you want try to log in? ")

    if login_answer.lower() == "yes":
        login_username = input("Enetr your username: ")
        login_password = input("Enetr your password: ")

        if login_username and login_password in account:
            print("Welcome to your account!")
        else:
            print("Invalid try again. Check your username or password!")

    return "Have a good day."
    

if begining.lower() == "yes":
    create_acc = create_account()
    print(create_acc)

elif begining.lower() == "no":
    confirm = input("Are you sure you don't want to make an account? ")

    if confirm.lower() == "yes":
        print("Okay than have a good day.")

    if confirm.lower() == "no":
        question = input("Do you want to make an account? ")

        if question.lower() == "yes":
            create_acc = create_account()
            print(create_acc)

        if question.lower() == "no":
            print("Okay than have a good day.")

else:
    print("Okay than have a good day.")