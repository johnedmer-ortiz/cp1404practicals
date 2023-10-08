def main():
    """Main function"""
    email = input("Email: ")
    while email != "":
        extract_name(email)
        email = input("Email: ")

def extract_name(email):
    name = email.split("@")[0]
    check_name = input(f"Is your name {name}? (Y/N)")

main()