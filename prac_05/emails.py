"""
CP1404 - prac_05 - email dictionary
"""


def main():
    """Main function"""
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        email_to_name[email] = extract_name(email)
        email = input("Email: ")
    display_emails(email_to_name)


def extract_name(email):
    """Extracts names from email or user input"""
    name = email.split("@")[0]
    check_name = input(f"Is your name {name}? (Y/N)").upper()
    if check_name == "" or check_name == "Y" or check_name == "YES":
        return name
    else:
        return input("Name:")


def display_emails(email_to_name):
    """Lists all names and corresponding email addresses"""
    print("")
    for email, name in email_to_name.items():
        print(f"{name} ({email})")


main()
