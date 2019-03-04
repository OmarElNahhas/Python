import random


# making a random string for your password
def generate_password():
    array1 = []
    i = 0
    # the while loop runs for a random number between 5 and 20 including 20
    # Every loop it will add 1 number and 1 letter/character.
    while i <= random.randrange(5, 20):
        array1.append(random.randrange(0, 10))
        # not all sites accept passwords with special characters in it
        array1.append(random.choice(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 'X', 'Z', '!', '@', '%', '*', '&', '^', '$', '#', '=', '+', '>', '<']))
        i +=1
    return "".join(map(str, array1))


# adding your password to filename so you won't forget it
def save_password(password, username, website, filename):
    # "a" means append to the file. The "+" will create the file if it isn't found.
    password_file = open(filename, "a+")
    password_file.write("\nWebsite: ")
    password_file.write(website.lower())
    password_file.write("\nUsername: ")
    password_file.write(username)
    password_file.write("\nPassword: ")
    password_file.write(password.upper())
    password_file.write("\n")
    password_file.close()


if __name__ == "__main__":
    website = str(input(("For which website do you need a password?: " )))
    username = str(input("What username/email are you going to use?: "))
    filename = str(input("In which file do you want to save the password? (if left empty, default passwordfile.txt): "))
    if filename is "":
        filename = "passwordfile.txt"
    if "."  not in filename:
        filename = filename + ".txt"
    if website is "" or username is "":
        print("\nYou didn't give me all the information, please try again.")
        # exits the program
        exit()
    else:
        password = generate_password()
        save_password(password, username, website, filename)
        print("\nSuccess. You can find your password in:", filename)