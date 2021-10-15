import random
digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
chars = ''

amount_pass = int(input('Укажите количество паролей для генерации:'))
len_pass = int(input('Укажите длину одного пароля:'))
digit_pass = input('Включать ли цифры 0123456789? Yes, no').strip()
upp_pass = input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? Yes, no').strip()
low_pass = input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? Yes, no').strip()
sym_pass = input('Включать ли символы !#$%&*+-=?@^_? Yes, no').strip()
del_sym_pass = input('Исключать ли неоднозначные символы il1Lo0O? Yes, no').strip()

if digit_pass.lower() == 'yes':
    chars += digits
if upp_pass.lower() == 'yes':
    chars += uppercase_letters
if low_pass.lower() == 'yes':
    chars += lowercase_letters
if sym_pass.lower() == 'yes':
    chars += punctuation
if del_sym_pass.lower() == 'no':
    for i in 'il1Lo0O':
        chars = chars.replace(i, '')

def generate_password(len_pass, chars):
    password = ''
    for _ in range(len_pass):
        password += random.choice(chars)
    print(password)
for _ in range(amount_pass):
    generate_password(len_pass, chars)
