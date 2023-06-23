import sqlite3

conn = sqlite3.connect('test.db')

print("Opened database  Successfully")

conn.execute('''
create table todos (id int, task text, date text, status text)
''')

print("Table Created!")

# conn.execute('''
# insert into todo (id, task, date, status) values (3, 'Jumping', '09/12/23', 'Done');
# ''')
# conn.commit()
 
# print("Values inserted")

# conn.execute('''
# update todo set status = 'Done' where id = 1
# ''')

# conn.commit()

# conn.execute('''
# delete from todo where id=3
# ''')
# conn.commit()

result = conn.execute("select * from todos")

for i in result:
    print(i)