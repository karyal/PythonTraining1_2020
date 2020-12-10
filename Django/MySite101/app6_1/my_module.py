import mysql.connector # pip install mysql-connector-python
import sys

class person():
    def __init__(self, pid=0, full_name="", contact_address=""):
        self.pid = pid
        self.full_name = full_name
        self.contact_address = contact_address
    # Getters
    def get_pid(self):
        return self.pid
    def get_full_name(self):
        return self.full_name
    def get_contact_address(self):
        return self.contact_address
    # Setters
    def set_pid(self, pid):
        self.pid=pid
    def set_full_name(self, full_name):
        self.full_name = full_name
    def set_contact_address(self, contact_address):
        self.contact_address = contact_address
    #to_string
    def __str__(self):
        return str(self.pid)+","+self.full_name+","+self.contact_address

def create_table():
    result = "False"
    try:
        conn = mysql.connector.connect(host="localhost", user="admin", password="admin@123", database="python1")
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE contacts (pid int(3) not null primary key, full_name VARCHAR(255) not null, contact_address VARCHAR(255) not null)")
        cursor.close()
        conn.close()
        result = "True"
    except:
        result = "False"
        print("Error : ", sys.exc_info()[1])
    finally:
        return result

def select_all():
    persons = []
    str_sql = """SELECT * FROM contacts"""
    try:
        conn = mysql.connector.connect(host="localhost", user="admin", password="admin@123", database="python1")
        cursor = conn.cursor()
        cursor.execute(str_sql)
        rows = cursor.fetchall()
        for row in rows:
            persons.append(row)
        rows.close()
        cursor.close()
        conn.close()
    except:
        pass
    finally:
        return persons

def search(pid):
    person = None
    str_sql = """SELECT * FROM contacts WHERE pid = %s"""
    values = (pid, )
    try:
        conn = mysql.connector.connect(host="localhost", user="admin", password="admin@123", database="python1")
        cursor = conn.cursor()
        cursor.execute(str_sql, values)
        person = cursor.fetchone()
        cursor.close()
        conn.close()
    except:
        person = None
    finally:
        return person

def insert(person):
    result = "False"
    str_sql = """INSERT INTO contacts VALUES(%s, %s, %s)"""
    values = (person.get_pid(), person.get_full_name(), person.get_contact_address())
    print(values)
    try:
        conn = mysql.connector.connect(host="localhost", user="admin", password="admin@123", database="python1")
        cursor = conn.cursor()
        cursor.execute(str_sql, values)
        conn.commit()
        cursor.close()
        conn.close()
        result = "True"
    except:
        result = "False"
        print("Error: ", sys.exc_info()[1])
    finally:
        return result

def update(person):
    result = "False"
    str_sql = """UPDATE contacts SET full_name=%s, contact_address=%s WHERE pid = %s"""
    values = (person.get_full_name(), person.get_contact_address(), person.get_pid())
    print(values)
    try:
        conn = mysql.connector.connect(host="localhost", user="admin", password="admin@123", database="python1")
        cursor = conn.cursor()
        cursor.execute(str_sql, values)
        conn.commit()
        cursor.close()
        conn.close()
        result = "True"
    except:
        result = "False"
        print("Error: ", sys.exc_info()[1])
    finally:
        return result

def delete(pid):
    result = "False"
    str_sql = """DELETE FROM contacts WHERE pid = %s"""
    values = (pid, )
    try:
        conn = mysql.connector.connect(host="localhost", user="admin", password="admin@123", database="python1")
        cursor = conn.cursor()
        cursor.execute(str_sql, values)
        conn.commit()
        cursor.close()
        conn.close()
        result = "True"
    except:
        result = "False"
        print("Error: ", sys.exc_info()[1])
    finally:
        return result