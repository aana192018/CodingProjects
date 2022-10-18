# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
#print(type(position))

p_row = position[0]
p_cln = position[1]
if p_row == "1":
  row1[int(p_cln)-1] = "X"
elif p_row == "2":
  row2[int(p_cln)-1] = "X"
elif p_row == "3":
  row3[int(p_cln)-1] = "X"

#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")
