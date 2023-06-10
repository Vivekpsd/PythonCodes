theList = [3, 5, 6, 9, 20, "Hello"]
print(theList)
print(type(theList))


# negative indexing
print(theList[-1])


# in conditionals
if 7 in theList:
    print("Present")
else:
    print("Not Present")


# listName[start: end: JUMPINDEX]
print(theList[0:5:2])

# list are mutable
theList.append(200)
theList.remove(5)
print(theList)

#list slicing
print(theList[1:])


# dictionary and tuple in list :()
dic = {0: "Vivek", 1: "Pawan", 2: "Avro"}
print(dic)

tup = ("apple", "banana", "orange")
print(tup)

theList.append(dic)
theList.append(tup)

print(theList)


# methods in list
marks = [200, 20, 30, 10, 50, 10]

marks.sort()
print(marks)

marks.reverse()
print(marks)

print(marks.index(50)) # index of 50

print(marks.count(10)) # no. of occ of 10

# copying vs referance

# score = marks # score is now referance to marks list and 
#               # change in score will reflect the change in marks too!

# score[0] = "Changed Ha Ha Ha!"
# print(score)
# print(marks)

# copying list

score = marks.copy();
score[0] = "Changed Ha Ha Ha!"
print(score)
print(marks)

# merge two list
theList.extend(score)
print(theList)