# Student Grade Tracker
# Python 3.10+ compatible

def get_valid_score():
    """Prompt user for a valid score between 0 and 100."""
    while True:
        try:
            score = float(input("Enter score (0-100): "))
            if 0 <= score <= 100:
                return score
            else:
                print("❌ Score must be between 0 and 100.")
        except ValueError:
            print("❌ Invalid input. Please enter a number.")

def calculate_grade(score):
    """Return letter grade based on score."""
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

def main():
    print("📚 Student Grade Tracker")
    students = {}

    while True:
        name = input("\nEnter student name (or 'done' to finish): ").strip()
        if name.lower() == "done":
            break
        if not name:
            print("❌ Name cannot be empty.")
            continue

        score = get_valid_score()
        grade = calculate_grade(score)
        students[name] = {"score": score, "grade": grade}
        print(f"✅ {name} scored {score} and got grade '{grade}'.")

    # Display all results
    if students:
        print("\n📊 Final Results:")
        for student, data in students.items():
            print(f"{student}: Score = {data['score']}, Grade = {data['grade']}")
    else:
        print("\nNo student data entered.")

if __name__ == "__main__":
    main()
