food = ['pizza', 'hot dogs', 'hamburgers', 'cake', 'tacos']
print(food)
print(food[0])
print(food[0].upper())
print(food[-1])  #last item in list, -2 is next to last, etc.

message = "I love eatting " + food[1] + " and " + food[2] + "."
print(message)

#change an element in a list
food[0] = 'lasagna'
print(food)

#add an element
food.append('pizza')
print(food)

#start with a blank list
new_list = []
new_list.append('stuff')
print(new_list)

#insert an element to a specific position
food.insert(1,'chicken')
print(food)

#remove an element
del food[1]
print(food)

#popping an element
#removes an item but lets you define a variable as it
print("\n*popping*")
popped_food = food.pop()
print(food)
print("The last food I ate was " + popped_food + ".")
popped_food = food.pop(0)
print("The FIRST food I ate was " + popped_food + ".")

#remove element by element
print("\n")
print(food)
food.remove('cake')
print("non desserts:")
print(food)
mexican = 'tacos'
food.remove(mexican)
print(food)