import sqlite3

connection= sqlite3.connect('hospital.db')
cursor=connection.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS patients ( 
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER,
    illness TEXT
    )
    ''')
connection.commit()

print("Database and table created successfully!")

def add_patient(name,age,illness):
    cursor.execute('''
        INSERT INTO patients(name,age,illness)
        VALUES(?,?,?)
    ''',(name,age,illness))
    connection.commit()
    print(f"Successfully added {name} to the database!")

def view_patients():
    cursor.execute('SELECT*FROM patients')
    records=cursor.fetchall()

    print("\n---Current Patients---")
    for row in records:
        print(f"ID:{row[0]} | Name:{row[1]} | Age:{row[2]} | Illness:{row[3]}")
    print("------------\n")


add_patient("Shelly",34,"Asthma")
add_patient("Genotry", 25, "Heart attack") 
add_patient("Shemaiah",35,"Hot Flashes")   


view_patients()

connection.close()
