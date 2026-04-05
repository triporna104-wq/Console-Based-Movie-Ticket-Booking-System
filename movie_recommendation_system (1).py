movies = {
    1: {"name": "3 Idiots", "price": {"Silver": 150, "Gold": 200, "Platinum": 300}},
    2: {"name": "Dhurandhar 2", "price": {"Silver": 120, "Gold": 180, "Platinum": 250}},
    3: {"name": "Avengers", "price": {"Silver": 130, "Gold": 190, "Platinum": 270}}
}

seats = {
    "Silver": list(range(1, 21)),
    "Gold": list(range(1, 16)),
    "Platinum": list(range(1, 11))
}

def display_movies():
    print("\nAvailable Movies:")
    for key, value in movies.items():
        print(f"{key}. {value['name']}")

def select_movie():
    while True:
        try:
            choice = int(input("Select a movie (1-3): "))
            if choice in movies:
                return choice
            else:
                print("Invalid choice. Try again.")
        except:
            print("Enter a valid number.")

def display_seat_categories(movie_choice):
    print("\nSeat Categories & Prices:")
    for category, price in movies[movie_choice]["price"].items():
        print(f"{category} - Rs.{price}")

def select_category(movie_choice):
    while True:
        category = input("Select category (Silver/Gold/Platinum): ").capitalize()
        if category in movies[movie_choice]["price"]:
            return category
        else:
            print("Invalid category. Try again.")

def show_available_seats(category):
    print(f"\nAvailable seats in {category}:")
    print(seats[category])

def select_seat(category):
    while True:
        try:
            seat = int(input("Select seat number: "))
            if seat in seats[category]:
                seats[category].remove(seat)
                return seat
            else:
                print("Seat not available. Choose another.")
        except:
            print("Enter a valid seat number.")

def calculate_price(movie_choice, category, num_tickets):
    price_per_ticket = movies[movie_choice]["price"][category]
    total = price_per_ticket * num_tickets
    return total

def payment(total_amount):
    print(f"\nTotal amount to pay: Rs.{total_amount}")
    input("Press Enter to simulate payment...")
    print("Payment Successful!")

def booking_confirmation(movie_choice, category, booked_seats, total):
    print("\n----- Booking Confirmation -----")
    print(f"Movie: {movies[movie_choice]['name']}")
    print(f"Category: {category}")
    print(f"Seats Booked: {booked_seats}")
    print(f"Total Paid: Rs.{total}")
    print("Enjoy your movie!")
    print("--------------------------------")

def main():
    print("🎬 Welcome to Movie Ticket Booking System 🎬")

    while True:
        display_movies()
        movie_choice = select_movie()

        display_seat_categories(movie_choice)
        category = select_category(movie_choice)

        show_available_seats(category)

        try:
            num_tickets = int(input("Enter number of tickets: "))
        except:
            print("Invalid input. Defaulting to 1 ticket.")
            num_tickets = 1

        booked_seats = []
        for i in range(num_tickets):
            print(f"\nBooking seat {i+1}:")
            seat = select_seat(category)
            booked_seats.append(seat)

        total = calculate_price(movie_choice, category, num_tickets)

        payment(total)

        booking_confirmation(movie_choice, category, booked_seats, total)

        cont = input("\nDo you want to book another ticket? (yes/no): ").lower()
        if cont != "yes":
            print("Thank you for using the system!")
            break

main()