states_of_america = [
    "Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut",
    "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas",
    "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota",
    "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey",
    "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon",
    "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah",
    "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"
]

states_of_america.extend(["Washington D.C.", "Puerto Rico", "Guam", "U.S. Virgin Islands", "American Samoa"])
print (len(states_of_america))


print (states_of_america)

states_of_america.sort()

print (states_of_america)

print ("List of U.S. States:")
for state in states_of_america:
    print(state)    

dirty_dozen = [
    "Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes",
    "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"
]

print("Dirty Dozen Fruits and Vegetables:")
for item in dirty_dozen:
    print(item) 


dirty_dozen_fruit = dirty_dozen[0:6]    
print("Dirty Dozen Fruits:")
for fruit in dirty_dozen_fruit:
    print(fruit)

# print (states_of_america[10])  # prints "Hawaii"

fruits = ["apple", "banana", "cherry", "date", "elderberry"]
vegetables = ["asparagus", "broccoli", "carrot", "daikon", "endive"]
dirty_dozen = [fruits, vegetables]             
print ("Dirty Dozen [1][1]:", dirty_dozen[1][1])