from .models import Student


def print_student_report(students: list[Student]) -> None:
    for student in students:
        print(f"{student.name}: {student.average:.2f}")