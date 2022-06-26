import sqlite3

class db:
    def __init__(self, group):
        self.group = group
        with sqlite3.connect('logs.db') as self.db:
            self.cursor = self.db.cursor()
            query = str(
                'CREATE TABLE IF NOT EXISTS ' + self.group + 'logs (id INTEGER, role TEXT, filename TEXT, action TEXT, time INTEGER, thetable TEXT, subid INTEGER, other_information BLOB)')
            self.cursor.execute(query)

    def add_log(self,id, role, filename, action, time, table, subid=None, other_information=None):
        query = 'INSERT INTO ' + self.group + 'logs VALUES( ? , ? , ? , ? , ? , ?, ?, ?)'
        self.cursor.execute(query, [id, role, filename, action, time, table, subid, other_information])
        print('log added')
        self.db.commit()

    def return_selflength(self):
        query = 'SELECT COUNT(*) FROM ' + self.group + 'logs'
        self.cursor.execute(query)
        a = self.cursor.fetchone()
        return a[0]

    def return_logs(self):
        query = 'SELECT * FROM ' + self.group + 'logs'
        self.cursor.execute(query)
        a = self.cursor.fetchall()
        return a