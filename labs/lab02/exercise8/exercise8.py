def calculate_bounce_height(current_height):
    """
    Calculate the next bounce height (80% of current).
    """
    # TODO: Implement this
    current_height *= 0.8

    return current_height


def is_ball_stopped(height):
    """
    Check if the ball has stopped (height < 1).
    """
    # TODO: Implement this
    if height < 1:
        return True
    else:
        return False


def calculate_bounce_count(initial_height):
    """
    Count how many times the ball bounces.
    """
    # TODO: Implement this
    bounce_count = 0
    height = initial_height
    
    while height >= 1:
        bounce_count += 1
        height = calculate_bounce_height(height)

    return bounce_count


def calculate_total_distance(initial_height):
    """
    Calculate total distance traveled.
    """
    # TODO: Implement this
    total_distance = initial_height  
    height = initial_height         

    while height >= 1
        next_height = calculate_bounce_height(height)
        if next_height >= 1:
            total_distance += next_height * 2
        else:
            total_distance += next_height

    return total_distance
