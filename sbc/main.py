def register():
    new_username = input("Enter your desired username: ")
    password = input("Enter your desired password: ")

    if ' ' in new_username:
        print("Username cannot contain spaces")
    else:
        with open("data.txt", "r") as file:
            usernames = [line.split()[0] for line in file.readlines() if line.strip()]  # added if line.strip() to skip empty lines

        if new_username in usernames:
            print("Username Already Used")
        else:
            with open("data.txt", "a") as file:
                print(f"{new_username} {password}", file=file)

def login():
    checku_name = input("Enter your Username: ")
    checkp_word = input("Enter your password: ")

    found = False
    with open("data.txt","r") as file:
        for line in file:
            parts = line.strip().split()
            if len(parts) == 2:  # Check if the line has exactly two parts
                username, password = parts
                if username == checku_name and password == checkp_word:
                    print("Login successful!")
                    found = True
                    while True:
                        print("1. Change password")
                        print("2. Logout")
                        choice = input("Enter your choice: ")
                        if choice == "1":
                            new_password = input("Enter your new password: ")
                            changepass(username, password, new_password)
                            print("Password changed successfully!")
                        elif choice == "2":
                            print("Logged out")
                            return
                        else:
                            print("Invalid choice. Try again!")
                    return
    if not found:
        print("Invalid username or password. Try again!")

def changepass(username, old_password, new_password):
    with open("data.txt", "r+") as file:
        lines = file.readlines()
        file.seek(0)  # move the file pointer to the beginning of the file
        found = False
        for line in lines:
            parts = line.strip().split()
            if len(parts) >= 2 and parts[0] == username and parts[1] == old_password:
                file.write(f"{username} {new_password}\n")
                found = True
            else:
                file.write(line)
        file.truncate()  # remove any remaining characters in the file
        if not found:
            print("Username or password is incorrect")
        else:
            print("Password changed successfully")
while True:
    print("Choose if you want to Register or Login")
    print("1. For Login")
    print("2. For Register")
    print("3. To exit")
    choose = int(input("Please Choose: "))

    if choose == 1:
        login()
    elif choose == 2:
        register()
    elif choose == 3:
        break