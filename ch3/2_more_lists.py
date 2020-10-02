meats = ['pork', 'chicken', 'beef', 'fish']
meats.sort()
print(meats)
meats.sort(reverse=True)
print(meats)
#sort permanently changes the list

pork = ['bacon', 'sausage', 'ribs', 'loin']
print("\nHere's the original list:")
print(pork)
print("Here's the sorted list:")
print(sorted(pork))
print("\nHere's the original list again:")
print(pork)
#sorted doesn't change the list

print("Here it is reversed:")
pork.reverse()
print(pork)

print("Length of list:")
print(len(pork))

