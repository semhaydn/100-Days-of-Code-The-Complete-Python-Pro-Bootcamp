# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇

total = 0
student_amount = 0

for item in student_heights:
    total += item
    student_amount += 1

avarage = total / student_amount

print(round(avarage))

  

  