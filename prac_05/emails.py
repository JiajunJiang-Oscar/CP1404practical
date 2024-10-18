"""
Emails
Estimate: 30 minutes
Actual:   42 minutes

name_and_email = empty dictionary
get email
while email not equal to empty
    name = split email by "@" and replace "." to " "
    get choice for verify name
    if name == email_name
        email_name = name
    else
        get email_name
    name_and_email[email_name] = email
    get email
for email_name, email in items of name_and_email
    display email_name and email
"""

name_and_email = {}
email = input("Email: ")

while email != '':
    # replace "." to " " and split by "@"
    name = email.replace("."," ").split("@")
    choice = input(f"Is your name {name[0].title()}? (Y/N) >>> ").upper()
    if choice == "Y":
        email_name = name[0]
    else:
        email_name = input("Name: ")
    # add email_name and email to dictionary
    name_and_email[email_name]= email
    email = input("Email: ")

# display an empty line for differentiated output
print()
for email_name, email in name_and_email.items():
    print(f"{email_name} ({email})")
