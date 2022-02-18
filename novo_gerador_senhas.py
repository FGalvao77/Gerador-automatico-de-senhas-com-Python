'''
Gerador de senhas alfanumérico com 9 caracteres
'''
from random import SystemRandom, choice
from string import ascii_letters, digits, punctuation

symbols = ascii_letters + digits + punctuation
secure_random = SystemRandom()

password = ''.join(secure_random.choice(symbols) for i in range(9))

print(password)