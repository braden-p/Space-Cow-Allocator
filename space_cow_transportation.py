from partition import get_partitions
import time


def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """

    cow_dict = dict()

    f = open(filename, 'r')
    
    for line in f:
        line_data = line.split(',')
        cow_dict[line_data[0]] = int(line_data[1])
    return cow_dict


def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    cowsList = list(cows.keys())
    weightsList = list(cows.values())
    availWeight = limit

    def findCow(cowsList,index):
        ''' 
        Looks up the heaviest cow that will fit on the current trip
        returns a string, the name of the heaviest cow that will fit
        '''
        return (cowsList[index])
        
    def findIndex(cowsList,weightsList,availWeight):
        ''' 
        Finds the index of the heaviest cow that will fit on the current trip
        Returns an int, the index of the cow and its corresponding weight in their lists
        '''
        targetWeight = availWeight
        while targetWeight > 0:
            for weight in weightsList:
                if weight == targetWeight:
                    index = weightsList.index(weight)
                    return index
            targetWeight -= 1
        
    def willAnyFit(weightsList,availWeight):
        ''' 
        Checks if any of the available cows will fit on the current trip
        returns a boolean, true if a cow will fit false if none will fit
        '''
        willFit = True
        if len(weightsList) == 0:
            return False
        if min(weightsList) > availWeight:
            willFit = False
        return willFit
    
    def removeCow(cowsList, weightsList, index):
        ''' 
        Removes the cow and its correponding weight from the cowsList and weightsList
        '''
        del cowsList[index]
        del weightsList[index]
         
    masterTrips = []
    while len(cowsList) > 0:
        currentTrip = []
        # Fill current trip
        while willAnyFit(weightsList,availWeight):
            index = findIndex(cowsList,weightsList,availWeight)
            currentTrip.append(findCow(cowsList,index))
            availWeight -= weightsList[index]
            removeCow(cowsList, weightsList, index)
        # if trip full, append current trip to masterTrips
        masterTrips.append(currentTrip)  
        availWeight = limit
    return masterTrips


def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    pass

        
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    # TODO: Your code here
    pass


cows = load_cows("cow_data.txt")
limit=100
print(cows)

print(greedy_cow_transport(cows, limit))
print(brute_force_cow_transport(cows, limit))


