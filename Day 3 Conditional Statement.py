print ("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        print("Child tickets are $5.")      
    elif age <= 18:
        print("Youth tickets are $7.")  
    elif age > 18:
        print("Adult tickets are $12.")
else:
    print("Sorry, you have to grow taller before you can ride.")

print(f"Height in inches: {height / 2.54}")  # Convert cm to inches
print(f"Height in feet: {height / 30.48}")  # Convert cm to feet