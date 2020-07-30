# Use this playground to experiment with list methods, using Test Run

elements = ['hydrogen', 'number', 'weight', 'symbol']

# to know the number of items in the list, you usen .len()
print(len(elements))

# to add an item ti the end of he list, you use .append()
elements.append('neighbor')

print(elements)

# .insert()


# to remove an item from a list
elements.remove('number')

print(elements)

# .pop() remove the last item if the item is not specified
elements.pop()

print(elements)

# copy() makes a copy of list 
elements.copy()

print(elements)


# the clear() empties the list
elements.clear()

print(elements)


