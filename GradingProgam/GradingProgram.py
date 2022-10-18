student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
  "Luna": 82,
  "Ginny": 94,
  "Goyle": 50,
  "Crabe": 51,
  "Fred": 77,
  "George": 77,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.👇

for f in student_scores:
    #student_grades = (student_scores[f])
    if student_scores[f] <= 100 and student_scores[f] >= 91:
        student_grades [f] = "Outstanding"
    elif student_scores[f] <= 90 and student_scores[f] >= 81:
        student_grades [f] = "Exceeds Expectations"
    elif student_scores[f] <= 80 and student_scores[f] >= 71:
        student_grades [f] = "Acceptable"
    elif student_scores[f] <=70:
        student_grades [f] = "Fail"

      
# 🚨 Don't change the code below 👇
print(student_grades)