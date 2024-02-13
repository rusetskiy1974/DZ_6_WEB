import sqlite3
import logging


class Table:
    conn: sqlite3.Connection = None

    def __init__(
            self,
            table_name: str,
            columns: dict,
            constrains: list[str]
    ) -> None:

        self.columns = columns
        self.table_name = table_name
        self.constrains = constrains

        full_columns = [f"{key} {val}" for key, val in columns.items()]
        full_columns.extend(constrains)

        temp = (", ").join(full_columns)

        sql_request_0 = f"drop table if exists {table_name};"
        logging.debug(sql_request_0)

        sql_request = f"CREATE TABLE IF NOT EXISTS {table_name} ({temp});"
        logging.debug(sql_request)
        c = self.conn.cursor()
        try:
            c.execute(sql_request_0)
            c.execute(sql_request)
            self.conn.commit()
        except sqlite3.Error as e:
            print(e)
        finally:
            c.close()

    def create(self, cur, obj_dict: dict) -> int | None:
        table_columns = (",").join(obj_dict.keys())
        table_questions = (",").join("?" for _ in obj_dict.keys())

        sql_request = f'INSERT INTO {self.table_name}({table_columns}) VALUES({table_questions});'

        logging.debug(sql_request)
        logging.debug(list(obj_dict.values()))

        try:
            cur.execute(sql_request, list(obj_dict.values()))
        except sqlite3.Error as e:
            print(e)
        return cur.lastrowid

