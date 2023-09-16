#Цифровой гениратор паролей. Генирирует пароль состоящий только из цифр. 

import random
import string

length_password = int(input('Какой длины должен быть пароль?: '))
password = ''.join(random.sample(string.digits, length_password))
print(password)