student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
sum_heights = 0
for single_height in student_heights:
  sum_heights = sum_heights + single_height

num_of_students = len(student_heights)
avg_heights = sum_heights / num_of_students

print(student_heights)
print("num_of_students = ", num_of_students)
print("avg_heights = ", avg_heights)