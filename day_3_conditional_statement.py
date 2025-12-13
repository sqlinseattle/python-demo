print ("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))


if height >= 120:
    print("You can ride the rollercoaster!")
    bill = 0
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5    
    elif age <= 18:
        bill = 7
    elif age > 18:
        bill = 12
    elif age >= 45 and age <= 55:
        print("Everything is going to be ok. Have a free ride on us!")
        bill = 0
    wants_photo = input("Do you want a photo taken? Y or N. ").upper()  
    if wants_photo == "Y":
        bill += 3
    print(f"Your final bill is ${bill}.")


else:
    print("Sorry, you have to grow taller before you can ride.")

#print(f"Height in inches: {height / 2.54}")  # Convert cm to inches
#print(f"Height in feet: {height / 30.48}")  # Convert cm to feet

print ("Welcome to Python Pizza Deliveries!")