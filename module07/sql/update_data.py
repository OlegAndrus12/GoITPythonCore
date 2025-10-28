from faker import Faker
from connection import create_connection

fake = Faker()

if __name__ == '__main__':
    update_users_table = "UPDATE users SET phone = ? WHERE id = ?"

    with create_connection() as conn:
        if conn is not None:
            cur = conn.cursor()
            for i in range(1, 50000):
                cur.execute(update_users_table, (fake.phone_number(), i))
            cur.close()
        else:
            print('Error: can\'t create the database connection')
