tup = (1, 5, 6, 6, 6, "green")
print(tup)

# rest all are same in tuples as list
# Just tuples are immutable..

# How to change tuple: Converting it to list
temp = list(tup)
temp.append("Blue")
temp.pop(1)
temp[2] = "Yellow"
tup = tuple(temp)

print(tup)

# METHODS ..........

print(temp.index(6))
print(temp.count(6))

