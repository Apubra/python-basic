# Add informations
x = [5,6,2,1,6,7,2,2,6,7,2]

x.append(2)
print(x)

# Add informations specific index
x.insert(2,99)
print(x)

# Remove informations by value
x.remove(99)
print(x)

# Remove informations by index value
x.remove(x[2])
print(x)

# Slicing index in list
print(x[5:9])

# Get last index from list
print(x[-1])

# Get index number by value from list
print(x.index(7))

# Count how much same data in list
print(x.count(6))

# Sorting data in list
x.sort()
print(x)

y = ['Janet', 'Jessy', 'Kelly', 'Alice', 'Joe', 'Bob']
y.sort()
print(y)
