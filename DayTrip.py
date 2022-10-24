import random
from re import T
from tkinter import N, Y
destination = ["Cincinnati", "Chicago", "Orlando", "Mason, OH", "Myrtle Beach", "Tampa Bay"] 
transportation = ["a car", "a train", "an airplane"]
restaurant = ["Chick-Fil-A", "Skyline Chili", "La Rosas", "Outback Steakhouse", "Olive Garden"]
entertainment = ["a baseball game", "a football game", "a basketball game", "Kings Island", "the beach"]

trip_dictionary = {
    "destination": "Mason, OH", 
    "transportation": "car",
    "restaurant": "La Rosas",
    "entertainment": "Kings Island"
}

while True:
    random_dest = random.choice(destination)
    print(f"How does {random_dest} sound for your destination?")
    user_choice = input("Please enter Y or N: ")
    if user_choice == Y:
        print(f"Sounds great! You are sure to have fun in {random_dest}!")
        trip_dictionary["destination"] = random_dest
        break
    elif user_choice == N:
        print(f"That's okay. We will choose another destination.")

while True:
    random_tran = random.choice(transportation)
    print(f"How does {random_tran} sound for your transportation?")
    user_choice = input("Please enter Y or N: ")
    if user_choice == Y:
        print(f"Sounds great! Let's get your {random_tran}!")
        trip_dictionary["transportation"] = random_tran
        break
    elif user_choice == N:
        print(f"That's okay. We will choose other transportation.")

while True:
    random_rest = random.choice(restaurant)
    print(f"How does {random_rest} sound for your restaurant?")
    user_choice = input("Please enter Y or N: ")
    if user_choice == Y:
        print(f"Yum! Enjoy the pizza from {random_dest}!")
        trip_dictionary["restaurant"] = random_rest
        break
    elif user_choice == N:
        print(f"That's okay. Let's pick a different restaurant.")

while True:
    random_ent = random.choice(entertainment)
    print(f"How does {random_ent} sound for your entertainment?")
    user_choice = input("Please enter Y or N: ")
    if user_choice == Y:
        print(f"Sounds exciting! Let's ride some roller coasters at {random_ent}!")
        trip_dictionary["entertainment"] = random_ent
        break
    elif user_choice == N:
        print(f"That's okay. There's more entertainment to choose.")


final_trip = "Drive to Mason, OH in your car head to Kings Island and have some La Rosas pizza while there."

print(final_trip)