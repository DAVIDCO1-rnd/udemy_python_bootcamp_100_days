#student_heights = input("Input a list of student heights ").split()
student_heights = [4, 5, 7, 6]
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
sum_heights = 0
for single_height in student_heights:
  sum_heights = sum_heights + single_height
sum_heights1 = sum(student_heights)
max_height = max(student_heights)

num_of_students = len(student_heights)
avg_heights = sum_heights / num_of_students

print(student_heights)
print("max_height ", max_height);
print("sum_heights ", sum_heights);
print("sum_heights1 ", sum_heights1);
print("num_of_students = ", num_of_students)
print("avg_heights = ", avg_heights)