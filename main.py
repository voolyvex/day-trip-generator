import random

destinations = ["Shore Acres, Oregon", "Antarctica", "Golden Gate State Park", "Preparation Canyon", "Google Headquarters", "Chicago", "Boston", "Italy", "Little Italy", "Hawaiian island", "Aruba", "Kyoto, Japan", "Paris", "Iceland"]
restaurants = ["4-star Michelin restaurant", "Bad Thai", "Taco Shelf", "Chunky Chicken Burgers", "La Buvette", "Panda Express", "Zio's Pizza", "La Casa", "El Mexican Restaurant", "Bangkok Thai Cuisine", "Matsu Sushi", "picnic lunch"]
transportation = ["bicycle", "train", "walking", "Uber", "school bus", "limousine", "skateboard", "kayak", "plane", "snowboard", "taxi", "motorcycle", "horseback", "riding lawnmower"]
entertainment = ["art museum", "nature hike", "ballet", "concert", "dance club", "karaoke", "video game arcade", "miniature golf", "go to a movie", "state fair", "shopping", "architecture tour", "zoo", "scuba diving", "beach day", "go to the theatre"]


def generate_day_trip():
    print_current_trip()

def print_current_trip():
    print("Destination: ", get_random_destination())
    print("Restaurant: ", get_random_restaurant())
    print("Mode of transportation: ", get_random_transportation())
    print("Entertainment: ", get_random_entertainment())


def get_random_restaurant():
    pass
def get_random_destination():
    random_list_index = random.randrange(0, len(destinations))
    return(destinations[random_list_index])
def get_random_transportation():
    pass
def get_random_entertainment():
    pass
def print_final_trip():
    pass

if __name__ == "__main.py__":
    generate_day_trip()