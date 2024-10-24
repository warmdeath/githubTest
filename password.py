import string
import re
import secrets
def generate(length = 8,nums = 3,special = 0, lowercase = 4,uppercase = 1):
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation
    all_chars = letters+digits+symbols
    while True:
        password = ""
        for _ in range(length):
            password += secrets.choice(all_chars)
        constraints = [
            (nums,r"\d"),
            (special,fr"[{symbols}]"),
            (lowercase,r"[a-z]"),
            (uppercase,r"[A-Z]")
        ]
        if all([constraint<=len(re.findall(pattern,password)) for constraint,pattern in constraints]):
            break
    return password

# new_password = generate()
password_list = [generate() for x in range(10)]
print('Generated passwords:', password_list)
