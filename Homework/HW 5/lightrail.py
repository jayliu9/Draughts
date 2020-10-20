'''
YOUR FILE COMMENT HERE
'''
LINK_STATIONS = ("University of Washington", "Capitol Hill", "Westlake",
                 "University Street", "Pioneer Square",
                 "International District/Chinatown", "Stadium", "SODO",
                 "Beacon Hill", "Mount Baker", "Columbia City", "Othello",
                 "Rainier Beach", "Tukwila International Boulevard",
                 "SeaTac/Airport", "Angle Lake")



def is_valid_station(station):
    '''
        Function -- is_valid_station
            Checks if a given string is a valid Seattle light rail station.
            Provided station must match a station name exactly. For example, "mount
            baker" would not be valid because the case doesn't match.
        Parameter:
            station -- The string to check
        Returns:
            True if a given string is a valid Seattle light rail station
            name, False otherwise.
    '''
    return station in LINK_STATIONS



def get_direction(start, end):
    '''
        Function -- get_direction
            Given start and end station names, determines if the direction is
            Northbound or Southbound.
        Parameters:
            start - The starting station name
            end - The ending station name.
        Returns:
            "Northbound" if the end station is north of the start station, or
            "Southbound" if the end station is south of the start station. If
            either station is invalid, or start and end stations are the same,
            return "No destination found".
    '''
    if not good_start_end(start, end):
        return "No destination found"
    elif index_difference(start, end) < 0:
        return "Southbound"
    return "Northbound"
    

def get_num_stops(start, end):
    '''
        Function -- get_num_stops
            Calculates the number of stops from start to end.
        Parameters:
            start - The starting station name
            end - The ending station name.
        Returns: 
            The number of stops from start to end. If either station is invalid
            or both stations are the same, return 0.
    '''
    if not good_start_end(start, end):
        return 0
    num_of_stops = abs(index_difference(start, end))
    return num_of_stops


def index_difference(start, end):
    '''
        Function -- index_difference
            Calculates the difference between the indexes of the start station
            and the end station in the predefined tuple. The index of the start
            station is set to the minuend.
        Parameters:
            start - The starting station name
            end - The ending station name.
        Returns:
            The difference between the indexes of the start station and the end
            station in the predefined tuple.
            
    '''
    start_index = LINK_STATIONS.index(start)
    end_index = LINK_STATIONS.index(end)
    return start_index - end_index


def good_start_end(start, end):
    '''
        Function -- good_start_end
            Checks if the start station and the end station are valid and make
            sense for the program at the same time.
        Parameters:
            start - The starting station name
            end - The ending station name.
        Returns:
            True if the start station and the end station are valid and make
            sense for the program at the same time, False otherwise.
    '''
    both_valid_stations = is_valid_station(start) and is_valid_station(end)
    return both_valid_stations and index_difference(start, end) != 0