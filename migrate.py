from main import db_init

def create_table(db):
    table_name = "videos"
    fields = ('id INTEGER PRIMARY KEY AUTOINCREMENT', 'name TEXT NOT NULL', 'duration TEXT NOT NULL')

    db.create_table(table_name, fields)

def migrate():
    db = db_init()

    create_table(db)

migrate()