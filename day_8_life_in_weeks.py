def life_in_weeks() -> None:
    age = int(input("What is your current age? "))
    years_remaining = 90 - age
    weeks_remaining = years_remaining * 52
    print(f"You have {weeks_remaining} weeks left.")


life_in_weeks() 