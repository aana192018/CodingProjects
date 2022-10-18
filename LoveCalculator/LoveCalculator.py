# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
count_L= 0
count_O = 0
count_V = 0
count_E = 0
count_T = 0
count_R = 0
count_U = 0
name1 = name1.upper()
for singleLetter in name1:
  if singleLetter == "L":
    count_L = count_L+1
  elif singleLetter == "O":
    count_O = count_O+1
  elif singleLetter == "V":
    count_V = count_V+1
  elif singleLetter == "E":
    count_E = count_E+1
  elif singleLetter == "T":
    count_T = count_T+1
  elif singleLetter == "R":
    count_R = count_R+1
  elif singleLetter == "U":
    count_U = count_U+1
name2 = name2.upper()
for singleLetter in name2:
  if singleLetter == "L":
    count_L = count_L+1
  elif singleLetter == "O":
    count_O = count_O+1
  elif singleLetter == "V":
    count_V = count_V+1
  elif singleLetter == "E":
    count_E = count_E+1
  elif singleLetter == "T":
    count_T = count_T+1
  elif singleLetter == "R":
    count_R = count_R+1
  elif singleLetter == "U":
    count_U = count_U+1
score = ((count_L + count_O + count_V +count_E) + (count_T + count_R + count_U + count_E)*10)
#print(str((count_L + count_O + count_V +count_E) + (count_T + count_R + count_U + count_E)*10), "/ 100") 
if score < 10 or score >90:
  print("You go together like coke and mentos! You are not a good pair.")
elif score > 40 and score < 50:
  print("You are an ok pair.")
else:
  print("You are a great pair.")