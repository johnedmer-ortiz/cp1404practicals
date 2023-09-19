def main():
    """password with error checking"""
    min_pass_len = 10
    password = input("Enter password: ")
    pass_check = error_check(password, min_pass_len)
    while pass_check == False:
        print("Password does not meet the requirements.")
        password = input("Enter password: ")
        pass_check = error_check(password, min_pass_len)
    print("*" * len(password))
def error_check(password, min_pass_len):
    """password length checker"""
    if len(password)>= min_pass_len:
        return True
    return False

main()