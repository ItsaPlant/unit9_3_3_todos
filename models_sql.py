import sql_data

class Todos:
    def __init__(self):
        self.conn = sql_data.create_connection()
        conn = sql_data.create_connection()
        table = "project"
        self.table = table
        self.todos = sql_data.select_all(conn, table)

    def all(self):
        return self.todos

    def get(self, id):
        return sql_data.select_where(self.conn, self.table, querry=id)
    
    def create(self, data):
        data.pop('csrf_token')
        sql_data.add_project(self.conn, self.table, data)

    def save_all(self):
        pass
    
    def update(self, id, data):
        pass

todos = Todos()