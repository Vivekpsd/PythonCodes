import sqlite3

conn = sqlite3.connect('test.db')

print("Database connected Successfully")

# conn.execute('''
# create table student (name text, id int primary key, batch int, course text)
# ''')

# conn.execute('''
# insert into student (name, id, batch, course) values ('Vivek', 214, 2022, 'MCA')
# ''')

# print("Values inserted")
# conn.commit()

res = conn.execute('''select * from student''')

for i in res:
    print(i)