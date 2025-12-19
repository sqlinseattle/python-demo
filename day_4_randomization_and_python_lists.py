import random

print(random.randint(1,10))

print (random.randrange(1,10))

# Choosing from a list
my_list = ["apple", "banana", "cherry", "date"]
selected_item = random.choice(my_list)
print(selected_item) 

# Choosing from a string
my_string = "Python"
selected_char = random.choice(my_string)
print(selected_char) 

# Choosing from a range
selected_number = random.choice(range(1, 101))
print(selected_number) 