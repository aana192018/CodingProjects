# Split string method
names_string = input("Give me everybody's names, separated by a comma.\n")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

import random
chosen_name = (random.choice(names))
print(chosen_name + " is going to buy the meal today!")