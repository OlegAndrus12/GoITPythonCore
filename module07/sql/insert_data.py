from faker import Faker

from random import randint

from connection import create_connection

fake = Faker()

if __name__ == '__main__':
    sql_insert_users_table = "INSERT INTO users(name,email,password, age) VALUES(?, ?, ?, ?)"

    with create_connection() as conn:
        if conn is not None:
            cur = conn.cursor()
            for _ in range(50000):
                cur.execute(sql_insert_users_table, (fake.name(), fake.email(), fake.password(), randint(11, 89)))
            cur.close()
        else:
            print('Error: can\'t create the database connection')
