def cs():
    print("—" * 5, "WELCOME TO DreamSafari!!", "—" * 5)
    print("             ~Make your dream trips real!")
    
    # Trip details
    from datetime import datetime
    import random
    
    trip_name = input("Enter trip name: ").upper()
    start_date_str = input("Enter start date (YYYY/MM/DD): ")
    end_date_str = input("Enter end date (YYYY/MM/DD): ")
    number_of_people = int(input("Enter number of people: "))
    destination = input("Enter destination: ").title()
    start_date = datetime.strptime(start_date_str, "%Y/%m/%d")
    end_date = datetime.strptime(end_date_str, "%Y/%m/%d")
    duration = (end_date - start_date).days

    print("—" * 5, "TRIP DETAILS", "—" * 5)
    print(f"Trip Name: {trip_name}")
    print(f"Start Date: {start_date.strftime('%Y/%m/%d')}")
    print(f"End Date: {end_date.strftime('%Y/%m/%d')}")
    print(f"Duration: {duration} days")
    print(f"Number of People: {number_of_people}")
    print(f"Destination: {destination}")
    
    # Itinerary Plan
    print("-" * 5,"ITINERARY PLAN","-" * 5)
    places_by_city = {
        "Mumbai": ["Gateway of India","Marine Drive","Trimbakeshwar Jyotirling","Juhu Beach", "Siddhivinayak Temple",
        "Chhatrapati Shivaji Terminus", "Lonavala", "Nasik", "Shirdi", "Ajanta and Ellora Caves"],
        "Delhi": ["Red Fort", "India Gate", "Kashi Viswanath Temple", "Lotus Temple", "Mathura",
        "Akshardham Temple", "Taj Mahal", "Chandni Chowk", "Raj Ghat", "Ayodhya"],
        "Kolkata": ["Victoria Memorial", "Howrah Bridge", "Dakshineswar Temple", "Eden Gardens", "Birla Planetarium",
        "Indian Museum", "Kalighat Temple", "Science City", "Park Street", "Eco Park"],
        "Hyderabad": ["Charminar", "Golconda Fort", "Hussain Sagar Lake", "Salar Jung Museum", "Ramoji Film City",
        "Birla Mandir", "Lumbini Park", "Chowmahalla Palace", "Snow World", "Nehru Zoological Park"],
        "Ahmedabad": ["Sabarmati Ashram", "Kankaria Lake", "Adalaj Stepwell", "Akshardham Temple", "Jama Masjid",
        "Manek Chowk", "Sidi Saiyyed Mosque", "Calico Museum", "Law Garden", "Auto World Vintage Car Museum"],
        "Bangalore": ["Lalbagh Botanical Garden", "Cubbon Park", "Bangalore Palace", "Tipu Sultan’s Palace", "UB City Mall",
        "Vidhana Soudha", "ISKCON Temple", "Bannerghatta National Park", "Nandi Hills", "Commercial Street"],
        "Chennai": ["Marina Beach", "Kapaleeshwarar Temple", "Fort St. George", "Santhome Cathedral", "Government Museum",
        "Vivekananda House", "Edward Elliot's Beach", "VGP Universal Kingdom", "Guindy National Park", "Mahabalipuram"]

    }

    local_tips = {
        "Mumbai": "Eat a vada pav from a busy street shop!😉",
        "Delhi": "Try chole bhature in Chandni Chowk!😉",
        "Kolkata": "Enjoy the lights and music during Durga Puja!🪔",
        "Hyderabad": "Eat tasty biryani at Paradise restaurant!😊",
        "Ahmedabad": "Buy colorful things at Law Garden market!",
        "Bangalore": "Drink hot filter coffee at a small cafe!",
        "Chennai": "Watch the sunrise and eat dosa at Marina Beach!🌅"
    }

    if destination in places_by_city:
        print(f"\nYour itinerary for {destination}:")
        selected_places = random.sample(places_by_city[destination], min(duration, len(places_by_city[destination])))
        for day in range(duration):
            place = selected_places[day % len(selected_places)]
            print(f"Day {day + 1}: Visit {place}")
        print("\nTravel Tip:")
        print(local_tips[destination])
    else:
        print("Sorry, we don't have information for that city.")

    # Budget setup
    print("-" * 5, "BUDGET", "-" * 5)
    total_budget = float(input("Enter your total budget: "))
    categories = {
        "Travel": 0.35,
        "Accommodation": 0.30,
        "Food": 0.20,
        "Entertainment": 0.10,
        "Miscellaneous": 0.05
    }
    budget = {category: total_budget * percentage for category, percentage in categories.items()}
    for category in categories:
        print(f"{category} budget: ₹{budget[category]:.2f}")
    
    # Travel Booking
    print("-" * 5,"TRAVEL BOOKING","-" * 5)
    travel_cost = 0
    travel_budget_input = input("Enter your travel budget (low / medium / high): ").lower()
    if travel_budget_input == "low":
        options = {1: ("Vande Bharat Express - 6:00 AM", 900), 2: ("Shatabdi Express - 8:00 PM", 850)}
    elif travel_budget_input == "medium":
        options = {1: ("IndiGo Flight - 9:00 AM", 4500), 2: ("AirAsia Flight - 5:00 PM", 4800), 3: ("Rajdhani Express - 11:00 PM", 3500)}
    elif travel_budget_input == "high":
        options = {1: ("Vistara Flight - 6:00 AM", 7000), 2: ("SpiceJet Flight - 9:00 PM", 6800), 3: ("Tata Starbus - 8:00 AM", 4500), 4: ("Maharaja Express - 4:00 PM", 9500)}
    else:
        print("Invalid budget entered.")
        options = {}

    if options:
        for num, (desc, cost) in options.items():
            print(f"{num}. {desc} - ₹{cost}")
        choice = int(input("Enter your choice number: "))
        if choice in options:
            travel_cost = number_of_people * options[choice][1]
            print(f"\nYou selected: {options[choice][0]} - ₹{travel_cost}")
        else:
            print("Invalid option selected.")

    # Accommodation Booking
    print("-" * 5,"ACCOMMODATION BOOKING","-" * 5)
    accommodation_cost = 0
    hotel_budget_input = input("Enter your hotel budget (low / medium / high): ").lower()
    if hotel_budget_input == "low":
        Hotels = {1: ("Ginger Hotels", 900), 2: ("Treebo Hotels", 1500)}
    elif hotel_budget_input == "medium":
        Hotels = {1: ("Lemon Tree Hotels", 3500), 2: ("Fortune Hotels", 5500)}
    elif hotel_budget_input == "high":
        Hotels = {1: ("Taj Hotels", 9000), 2: ("ITC Hotels", 15000)}
    else:
        print("Invalid budget entered.")
        Hotels = {}

    if Hotels:
        for num, (desc, cost) in Hotels.items():
            print(f"{num}. {desc} - ₹{cost} per night")
        choice = int(input("Enter your choice number: "))
        if choice in Hotels:
            accommodation_cost = Hotels[choice][1] * duration
            print(f"\nYou selected: {Hotels[choice][0]} - ₹{accommodation_cost} for {duration} nights")
        else:
            print("Invalid option selected.")

    # Expense Calculation
    actual_expenses = {
        "Travel": travel_cost,
        "Accommodation": accommodation_cost
    }

    print("\nEnter your actual expenses for the remaining categories:")
    for category in categories:
        if category not in actual_expenses:
            expense = float(input(f"{category}: ₹"))
            actual_expenses[category] = expense

    total_expenditure = sum(actual_expenses.values())
    remaining_budget = {
        category: budget[category] - actual_expenses[category]
        for category in budget
    }

    print("-" * 5, "EXPENSES", "-" * 5)
    for category in budget:
        print(f"--> {category} expenditure: ₹{actual_expenses[category]:.2f}")
        print(f"Remaining budget for {category}: ₹{remaining_budget[category]:.2f}")

    print(f"\nTotal Expenditure: ₹{total_expenditure:.2f}")
    if total_expenditure > total_budget:
        overspent = total_expenditure - total_budget
        print(f"You have overspent by: ₹{overspent:.2f}")
    else:
        print(f"You are within the budget. Remaining: ₹{total_budget - total_expenditure:.2f}")

    print("-" * 5, "SUMMARY", "-" * 5)
    print(f"Trip Name: {trip_name}")
    print(f"Duration: {duration} days")
    print(f"Total Budget: ₹{total_budget}")
    print(f"Total Expenditure: ₹{total_expenditure}")
    print(f"HAVE A GREAT JOURNEY ON YOUR, {trip_name}! 😊")
    print("Go anywhere with DreamSafari!")

cs()