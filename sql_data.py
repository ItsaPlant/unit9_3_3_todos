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

def select_all(conn, table):
    """
    Query all rows in the table
    :param conn: the connection obj
    :return:
    """
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM {table}")
    rows = cur.fetchall()
    return rows

def select_where(conn, table, **querry):#querry: id=id_number
    """
    Querry tasks from table with data from **query dict
    :param conn:
    :param table: table name
    :param query: dict of attributes and values
    :return:
    """
    cur = conn.cursor()
    qs = []
    values = ()
    for k, v in querry.items():
        qs.append(f"{k}=?")
        values += (v,)
    q = "AND".join(qs)
    cur.execute(f"SELECT * FROM {table} WHERE {q}", values)
    rows = cur.fetchall()
    return rows

def add_project(conn, nazwa, opis, status):
    """
    Create a new project into the project table
    :param conn:
    :param project:
    :return: project id
    """
    sql = '''INSERT INTO projects(nazwa, start_date, end_date)
             VALUES(?,?,?)'''
    cur = conn.cursor()
    cur.execute(sql, (nazwa, opis, status))
    conn.commit()
    return cur.lastrowid

#SAVE jest niepotrzebny

#SAVE ALL jest niepotrzebny

if __name__ == "__main__":
    conn = create_connection("database.db")