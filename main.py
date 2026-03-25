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

    return password

def get_info():
    while True:
        try:
            min_len = int(input("Enter the minimum length of password that you need: "))
            break
        except ValueError:
            print("Please enter the number")
    want_digits = True if input("Want digits (Y /N): ").lower() == "y" else False
    want_special = True if input("Want special chracters (Y /N): ").lower() == "y" else False
    password = generate_password(min_len , want_digits , want_special)

    print(f"Password: {password}")
def main():
    get_info()

if __name__ == "__main__":
    main()