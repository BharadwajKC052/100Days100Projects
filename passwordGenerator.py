import random as r

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k','l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = [0,1,2,3,4,5,6,7,8,9]
symbols = ['!', '@', '#', '$', '%', '&', '^', '&', '*']

# Password Generator
no_Letters = int(input("How many letters do you want in your password :"))
no_numbers = int(input("How many numbers do you want in your password :"))
no_symbols = int(input("How many symbols do you want in your password :"))

#Easy Level Password
# Password =""

# for letr in range(1,no_Letters+1):
#     Password+=r.choice(letters)
   
# print(Password)

# for symnb in range(1,no_symbols+1):
#     Password+=r.choice(symbols)

# print(Password)

# for numb in range(1,no_numbers+1):
#     Password+=str(r.choice(numbers))

# print(Password)

#Hard Level
PasswordL =[]

for letr in range(1,no_Letters+1):
    PasswordL.append(r.choice(letters))
   
# print(PasswordL)

for symnb in range(1,no_symbols+1):
    PasswordL.append(r.choice(symbols))

# print(PasswordL)

for numb in range(1,no_numbers+1):
    PasswordL.append(str(r.choice(numbers)))
# print(PasswordL)
r.shuffle(PasswordL)
finalpass=""
for puss in PasswordL:
    finalpass+=puss

print(f"Your Password is {finalpass}")
