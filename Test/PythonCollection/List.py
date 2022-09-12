# list can be defined with [];
# List is a collection which is ordered and changeable.Allow duplicate members

car = ["BMW", "Skoda", "Maruthi"]

print(len(car))
print(type(car))

# Access Items

print(car[-2])

# Range of index
print(car[0:3])

# check if item exists
if "Honda" in car:
    print("BMW is present in car list")
else:
    print("BMW is not present in a cars list ")

# change list items:

car[0] = "Honda"
print(car)

# insert new iteams in exists list
car.insert(3, "BMW")
print(car)

# extend the list items

motor = ["Activa", "Hero", "Bajaj"]
car.extend(motor)
print(car)


# sort list based alphanumerically

car.sort()

print(car)

# Loop based on index

for x in range(len(car)):
    print(car[x])
