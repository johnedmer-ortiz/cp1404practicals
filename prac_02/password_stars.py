
def main():
    """checks if user's password meets the length requirement in a loop"""
    pass_limit = 10 # minimum number of characters
    password = get_password()
    pass_len = len(password)
    while pass_len < pass_limit:
        print("Password does not meet the requirements.")
        pass_len = len(get_password())
    print_asterisk(pass_len)

def get_password():
    """returns password from user input"""
    password = input("Enter password: ")
    return password

def print_asterisk(pass_len):
    """prints number of asterisks according to the number of password characters"""
    print("*" * pass_len)

main()