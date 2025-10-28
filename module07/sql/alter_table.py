from connection import create_connection

if __name__ == '__main__':
    alter_users_table = "alter table users add column phone varchar(30);"

    with create_connection() as conn:
        if conn is not None:
            cur = conn.cursor()
            cur.execute(alter_users_table)
            cur.close()
        else:
            print('Error: can\'t create the database connection')
