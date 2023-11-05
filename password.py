import random
lower_char="abcdefghijklmnopqrstuvwxyz"
upper_char="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
num="0123456789"
special_symbol="!@#$%^&*."
lib=lower_char+upper_char+num+special_symbol
length=int(input("enter length"))
password=""


for a in range(length):
    password+=random.choice(lib)
print(password)
