import random

elementes = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
pass_l = int(input("Введите нужную длину пароля"))

password = ''
for i in range(pass_l):
    password += random.choice(elementes) 

print(password)
