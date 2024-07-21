import string
import re
import secrets
def generate(length = 16,nums = 1,special = 1, lowercase = 1,uppercase = 1):
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

new_password = generate()
print('Generated password:', new_password)