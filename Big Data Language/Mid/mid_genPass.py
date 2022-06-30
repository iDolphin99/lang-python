import random

def genPass() : 
    alphabet = "abcdefghijklmnopqrstuvwxyz0123456789"
    password = ""
    
    for i in range(6) : 
        index = random.randrange(len(alphabet))
        password = password + alphabet[index]
    
    return password

print(genPass())
print(genPass())
print(genPass())