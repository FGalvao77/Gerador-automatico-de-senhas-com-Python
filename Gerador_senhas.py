import string 
import random

all_characters: str = (
    string.ascii_lowercase + 
    string.ascii_uppercase +
    string.digits #+ 
    #string.punctuation
)

password_list: list = random.sample(all_characters, 6)
password: str = ''.join(password_list)

print(f'The password you generated is: {password}')
