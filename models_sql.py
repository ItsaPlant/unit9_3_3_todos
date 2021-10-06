import sql_data

class Todos:
    def __init__(self, sql_data):
        self.sql_data = sql_data
        self.db_file = "database.db"
        self.conn = self.sql_data.create_connection(self.db_file)

        self.table = "projects"

    def all(self):
        todos = sql_data.select_all(self.table, self.db_file)
        return todos

    def get(self, id):
        return sql_data.select_where(self.db_file, self.table, id=id)
    
    def create(self, data):
        data.pop('csrf_token')
        sql_data.add_project(self.db_file, data['title'], data['description'], data['done'])

    def save_all(self):
        pass
    
    def update(self, id, data):
        data.pop('csrf_token')
        sql_data.update_sql(self.db_file, self.table, id, data['title'], data['description'], data['done'])

todos = Todos(sql_data)