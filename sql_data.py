import sqlite3

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.Error as e:
        print(e)
    return conn

def select_all(table, db_file):
    """
    Query all rows in the table
    :param conn: the connection obj
    :return:
    """
    with create_connection(db_file) as conn:
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM {table}")
        rows = cur.fetchall()
        data = []
        for row in rows:
            (id, nazwa, opis, status) = row
            row = {
                'title': nazwa,
                'description': opis,
                'done': status
            }
            data.append(row)
        return data

def select_where(db_file, table, **querry):#querry: id=id_number
    """
    Querry tasks from table with data from **query dict
    :param conn:
    :param table: table name
    :param query: dict of attributes and values
    :return:
    """
    with create_connection(db_file) as conn:
        cur = conn.cursor()
        qs = []
        values = ()
        for k, v in querry.items():
            qs.append(f"{k}=?")
            values += (v,)
        q = "AND".join(qs)
        cur.execute(f"SELECT * FROM {table} WHERE {q}", values)
        rows = cur.fetchall()
        rows = tuple_to_dict(rows)
        return rows

def add_project(db_file, nazwa, opis, status):
    """
    Create a new project into the project table
    :param conn:
    :param project:
    :return: project id
    """
    sql = '''INSERT INTO projects(nazwa, opis, status)
             VALUES(?,?,?)'''
    with create_connection(db_file) as conn:
        cur = conn.cursor()
        cur.execute(sql, (nazwa, opis, status))
        conn.commit()
        return cur.lastrowid

def update_sql(db_file, table, id, title, description, status): #dokończyć to, dopadować wartości do updateu
    """
    update status, begin_date, and end date of a task
    :param conn:
    :param table: table name
    :param id: row id
    :return:
    """
    # parameters = [f"{k} = ?" for k in kwargs]
    # parameters = ", ".join(parameters)
    # values = tuple(v for v in kwargs.values())
    # values += (id, )
    ###
    values = (title, description, status, (id+1),)

    # sql = f''' UPDATE {table}
    #         SET {parameters}
    #         WHERE id = ?'''

    #
    sql = f'''UPDATE {table}
            SET nazwa = ?,
            opis = ?,
            status = ?
            WHERE id = ?'''
    try:
        with create_connection(db_file) as conn:
            cur = conn.cursor()
            cur.execute(sql, values)
            conn.commit()
            print("OK")
    except sqlite3.OperationalError as e:
        print(e)

#SAVE jest niepotrzebny

#SAVE ALL jest niepotrzebny

def tuple_to_dict(tuple):
    dict_list = []
    for row in tuple:
        (id, nazwa, opis, status) = row
        row = {
            'title': nazwa,
            'description': opis,
            #'done': status
        }
        dict_list.append(row)
    return dict_list



if __name__ == "__main__":
    conn = create_connection("database.db")