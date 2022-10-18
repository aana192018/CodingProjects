print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
userselec1 = input("Would you like to go right or left? To go right, type right and to go left type left.\n")
if userselec1 == "left":
  userselec2 = input("You have reached a lake. There is a small island in the center. To reach the island you can either swim or wait for a boat. To wait for a boat, type boat. To swim across the lake, type swim.\n")
  if userselec2 == "boat":
    userselec3 = input("You have reached the island. There is an old building that you can enter. You go through the main gates but reach 3 doors that are yellow, red, and blue. Type red to go through the red door, type yellow to go throught the yellow door, type blue to go through the blue door.\n")
    if userselec3 == "yellow":
      print("You have reached the treasure! Great job! The money is all yours!\n")
    elif userselec3 == "blue":
      print("This door leads to a wall of fire. You died. Sorry for your loss.\n")
    elif userselec3 == "red":
      print("This door leads to a swarm of mosquitoes. You died. Sorry for your loss.\n")
  elif userselec2 == "swim":
    print("You died. A hungry shark saw you swimming towards him. Sorry for your loss.")
elif userselec1 == "right":
  print("You died by falling into a deep hole. Sorry for your loss.")