def get_position(cars, car_number):
    for i in range (len(cars)):
        if cars[i] == car_number:
            return i

def has_overtaken(before, after, car1, car2):
    car1_before = get_position(before, car1)
    car2_before= get_position(before, car2)

    car1_after = get_position(after, car1)
    car2_after = get_position(after, car2)

    if car1_before > car2_before and car2_after > car1_after:
        return True
    
    return False
