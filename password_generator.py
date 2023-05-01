
import random

str1 = "1234567890"

str2 = "qwertyuiopasdfghjklzxcvbnm"

str3 = str2.upper()

str4 = "!#%&*_?"

str = str1*5 + str2*5 + str3*5 + str4*5


lst = list(str)

random.shuffle(lst)

password = ''.join([random.choice(lst) for i in range(10, 25)])

print("Your password is:", password)