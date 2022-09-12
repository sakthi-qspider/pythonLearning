# A set is a collection which is unordered, unchangeable*, and unindexed.
# Set items are unchangeable, but you can remove items and add new items.
# Sets are written with curly brackets.


thisset = {"apple", "banana", "orange", "apple"}

print(thisset)

# change the  item
x = {"apple", "banana", "orange", "apple"}
y = list(x)
y[1] = "rebanana"
x = set(y)
print(x)


# Remove

x = {"apple", "banana", "orange"}

#x.remove("orange")
#x.discard("orange")
x.pop()
print(x)

# Join Two Set

set1 = {"a", "b", "c", "d"}
set2 = {1, 2, 3, 4, 5}

set3 = set1.union(set2)
print(set3)






