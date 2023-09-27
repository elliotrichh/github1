# Hashed passwords
hashed_passwords = [
    '5f4dcc3b5aa765d61d8327deb882cf99',  # 'password'
    '098f6bcd4621d373cade4e832627b4f6',  # 'test'
    '5994471abb01112afcc18159f6cc74b4',  # '123456'
    '098f6bcd4621d373cade4e832627b4f6',  # 'test'
    'ea2710a74d97d39b0e8780119c60d82a',  # 'secret'
]

def check_password(input_password):
    hashed_input = input_password
    if hashed_input in hashed_passwords:
        print("Correct")
    else:
        print("Incorrect")

# get the user input
user_input = input("Enter the hashed password to check: ")

check_password(user_input)
