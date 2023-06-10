data = {1: "Navin", 2: "Vivek", 4: "Pawan"}

print(data.get(3, "Not Found")) # print not found

# another method _____________(ZIP)______________

keys = ['Navin', 'Kiran', 'Harsh']
values = ['Python', 'Java', 'JS']
data = dict(zip(keys, values))

print(data)

data['angel'] = 'priya'

print(data)

del data['angel']

print(data)
