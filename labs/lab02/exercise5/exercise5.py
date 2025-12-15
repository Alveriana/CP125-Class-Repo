def is_valid_triangle(a, b, c):
    if (a + b > c) and (a + c > b) and (b + c > a):
        return True
    else:
        return False
    
print(is_valid_triangle(5, 5, 6))