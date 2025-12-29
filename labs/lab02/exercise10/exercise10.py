
def calculate_base_usage(distance):
    """
    Calculates the base battery usage.
    1.5% battery per 10 meters.
    """
    # TODO: Implement this function
    base_usage = 1.5 * (distance/10)

    return base_usage

def apply_mode_bonus(usage, is_sport_mode):
    """
    Increases battery consumption by 50% if in Sport Mode.
    """
    # TODO: Implement this function
    if is_sport_mode:
        usage *= 1.5

    return usage

def has_enough_battery(distance, current_battery, is_sport_mode):
    """
    Calculates if there is enough battery for a round trip (distance * 2).
    """
    # TODO: Implement this function
    total_distance = distance * 2
    usage = calculate_base_usage(total_distance)
    usage = apply_mode_bonus(usage, is_sport_mode)
    return current_battery >= usage