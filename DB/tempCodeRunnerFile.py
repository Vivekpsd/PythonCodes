res = conn.execute('''
select * from todo
''')

for data in res:
    print(data)