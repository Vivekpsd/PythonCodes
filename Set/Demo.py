s = {2, 3, 4, 2, 4, 3, 2}
print(s)

info = {19, "Hero", 10, 1, 5.9}
print(info)

emptySet = {''}
print(type(emptySet))

# ____________ METHODS ____________

s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}

s3 = s1.union(s2)
print(s3)

s3 = s1.intersection(s2)
print(s3)

s1.update(s2)
print(s1)

s3.intersection_update(s1)
print(s3)

#  ________________________________
print("____________________________")
s1 = {1, 2, 3, 4, 5}
s2 = {2, 3, 4, 6, 10}

s3 = s1.symmetric_difference(s2)
print(s3) # those who are not common

# set manipulation

# isdisjoin -> If item of given set is present in another set

s1 = {1, 2, 3, 4}
s2 = {5, 6, 7, 8}

print(s1.isdisjoint(s2))

# issuperset -> if all item of current present in original set

s1 = {1, 2, 3, 4}
s2 = {1, 2}

print(s2.issuperset(s1))
print(s1.issuperset(s2))

# .add()   .remove()