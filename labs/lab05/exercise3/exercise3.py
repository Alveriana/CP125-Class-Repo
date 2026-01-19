
def find_bottleneck_index(traceroute):
    """
    Find the index of the hop where the largest latency jump begins.
    """
    max_jump = 0
    bottleneck = 0
    for i in range(1, len(traceroute)):
        hop_number, current_latency = traceroute[i]
        hop_number, previous_latency = traceroute[i-1]

        hop_number = current_latency - previous_latency
        
        if hop_number > max_jump:
                max_jump = hop_number
                bottleneck = i-1
    
    return bottleneck


# Test
traceroute = ((1, 5), (2, 8), (3, 45), (4, 48), (5, 50))
result = find_bottleneck_index(traceroute)
print(f"Bottleneck Index: {result}")  # Expected: 1
