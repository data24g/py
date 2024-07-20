name = input("Enter your name: ")
credits = []
grades = []

def input_number(prompt):
    while True:
        try:
            number = float(input(prompt))
            return number
        except ValueError:
            print("Error! Please enter a valid number.")

def calculate_gpa(grades, credits):
    tpoints = 0
    for i in range(len(grades)):
        tpoints += grades[i] * credits[i]
    return tpoints / sum(credits)

subjects = ["C#", "Python"]

for subject in subjects:
    grade = input_number(f"Enter grade for {subject}: ")
    credit = input_number(f"Enter credits for {subject}: ")
    grades.append(grade)
    credits.append(credit)

tgrades = sum(grades)
tcredits = sum(credits)
GPA = calculate_gpa(grades, credits)

print(f"Total grades of {name} is: {tgrades}")
print(f"Total credits of {name} is: {tcredits}")
print(f"GPA score: {GPA}")

with open("scorefile.txt", "w") as f:
    f.write(f"Name: {name}\n")
    f.write(f"Grade: {grades}\n")
    f.write(f"Credit: {credits}\n")
    f.write(f"GPA: {GPA}\n")