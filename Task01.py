# taking student name and marks
name = input("Enter student name: ")

# taking marks in 5 subjects
s1 = int(input("Enter marks in subject 1: "))
s2 = int(input("Enter marks in subject 2: "))
s3 = int(input("Enter marks in subject 3: "))
s4 = int(input("Enter marks in subject 4: "))
s5 = int(input("Enter marks in subject 5: "))

# calculating total
total = s1 + s2 + s3 + s4 + s5

# calculating percentage
percent = (total / 500) * 100

# printing total and percentage
print("\nStudent Name:", name)
print("Total Marks:", total)
print("Percentage:", percent, "%")

# checking grade using if-elif-else
if percent >= 90:
    print("Grade: A")
elif percent >= 80:
    print("Grade: B")
elif percent >= 70:
    print("Grade: C")
elif percent >= 60:
    print("Grade: D")
else:
    print("Grade: F")