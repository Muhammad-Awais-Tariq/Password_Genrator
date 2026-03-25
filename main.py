import random
import string

def generate_password(min_len , want_digits = True , want_special = True):
    letters = string.ascii_letters
    digits = string.digits
    punctuation = string.punctuation

    password = ""
    for i in range(min_len):
        if want_digits and want_special:
            password += random.choice(letters + digits + punctuation)
        elif want_digits and not want_special:
            password += random.choice(letters + digits)
        elif not want_digits and want_special:
            password += random.choice(letters + punctuation)
        else:
            password += random.choice(letters)

    print(password)
generate_password(10 , True , False)