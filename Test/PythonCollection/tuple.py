# A tuple is a collection which is ordered and unchangeable:

thistuple = ("apple", "banana", "cherry")
print(thistuple)


# it will allow duplicate


thistuple = ("apple", "banana", "cherry", "apple")
print(thistuple)

# Change tuple value , Note: once a tuple is created , you cannot change its values.Tuples are unchangeable or immutable as it called.
# Wrokaround: you can convert the tuple into a list , change the list and convert the list back into a tuple.

x = ("apple", "banana", "carrot")
y = list(x)
y[1] = "redbanana"
x = tuple(y)

print(x)

#unpacking the tuple values:

x = ("apple", "banana")

(a, b) = x

print(a)
print(b)

# while loop

x = ("apple", "banana", "carrot", "orange")
i = 0;
while i < len(x):
    print(x[i])
    i = i+1

