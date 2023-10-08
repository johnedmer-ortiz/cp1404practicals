def main():
    """Main function"""
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        email_to_name[email] = extract_name(email)
        email = input("Email: ")


def extract_name(email):
    name = email.split("@")[0]
    check_name = input(f"Is your name {name}? (Y/N)").upper()
    if check_name == "" or check_name == "Y" or "YES":
        return name
    else:
        return input("Name:")


main()
