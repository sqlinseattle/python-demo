# The for loop iterates over each fruit in the list and prints it.
fruits = ["apple", "banana", "cherry", "date", "elderberry"]  # A list of fruits
for fruit in fruits:
    print(fruit)
print("All fruits have been printed.")

# student_scores = [
#     "Alice": 85,    
#     "Bob": 92,
#     "Charlie": 78,
#     "Diana": 90,
#     "Ethan": 88,
#     "Andre": 95,
#     "Fiona": 73,
#     "George": 80]

student_scores = [85, 92, 78, 90, 88, 95, 73, 80, 67, 100, 82, 76, 89, 94, 81, 77, 84, 91, 79, 87, 93, 110, 65, 72, 86, 83, 74, 96, 98, 99, 64, 71, 69, 68, 66, 75, 97, 101, 102, 103, 104, 105, 106, 107, 108, 109]
total_score = 0
for score in student_scores:
    total_score += score
average_score = total_score / len(student_scores)
print(f"Average score: {average_score}")
print(f"Max score: {max(student_scores)}")
print(f"Min score: {min(student_scores)}")  

# for loop on range
_accumulator = 0
for number in range(1, 101):  # Numbers from 1 to 100 inclusive
    _accumulator += number
print(f"Sum of numbers from 1 to 100: {_accumulator}")