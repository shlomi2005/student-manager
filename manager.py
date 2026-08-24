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


def add_student(students, name, grade, class_name):
    with open(students, "a", encoding="utf-8") as f:

        wrt = csv.writer(f)
        wrt.writerow([name, grade, class_name])


def find_student(students, name):

    with open(students, "r", encoding="utf-8") as f:
        a = csv.DictReader(f)
        for i in a:
            if i["name"] == name:
                return i
    return None
