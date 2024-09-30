import sqlite3
from datetime import datetime
from random import randint
import faker

NUMBER_TEACHERS = 5
NUMBER_STUDENTS = 30
NUMBER_SUBJECTS = 5
GRADES_PER_STUDENT = 10
fake = faker.Faker()


def generate_data():
    groups = [("Group A",), ("Group B",), ("Group C",)]
    teachers = [(fake.name(),) for _ in range(NUMBER_TEACHERS)]
    subjects = [("Mathematics", 1), ("Physics", 2), ("History", 3), ("English", 4), ("Chemistry", 5)]
    students = [(fake.name(), randint(1, len(groups))) for _ in range(NUMBER_STUDENTS)]

    grades = []
    for student_id in range(1, NUMBER_STUDENTS + 1):
        for subject_id in range(1, NUMBER_SUBJECTS + 1):
            for _ in range(GRADES_PER_STUDENT // NUMBER_SUBJECTS):  # Генеруємо оцінки для кожного студента по предметам
                grade = randint(60, 100)
                date_of = datetime(2023, randint(1, 12), randint(1, 28)).date()
                grades.append((student_id, subject_id, grade, date_of))

    return groups, teachers, subjects, students, grades


def insert_data_to_db(groups, teachers, subjects, students, grades):
    with sqlite3.connect('univ.db') as con:
        cur = con.cursor()

        sql_groups = """INSERT INTO groups(group_name) VALUES (?)"""
        cur.executemany(sql_groups, groups)

        sql_teachers = """INSERT INTO teachers(teacher_name) VALUES (?)"""
        cur.executemany(sql_teachers, teachers)

        sql_subjects = """INSERT INTO subjects(subject_name, teacher_id) VALUES (?, ?)"""
        cur.executemany(sql_subjects, subjects)

        sql_students = """INSERT INTO students(student_name, group_id) VALUES (?, ?)"""
        cur.executemany(sql_students, students)

        sql_grades = """INSERT INTO grades(student_id, subject_id, grade, date_of) VALUES (?, ?, ?, ?)"""
        cur.executemany(sql_grades, grades)

        con.commit()


if __name__ == "__main__":
    groups, teachers, subjects, students, grades = generate_data()
    insert_data_to_db(groups, teachers, subjects, students, grades)
