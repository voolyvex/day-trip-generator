import random

destinations = ["Shore Acres, Oregon", "Antarctica", "Golden Gate State Park", "Preparation Canyon", "Google Headquarters", "Chicago", "Boston", "Italy", "Little Italy", "Hawaiian island", "Aruba", "Kyoto, Japan", "Paris", "Iceland"]
restaurants = ["4-star Michelin restaurant", "Bad Thai", "Taco Shelf", "Chunky Chicken Burgers", "La Buvette", "Panda Express", "Zio's Pizza", "La Casa", "El Mexican Restaurant", "Bangkok Thai Cuisine", "Matsu Sushi", "picnic lunch"]
transportation = ["bicycle", "train", "walking", "Uber", "school bus", "limousine", "skateboard", "kayak", "plane", "snowboard", "taxi", "motorcycle", "horseback", "riding lawnmower"]
entertainment = ["art museum", "nature hike", "ballet", "concert", "dance club", "karaoke", "video game arcade", "miniature golf", "go to a movie", "state fair", "shopping", "architecture tour", "zoo", "scuba diving", "beach day", "go to the theatre"]


def generate_day_trip():
    print_current_trip()

def print_current_trip():
    print("Destination: ", get_random_element(destinations))
    print("Restaurant: ", get_random_element(restaurants))
    print("Mode of transportation: ", get_random_element(transportation))
    print("Entertainment: ", get_random_element(entertainment))


def get_random_element(from_list):
    random_list_index = random.randint(len(from_list))
    return(from_list[random_list_index])

def print_final_trip():
    print ("Here is your trip!")

if __name__ == "__main.py__":
    generate_day_trip()