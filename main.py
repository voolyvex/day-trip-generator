import random

destinations = ["Shore Acres, Oregon", "Antarctica", "Golden Gate State Park", "Preparation Canyon", "Google Headquarters", "Chicago", "Boston", "Italy", "Little Italy", "Hawaiian island", "Aruba", "Kyoto, Japan", "Paris", "Iceland"]
restaurants = ["4-star Michelin restaurant", "Bad Thai", "Taco Shelf", "Chunky Chicken Burgers", "La Buvette", "Panda Express", "Zio's Pizza", "La Casa", "El Mexican Restaurant", "Bangkok Thai Cuisine", "Matsu Sushi", "picnic lunch"]
transportation = ["bicycle", "train", "walking", "Uber", "school bus", "limousine", "skateboard", "kayak", "plane", "snowboard", "taxi", "motorcycle", "horseback", "riding lawnmower"]
entertainment = ["art museum", "nature hike", "ballet", "concert", "dance club", "karaoke", "video game arcade", "miniature golf", "go to a movie", "science fair", "shopping", "architecture tour", "zoo", "bowling", "beach day", "puppet show"]
current_trip = []

def generate_day_trip():
    get_current_trip()
    print_current_trip()
    user_satisfaction_logic()

def get_random_element(from_list):
    random_list_index = random.randint(0, len(from_list) - 1)
    return(from_list[random_list_index])

def get_current_trip():
    current_trip.append(get_random_element(destinations))
    current_trip.append(get_random_element(restaurants))
    current_trip.append(get_random_element(transportation))
    current_trip.append(get_random_element(entertainment))

def change_current_trip():
    change_list = ["d","r","t","e"]
    change_element = input("\nWhich item would you like to change?\nEnter 'd' for Destination, 'r' for Restaurant,\n't' for Transportation, 'e' for Entertainment: ").strip().lower()
    while change_element not in change_list:
        change_element = input("\nWhich item would you like to change?\nEnter 'd' for Destination, 'r' for Restaurant,\n't' for Transportation, 'e' for Entertainment: ").strip().lower()
    if change_element == "d":
        current_trip[0] = get_random_element(destinations)
    elif change_element == "r":
        current_trip[1] = get_random_element(restaurants)
    elif change_element == "t":
        current_trip[2] = get_random_element(transportation)
    elif change_element == "e":
        current_trip[3] = get_random_element(entertainment)
    print_current_trip()
    user_satisfaction_logic()

def print_current_trip():
    print("Destination: " + current_trip[0])
    print("Restaurant: " + current_trip[1])
    print("Mode of transportation: " + current_trip[2])
    print("Entertainment: " + current_trip[3])


def user_satisfaction_logic():
    user_satisfied = input("Are you happy with this day trip? (y/n): ").strip().lower()
    while user_satisfied != "y" and user_satisfied != "n":
        user_satisfied = input("Are you satisfied? (Enter 'y' or 'n'): ").strip().lower()
    if user_satisfied == "y":
        print_final_trip()
    else:
        change_current_trip()

def print_final_trip():
    print ("\nHere is your trip!")
    print_current_trip()
    current_trip.clear()

if __name__ == "__main__":
    generate_day_trip()