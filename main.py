import sqlite3
from faker import Faker

faker = Faker

con = sqlite3.connect("home_3.db")
cur = con.cursor()
sql = '''
CREATE TABLE IF NOT EXISTS person(
person_id NOT NULL VARCHAR(128),
address NOT NULL VARCHAR(1024),
job NOT NULL VARCHAR(128),
age NOT NULL INTEGER)
'''

cur.execute(sql)
sql = '''
INSERT INTO person (person_id, address, job, age) VALUES
    (1, 'Hollywood, 12', 'it', 22)
    (2, 'Paris, 2', 'driver', 35)
    (3, 'Ukraine, Kharkov, 77', 'lawyer', 55)  
'''
con.close()


def select_person():
    con = sqlite3.connect("home_3.db")
    cur = con.cursor()
    sql = '''
        SELECT person_id, address, job, age FROM person ORDER BY person_id
        '''
    person = cur.execute(sql)
    for i in person:
        print(i[1], i[3])
    con.close()
