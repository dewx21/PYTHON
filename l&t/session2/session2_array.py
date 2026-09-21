# Follow-up questions to start with
# write a script to create a employee id from 1001 to 2000 with numpy array
# write a python script to generate 60 students random marks between 33 to 100
import numpy as np


# Create employee IDs from 1001 through 2000.
employee_ids = np.arange(1001, 2001)

# Generate random marks for 60 students, inclusive of 33 and 100.
student_marks = np.random.randint(33, 101, size=60)
student_marks_2d = np.resize(student_marks, (6, 10))
student_marks_3d = np.resize(student_marks, (3, 5, 4))

print("Employee IDs:", employee_ids)
print("Student marks:", student_marks)
print("Student marks (2-D):\n", student_marks_2d)
print("Student marks (3-D):\n", student_marks_3d)

print("Student marks (2-D) only first row:", student_marks_2d[0,0]) #printing just an element of the array

print("Student marks (2-D), selected columns:\n", student_marks_2d[0, :2], "\n", student_marks_2d[1, :3], "\n", student_marks_2d[2, :4]) # two columns from the first row, three from the second, and four from the third

print("Alternative rows:\n", student_marks_2d[::2])
print("Alternative columns:\n", student_marks_2d[:, ::2])
print("Second to end row and column is 3rd till end for all row:\n", student_marks_2d[2:, 3:])

# Sum of all student marks.
print("Sum:", student_marks_2d.sum())
# Average of all student marks.
print("Mean:", student_marks_2d.mean())
# How far the marks typically vary from the mean.
print("Standard deviation:", student_marks_2d.std())
# The squared measure of variation in the marks.
print("Variance:", student_marks_2d.var())
# The value below which 25% of the marks fall.
print("25th percentile:", np.quantile(student_marks_2d, 0.25))
# The value below which 50% of the marks fall.
print("50th percentile:", np.quantile(student_marks_2d, 0.50))

print("Median:", np.median(student_marks_2d)) #median is found using this
print("Seed:", np.random.seed(42)) #generates the same random value of the array for everyone

