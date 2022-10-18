# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

week = (90 * 52 - int(age) * 52)
day = (90 * 365 - int(age) * 365)
month = (90 * 12 - int(age) *12)

print("You have " + str(week) + " weeks, " + str(day) + " days, and " + str(month) + " months left in your life.")