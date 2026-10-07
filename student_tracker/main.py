from student_tracker import load_students


def main() -> None:
    try:
        students = load_students("students.json")

        for student in students:
            print(f"{student.name}: {student.average:.2f}")

    except FileNotFoundError:
        print("Error: students.json file was not found.")

    except ValueError:
        print("Error: Invalid JSON data.")

    except KeyError as error:
        print(f"Error: Missing field {error}.")


if __name__ == "__main__":
    main()