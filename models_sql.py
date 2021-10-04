import sql_data

class Todos:
    def __init__(self, sql_data):
        self.sql_data = sql_data
        self.db_file = "database.db"
        self.conn = sql_data.create_connection(self.db_file)
        self.table = "project"

    def all(self):
        todos = sql_data.select_all(self.conn, self.table)
        return todos

    def get(self, id):
        return sql_data.select_where(self.conn, self.table, querry=id)
    
    def create(self, data):
        data.pop('csrf_token')
        sql_data.add_project(self.conn, self.table, data)

    def save_all(self):
        pass
    
    def update(self, id, data):
        pass

todos = Todos(sql_data)