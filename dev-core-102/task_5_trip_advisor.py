def choose_trip():
    
    print("What type of vacation do you prefer?")
    print("1. Active vacation")
    print("2. Relaxing vacation")

    preference = input("Enter 1 for an active vacation or 2 for a relaxing vacation: ")

    
    if preference == '1':
        print("\nChoose a destination for your active vacation:")
        print("1. Mountains")
        print("2. Forest")
        print("3. Desert")
        activity_choice = input("Enter the number of your choice: ")

        if activity_choice == '1':
            print("You chose a vacation in the mountains. Make sure to bring comfortable shoes and warm clothes!")
        elif activity_choice == '2':
            print("You chose a vacation in the forest. Don't forget to take insect repellent with you!")
        elif activity_choice == '3':
            print("You chose a vacation in the desert. Be sure to bring plenty of water!")
        else:
            print("Invalid choice. Please select a valid option.")

    elif preference == '2':
        print("\nChoose a destination for your relaxing vacation:")
        print("1. Beach")
        print("2. SPA")
        print("3. Hotel")
        relaxation_choice = input("Enter the number of your choice: ")

        if relaxation_choice == '1':
            print("You chose a beach vacation. Don't forget to bring sunscreen!")
        elif relaxation_choice == '2':
            print("You chose a SPA vacation. Relax and enjoy your treatments!")
        elif relaxation_choice == '3':
            print("You chose a hotel stay. A great choice for a peaceful retreat!")
        else:
            print("Invalid choice. Please select a valid option.")

    else:
        print("Invalid choice. Please enter 1 or 2.")

    
    try:
        budget = float(input("\nEnter your budget for the trip (in dollars): "))

        if budget < 100:
            print("With your budget, we recommend choosing nearby destinations for active vacations like the forest.")
        elif 100 <= budget < 500:
            print("With your budget, we recommend a beach or forest vacation.")
        else:
            print("You have enough budget for a luxury vacation, such as a SPA or a trip to the mountains!")
    except ValueError:
        print("Error: Please enter a numeric value for the budget.")


if __name__ == "__main__":
    choose_trip()
