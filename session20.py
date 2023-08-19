import random
import string
def generate_secret_number():
    digits = list(string.digits)
    random.shuffle(digits)
    result = ""
    for i in range(3):
        result += digits[i]
    return result
def result(user_g, sec):
    if sec == user_g:
        return "you won"
 
    res = ""
    for i in range(len(user_g)):
        if user_g[i] == sec[i]:
            res += "Fermi, "
        elif user_g[i] in sec:
            res += "Pico, "

    if len(res) == 0:
        return "bagels"
    
    return res
secret_number = generate_secret_number()
print(secret_number)
user_guess = input("enter your guess: ")
res = result(user_guess, secret_number)
print(res)
