marks = [3, 5, 6, 9, 20, "Hello"]
print(marks)
print(type(marks))


# negative indexing
print(marks[-1])


# in conditionals
if 7 in marks:
    print("Present")
else:
    print("Not Present")


# listName[start: end: JUMPINDEX]
print(marks[0:5:2])

# list are mutable
marks.append(200)
marks.remove(5)
print(marks)

#list slicing
print(marks[1:])


# dictionary and tuple in list :()
dic = {0: "Vivek", 1: "Pawan", 2: "Avro"}
print(dic)

tup = ("apple", "banana", "orange")
print(tup)

marks.append(dic)
marks.append(tup)

print(marks)