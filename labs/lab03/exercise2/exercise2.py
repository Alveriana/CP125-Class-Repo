def find_station(stations, name):
    for i in range (len(stations)):
        if stations[i] == name:
            return i
    return None  #station name does not exist

def count_stops(stations, start, stop):
    start_index = find_station(stations, start)
    end_index = find_station(stations, stop)

    if start_index == None or end_index == None:
        return -1
    elif start_index >= end_index:
        return start_index - end_index
    elif start_index <= end_index:
        return end_index - start_index