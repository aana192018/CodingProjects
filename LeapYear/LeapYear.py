# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

if float(year) % 4 == 0:
  if float(year) % 100 >= 1:
    print("This year is a leap year.")
  else:
    if float(year) % 400 == 0:
      print("This is a leap year.")
    else:
      print("This is not a leap year.")
else:
  print("This is not a leap year.")