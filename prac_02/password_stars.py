
def main():
    """checks if user's password meets the length requirement"""
    pass_limit = 10 # minimum number of characters
    password = get_password()
    pass_len = len(password)
    while pass_len < pass_limit:
        print("Password does not meet the requirements.")
        get_password()
    print("*" * pass_len)

def get_password():
    """returns password from user input"""
    password = input("Enter password: ")
    return password

main()