def analyze_mood():
    print("--- Mood Analyzer ---")

    questions = ["did you sleep well today? (y/n): ", "did you eat today? (y/n): ", "did you work today? (y/n): "]
    
    points = 0
    
    for question in questions:
        response = input(question)
        while response != "y" and response != "n":
            print("Invalid response. Please answer with 'y' or 'n'.")
            response = input(question)

        if response == "y":
            points += 1
        else:
            points -= 1
    
    if points == 3:
        print("Great day! You are feeling awesome.")
    elif points >= 1:
        print("Okay day! Things are moving along.")
    else:
        print("Tough day... Take some rest!")

    return points

analyze_mood()

while True:
    response = input("Would you like to analyze your mood again? (y/n): ")
    while response not in ("y", "n"):
        print("Invalid response. Please answer with 'y' or 'n'.")
        response = input("Would you like to analyze your mood again? (y/n): ")

    if response == "y":
        analyze_mood()
    else:
        print("Goodbye! Thank you for using the Mood Analyzer.")
        break