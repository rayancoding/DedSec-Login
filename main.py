import getpass

# Securely prompt for a password
password = getpass.getpass("Enter your password: ")

# Check the password (this is a placeholder; use a secure method in production)
if password == "Rayangsy1":
    print("Access granted")
else:
    print("Access denied")