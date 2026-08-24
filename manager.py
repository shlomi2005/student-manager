import csv


def load_students(filename):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            return list(reader)
    except FileNotFoundError:
        return []


def save_students(filename, students):
    with open(filename, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["name", "grade", "class"])
        writer.writeheader()
        for student in students:
            writer.writerow(student)


def add_student(students, name, grade, class_name):
    students.append({"name": name, "grade": grade, "class": class_name})


def find_student(students, name):
    for student in students:
        if student["name"] == name:
            return student
    return None


def class_average(students, class_name):
    total = 0
    count = 0
    for student in students:
        if student["class"] == str(class_name):
            total += int(student["grade"])
            count += 1
    if count == 0:
        return 0
    return total / count


def top_student(students):
    if not students:
        return None
    maxi = 0
    max_name = ""
    for student in students:
        if int(student["grade"]) > maxi:
            max_name = student["name"]
            maxi = int(student["grade"])
    return max_name


def print_all(students):
    for student in students:
        print(student)


filename = r"/Users/shlomo/שבוע חדש הכנה למבחן /student-manager/students.csv"
students = load_students(filename)
print(students)

while True:
    print("\n1. הצג הכל")
    print("2. הוסף")
    print("3. חפש")
    print("4. ממוצע כיתה")
    print("5. מצטיין")
    print("6. שמור וצא")

    choice = input("בחר אפשרות: ")
    if choice == "1":
        print_all(students)
    elif choice == "2":
        name = input("שם :")
        grade = input("ציון :")
        class_name = input("כיתה: ")
        add_student(students, name, grade, class_name)
        save_students(filename, students)
        print("התלמיד נוסף ונשמר.")

    elif choice == "3":
        name = input("שם לחיפוש: ")
        result = find_student(students, name)
        if result is not None:
            print(result)
        else:
            print("השם לא נמצא")

    elif choice == "4":
        class_name = input("שם כיתה: ")
        print(f"ממוצע: {class_average(students, class_name)}")

    elif choice == "5":
        print(f"מצטיין: {top_student(students)}")

    elif choice == "6":
        save_students(filename, students)
        print("נשמר. יוצא.")
        break
    else:
        print("אפשרות לא חוקית, נסה שוב.")
