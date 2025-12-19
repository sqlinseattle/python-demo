def calculate_love_score(name_1, name_2):
    # Combine names and convert to lowercase
    combined_names = (name_1 + name_2).lower()

    # Count occurrences of letters in "TRUE"
    true_count = sum(combined_names.count(letter) for letter in "true")

    # Count occurrences of letters in "LOVE"
    love_count = sum(combined_names.count(letter) for letter in "love")

    # Combine counts to form a two-digit score
    love_score = int(f"{true_count}{love_count}")

    # Determine the message based on the love score
    # if love_score < 10 or love_score > 90:
    #     return f"Your score is {love_score}, you go together like coke and mentos."
    # elif 40 <= love_score <= 50:
    #     return f"Your score is {love_score}, you are alright together."
    # else:
    #     return f"Your score is {love_score}."
    return love_score


print(calculate_love_score("Kanye West", "Kim Kardashian"))
    