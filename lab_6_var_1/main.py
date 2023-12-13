"""
Написать функцию, которая принимает наименование
таблицы, поля и его значение и возвращает идентификатор за-
писи, в которой значение полученного поля соответствует пе-
реданному функции, или возвращает None.
"""
import sqlite3


def create_table(table_name: str) -> None:
    con = sqlite3.connect("sql.db")
    with con:
        con.execute(f"""
            CREATE TABLE IF NOT EXISTS {table_name}   (
               id INTEGER PRIMARY KEY,
               product VARCHAR(20),
               count INTEGER,
               price INTEGER
    );
        """)
    con.close()

def insert_data(table_name: str) -> None:
    try:
        con = sqlite3.connect("sql.db")
        sql = f'INSERT INTO {table_name} (id,product, count, price) values(?, ?, ?, ?)'
        # указываем данные для запроса
        data = [
            (1, 'водка', 2, 3000),
            (2, 'сок', 5, 1000),
            (3, 'газировка', 1, 500)
        ]

        # добавляем с помощью множественного запроса все данные сразу
        with con:
            con.executemany(sql, data)

        con.close()
    except Exception:
        print(Exception)

def get_data(table_name, field, value):
    con = sqlite3.connect("sql.db")
    cur = con.cursor()
    cur.execute(f"SELECT * FROM {table_name} WHERE {field} = '{value}'")
    result = cur.fetchone()
    return result
    con.close()

def operate_db():
    create_table("goods")
    insert_data("goods")
    print(get_data("goods", "product", "водка"))


if __name__ == "__main__":
    operate_db()
