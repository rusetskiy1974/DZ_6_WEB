import sqlite3
import logging
from faker import Faker
import random

from table import Table
from bd_constants import STRUCTURE_BD, GROUPS, TEACHERS, STUDENTS, SUBJECTS, GRADES, SAMPLES_FROM_BD

logger = logging.getLogger()
stream_handler = logging.StreamHandler()
formatter = logging.Formatter('line_num: %(lineno)s > %(message)s')

stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)


# logger.setLevel(logging.DEBUG)


def main():
    project_tables = []
    with sqlite3.connect("dz_6.sqlite") as conn:
        Table.conn = conn
        for table_name, columns in STRUCTURE_BD.items():
            new_table = Table(table_name, *columns)
            project_tables.append(new_table)

        fake = Faker('uk_UA')

        # Додавання груп
        for group_name in GROUPS:
            project_tables[0].create({"name": group_name})

        # Додавання викладачів
        for _ in range(1, TEACHERS + 1):
            project_tables[1].create({"fullname": fake.name()})

        # Додавання предметів
        for subject in SUBJECTS:
            teacher_id_fn = random.randint(1, TEACHERS)
            project_tables[2].create({"name": subject, "teacher_id_fn": teacher_id_fn})

        # Додавання студентів
        for _ in range(1, STUDENTS + 1):
            group_id_fn = random.randint(1, len(GROUPS))
            project_tables[3].create({"fullname": fake.name(), "group_id_fn": group_id_fn})

        # Заповнюємо оцінки
        for student_id_fn in range(1, STUDENTS + 1):
            for _ in range(1, GRADES):
                subject_id_fn = random.randint(1, len(SUBJECTS))
                grade = random.randint(60, 100)
                project_tables[4].create(
                    {"student_id_fn": student_id_fn, "subject_id_fn": subject_id_fn, "grade": grade,
                     "grade_date": fake.date_this_year()})

        print(SAMPLES_FROM_BD)
        while True:

            try:
                query_number = int(input('Ваш вибір :'))
            except:
                print('Хибне значення')
                continue
            if query_number in range(1, 13):

                with open(f"query/query_{query_number}.sql", 'r') as fd:
                    sample = fd.read()
                    cur = Table.conn.cursor()
                    cur.execute(sample)
                    rows = cur.fetchall()
                    [print(row) for row in rows]

            elif query_number == 0:
                cur.close()
                Table.conn.close()
                break
            else:
                print('Хибне значення')


if __name__ == "__main__":
    main()
