def calculate_grade(percentage):
    """Determine grade based on percentage"""
    if percentage >= 90:
        return 'A'
    elif percentage >= 80:
        return 'B'
    elif percentage >= 70:
        return 'C'
    elif percentage >= 60:
        return 'D'
    else:
        return 'F'

def get_student_marks():
    """Get student name and marks for 5 subjects"""
    name = input("Enter student's name: ").strip()
    
    marks = []
    for i in range(1, 6):
        while True:
            try:
                mark = float(input(f"Enter marks for subject {i} (0-100): "))
                if 0 <= mark <= 100:
                    marks.append(mark)
                    break
                else:
                    print("Marks should be between 0 and 100. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")
    
    return name, marks

def main_task1():
    print("=" * 40)
    print("STUDENT GRADE CALCULATOR")
    print("=" * 40)
    
    name, marks = get_student_marks()
    total = sum(marks)
    percentage = (total / 500) * 100
    grade = calculate_grade(percentage)
    
    print("\n" + "=" * 40)
    print("RESULTS")
    print("=" * 40)
    print(f"Student Name: {name}")
    print(f"Total Marks: {total}/500")
    print(f"Percentage: {percentage:.2f}%")
    print(f"Grade: {grade}")
    print("=" * 40)

if __name__ == "__main__":
    main_task1()