import re

class CredentialValidator:
    # Updated email pattern to be more flexible
    email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    password_pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%#?&])[A-Za-z\d@$!%#?&]{8,}$"

    @staticmethod
    def validate_email(email):
        return bool(re.match(CredentialValidator.email_pattern, email))

    @staticmethod
    def validate_password(password):
        return bool(re.match(CredentialValidator.password_pattern, password))

# Loop until valid email
while True:
    user_email = input("Enter your email: ")
    if CredentialValidator.validate_email(user_email):
        print("Valid email")
        break
    else:
        print("Invalid email. Try again.")

# Loop until valid password
while True:
    user_password = input("Enter your password: ")
    if CredentialValidator.validate_password(user_password):
        print("Valid password")
        break
    else:
        print("Invalid password. Must be at least 8 characters, include uppercase, lowercase, digit, and special character.")