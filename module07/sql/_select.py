from connection import create_connection

if __name__ == '__main__':
    sql_select_users_table = "SELECT * FROM users WHERE id = %s"
    sql_select_where = """
    select id, name, age
    from users
    where age > 30
    order by name, age desc
    limit 10;
    """
    select_regex = """
    SELECT name FROM users WHERE name LIKE 'Ju%' LIMIT 100;
    """
    with create_connection() as conn:
        if conn is not None:
            cur = conn.cursor()
            # cur.execute(sql_select_users_table, (4, ))
            #print(cur.fetchone())
            #cur.execute(sql_select_where)
            cur.execute(select_regex)
            print(cur.fetchall())
            cur.close()
        else:
            print('Error: can\'t create the database connection')
