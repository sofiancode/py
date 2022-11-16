# Dictionary in Python is a collection of keys values,
# used to store data values like a map,
# which, unlike other data types which hold only a single value as an element.

capitals = {'Germany': 'Berlin', 'Russia': 'Moscow', 'USA': 'Washington'}
print(capitals.values())
print(capitals.keys())
print(capitals.items())

# conveting dictinary
print(list(capitals))
print(tuple(capitals))

# indexing with a dict

print(capitals['Germany'])  # does crash when it doesnt find the key
print(capitals.get('Russia'))  # better way to indexing Dictionary
print(capitals.get('X'))  # doesnt crash when it cannot find a key

# added key value to dictionary

capitals.update({'France': 'Paris'})
capitals.update(Japan='Tokyo')
print(capitals)
