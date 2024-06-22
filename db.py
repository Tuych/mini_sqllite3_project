import sqlite3


class DB:
    def __init__(self):
        self.con = sqlite3.connect("mini_crm_sqlite3.db")
        self.cur = self.con.cursor()

        self.cur.executescript(f"""
            CREATE TABLE IF NOT EXISTS groups(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT
            );
            
            CREATE TABLE IF NOT EXISTS student(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                last_name TEXT NOT NULL,
                phone_number BLOB NOT NULL DEFAULT "+79505158493",
                email TEXT UNIQUE,
                group_id INTEGER,
                FOREIGN KEY (id)
                REFERENCES groups(id)
            )
        """)
        self.con.commit()

    # <<< section for groups >>>

    def view_groups(self):
        groups = self.cur.execute("SELECT * FROM groups").fetchall()
        return groups

    def add_group(self, group_name):
        self.cur.execute(f"INSERT INTO groups VALUES(NULL, ?)", (group_name, ))
        self.con.commit()

    # group_list = [(...), (...)]
    def add_group_list(self, group_list):
        self.cur.executemany("INSERT INTO groups VALUES(NULL, ?)", group_list)
        self.con.commit()

    # << section for students >>

    def view_student(self):
        students = self.cur.execute("SELECT * FROM student").fetchall()
        return students

    def add_student(self, name, last_name, phone_number, email, group_id):
        self.cur.execute("INSERT INTO student \
                         VALUES(NULL, ?, ?, ?, ?, ?)", (name, last_name, phone_number, email, group_id))
        self.con.commit()

    # student_list = [(...), (...)]
    def add_student_list(self, student_list):
        self.cur.executemany("INSERT INTO groups VALUES(NULL, ?)", student_list)
        self.con.commit()

    def edit_tables(self, table_name, column_name, new_value, _id):
        self.cur.execute(f"""
            UPDATE {table_name}
            SET {column_name} = "{new_value}"
            WHERE id = {_id}
        """)
        self.con.commit()

    def delete_tables(self, table_name, id_):
        self.cur.execute(f"""
           DELETE FROM {table_name}
           WHERE id = {id_} 
        """)
        self.con.commit()



        













