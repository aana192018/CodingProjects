# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇


totalheight = 0
counter = 0
for heights in student_heights:
  totalheight = totalheight + heights
  #print(totalheight)
  counter = counter + 1
  #print (counter)
print("The average height is: " + str(round(totalheight/counter)))