import csv


def load_students(filename):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            a = csv.DictReader(f)
            c = ""
            for i in a:
                c += str(i) + "\n"
            return c
    except FileNotFoundError:
        return []


b = load_students(
    r"/Users/shlomo/שבוע חדש הכנה למבחן /student-manager/students.csv")
print(b)
