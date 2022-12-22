from mygroup import groupmates

def print_students(students):
    print(
        "Имя".ljust(15), "Фамилия".ljust(10), "Экзамены".ljust(30), "Оценки".ljust(20)
    )
    for student in students:
        print(
            student["name"].ljust(15),
            student["surname"].ljust(10),
            " ".join(student["exams"]).ljust(30),
            " ".join([str(i) for i in student["marks"]]).ljust(20),
        )


def filter_students_by_marks(students_data: list,  average_mark: float) -> list:
    return [student for student in students_data if (sum(student["marks"]) / len(student["marks"])) >= average_mark ]


avg_mark = float(input())

filtred_groupmates = filter_students_by_marks(groupmates, avg_mark)

print_students(filtred_groupmates)