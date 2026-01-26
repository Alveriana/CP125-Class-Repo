received_list = ["Drill", "Hammer", "Drill", "Saw", "Hammer", "Drill", "Wrench"]

def find_popular_items(received_list):
    count = set()
    popular = set()
    for item in received_list:
        if item in count :
            count.add(item)
        else:
            popular.add(item)

    return popular

find_popular_items = (["Drill", "Hammer", "Drill", "Saw", "Hammer", "Drill", "Wrench"])