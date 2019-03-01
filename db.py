import sqlite3


def create_connection(db_name='ec2'):
    return sqlite3.connect(db_name + '.db')

def create_instances_table(conn):
    cursor = conn.cursor()
    try:
        cursor.execute("""
            CREATE TABLE instances (
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    instance_id VARCHAR(25) NOT NULL UNIQUE,
                    name VARCHAR(255),
                    status_code INTEGER,
                    status_name VARCHAR(60)
            );
            """)
        return True
    except sqlite3.Error as e:
        return print('ERROR: ', e)
