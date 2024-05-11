import random
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
           'n','o','p','q','r','s','t','u','v','w','x','y','z',
           'A','B','C','D','E','F','G','H','I','J','K','L','M',
           'N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
num = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','@','#','$','%','^','&','*','+','-']
print("Welcome to password Generator!!")
lett= int(input("How many letters you want in your password\n"))
numbers= int(input("How many numbers you want in your password\n"))
sym= int(input("How many symbols you want in your password\n"))
password =[]
for i in range(1,lett+1):
    char = random.choice(letters)
    password += char
for i in range(1,numbers+1):
    char = random.choice(num)
    password += char
for i in range(1,sym+1):
    char = random.choice(symbols)
    password += char
print(password)
random.shuffle(password)
print(password)
passw=""
for i in password:
    passw += i
print(passw)





