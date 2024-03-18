import random
latters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = ['1','2','3','4','5','6','7','8','9','0']
symbols = ['!','@','#','$','%','^','&','*','(',')','=','+']

print("Welcome to Mypassword Generator !\n")
nr_latters = int(input("How many latter would you like in your password : "))
nr_number = int(input("How many numbers would you like : "))
nr_symbol = int(input("How many symbols would you like : "))

# password = ""
# # Easy way 
# for i in range(1, nr_latters + 1):
#     password = password + random.choice(latters)  #String concatnation

# for i in range(1, nr_number + 1):
#     password = password + random.choice(numbers) 

# for i in range(1, nr_symbol + 1):
#     password = password + random.choice(symbols)

# print(f"Generated password is {password}") 

# Hard way 
password_list = []
for i in range(1, nr_latters + 1):
    password_list.append(random.choice(latters))  #String concatnation

for i in range(1, nr_number + 1):
    password_list.append(random.choice(numbers)) 

for i in range(1, nr_symbol + 1):
    password_list.append(random.choice(symbols))

print(f"Generated password is {password_list}") 
random.shuffle(password_list)
print(f"Generated password is {password_list}") 
password = ""
for char in password_list:
    password += char
print(f"Generated password is {password}") 
