#funct to calculate grade
def calculate_grade(score):
    if score >= 90:
        return 4.0
    elif score >= 80:
        return 3.0
    elif score >= 70:
        return 2.0
    elif score >= 60:
        return 1.0
    else:
        return 0.0

# Function to calculate gwa
def calculate_overall_grade(subject_scores):
    total_subjects = len(subject_scores)
    total_grade_points = sum([calculate_grade(score) for score in subject_scores])
    overall_gwa = total_grade_points / total_subjects
    return overall_gwa

subjects = [
    {"name": "Statistics", "score": 85},
    {"name": "OOP", "score": 92},
    {"name": "Algorithm", "score": 78},
    {"name": "STS", "score": 88},
    {"name": "SocScie", "score": 75},
    {"name": "Database", "score": 95},
    {"name": "PE", "score": 70}
]

subject_scores = [subject["score"] for subject in subjects]

while True:
    print("\nGrading System");
    print("See the Grade of the specific Subject (eg. press 1 for stats)")
    print("QUIT")

    choice = input("Enter your choice (1,2,3): ")

    if choice == "1":
        Sub_Name = input("Enter the subject: ")
        for subject in subjects:
            if subject["name"].lower() == Sub_Name.lower():
                score = subject["score"]
                grade = calculate_grade(score)
                print(f"the grade {Sub_Name} is {grade}")
                break

            elif choice == "2":
                overall_gwa = calculate_overall_grade(subject_scores)
                print(f"The overall GPA is {overall_gwa:.2f}")

            elif choice == "3":
                print("QUIT.")
                break

            else:
                print("Invalid choice. Please select a again.")

