
def was_backward_detected(path):
    """
    Return True if drone moved backward in x or y, False otherwise.
    Use tuple unpacking.
    """
    for i in range(1, len(path)):
        previous_x, previous_y, previous_z = path[i-1]
        current_x, current_y, current_z = path[i]

        if current_x < previous_x or current_y < previous_y:
            return True
    return False


# Test
path = ((0, 0, 10), (5, 5, 12), (4, 6, 10), (10, 10, 15))
result = was_backward_detected(path)
print(f"Backward Movement: {result}")  # Expected: True
