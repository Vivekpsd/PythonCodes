# string methods (string are immutable)

a = "Harry"
print(len(a))

print(a.upper())    
print(a.lower())   
print(a.replace('r', 'p'))

sent = "hello World! How are you?"
print(sent.split(" "))

print(sent.capitalize())

print(sent.endswith('?'))

print(sent.find('z'))

data = "alpha123"
print(data.isalnum())