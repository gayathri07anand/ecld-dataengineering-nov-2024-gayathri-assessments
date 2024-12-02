def password_validation(password):
    
    if len(password) < 6 or len(password) > 24:
        return "False,Too short, Password should contain characters between 6 and 24."

    
    if not any(i.isupper() for i in password):
        return "False, Password should contain atleast one uppercase letter."

    
    if not any(i.islower() for i in password):
        return "False, Password should contain atleast one lowercase letter."

    
    if not any(i.isdigit() for i in password):
        return "False, missing a number."

    
    for j in range(len(password) - 2):
        if password[j] == password[j + 1] == password[j + 2]:
            return "False, Password cannot have more than 2 consecutive repeated characters."

    
    special_characters= "!@#$%^&*()+=_-{}[]:;\"'?<>,."
    if not all(i.isalnum() or i in special_characters for i in password):
        return "False, Password contains invalid special characters."

    return "Password is valid."
user_password = input("Enter a password to validate: ")
validatoion = password_validation(user_password)
print(validatoion)

# Test cases
"""print(password_validation("P1zz@")) ## False Too short.

print(password_validation("iLoveYou")) ##False Missing a number.

print(password_validation("Fhg93@"))## Password is valid"""
