
def filter_query_times(times):
    """
    Remove slow outliers (mean + std deviation) and return sorted times.
    """
    if len(times) == 0:
        return []
    
    mean = sum(times)/len(times)
    total = 0
    for x in times:
        total += (x-mean) ** 2 

    variance = total/len(times)
    std_dev = variance * 0.5
    upper_limit = mean + std_dev

    cleaned=[]
    for x in times:
        if x <= upper_limit:
            cleaned.append(x)


    cleaned.sort()
    return cleaned


# Test
query_times = [45, 52, 48, 180, 51, 47, 50, 12]
result = filter_query_times(query_times)
print(f"Filtered Times: {result}")  
# Expected: [12, 45, 47, 48, 50, 51, 52]
