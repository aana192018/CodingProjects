rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

uscho = input("What would you like to choose? Type 0 for Rock, type 1 for Paper, and type 2 for Scissors.\n")
if uscho == "0":
  print(rock)
elif uscho == "1":
  print(paper)
elif uscho == "2":
  print(scissors)

  
import random
comcho = random.randint(0,2)
print("\nThe computer chose: " + str(comcho))
if comcho == 0:
  print(rock)
elif comcho == 1:
  print (paper)
elif comcho == 2:
  print (scissors)


if uscho == "0" and comcho == 1:
  print("You lose!")
elif uscho == "1" and comcho == 2:
  print("You lose!")
elif uscho == "2" and comcho == 0:
  print("You lose!")
elif uscho == "1" and comcho == 0:
  print("You won!")
elif uscho == "2" and comcho == 1:
  print("You won!")
elif uscho == "0" and comcho == 2:
  print("You won!")
elif uscho == "0" and comcho == 0:
  print("It is a tie! Let's try again")
elif uscho == "1" and comcho == 1:
  print("It is a tie! Let's try again")
elif uscho == "2" and comcho == 2:
  print("It is a tie! Let's try again")
