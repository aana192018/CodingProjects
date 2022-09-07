# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#kg/m^2  weight = 85  height = 1.75 , slightover

bmi = round(float(weight)/(float(height)*float(height)))
if float(bmi) <= 18.5:
  print("You are underweight.")
elif float(bmi) <= 25:
  print("You have a normal weight.")
elif float(bmi) <= 30:
  print("You are slightly overweight.")
elif float(bmi) <= 35:
  print("You are obese.")
elif float(bmi) >= 35:
  print("You are clinically obese.")