import json

from .models import Student


def load_students(filepath: str) -> list[Student]:
    with open(filepath, "r", encoding="utf-8") as file:
        data = json.load(file)

    return [
        Student(student["name"], student["scores"])
        for student in data
    ]