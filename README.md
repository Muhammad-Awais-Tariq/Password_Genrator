# Password Generator (Terminal Based)
A simple terminal-based password generator built using Python. This program allows users to create secure passwords based on their preferences such as length, inclusion of digits, and special characters.

## Features
- Generate random passwords of custom length
- Option to include:
  - Digits (0–9)
  - Special characters (!, @, #, etc.)
- Input validation for password length
- Simple and interactive terminal interface
- Uses built-in Python libraries for randomness and character sets

## How the Program Works
- The program starts by asking the user to enter:
  - Minimum password length
  - Whether to include digits
  - Whether to include special characters
- Based on user input:
  - A pool of characters is created (letters, digits, symbols)
- The program randomly selects characters from this pool
- A password is generated and displayed to the user

## How to Run the Program
1. Make sure **Python** is installed.
2. Run the program:
```bash
python main.py
```

## File Structure
```bash
project/
│── main.py
│── README.md
```

## Technologies Used
- Python
- random (for generating random characters)
- string (for predefined character sets like letters, digits, symbols)

## Notes
- Password length must be a valid number.
- If both digits and special characters are disabled, the password will contain only letters.
-The randomness is based on Python’s pseudo-random generator.
- You can improve the program by ensuring at least one digit or special character when selected.

## Author
Muhammad Awais Tariq

If you like this project, consider giving it a star on GitHub!