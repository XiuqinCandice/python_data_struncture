# given arrival and departure times of trains
# calculate the number of platforms required for a train station
# so that none of them waits

# solution 1 for each time, see how many trains overlap with it, keep track of the max_platform

def find_platform(arrival, departure):

    max_platform = 1
    n = len(arrival)
    for i in range(n):
        num_platform = 1
        for j in range(i+1, n):
            if arrival[j] >= arrival[i] and arrival[j] <= departure[i]:
                num_platform += 1
        if num_platform > max_platform:
            max_platform = num_platform
        
    return max_platform

# O(n^2)
# print(find_platform([900, 940, 950, 1100, 1500, 1800],[910, 1200, 1120, 1130, 1900, 2000]))

# solution 2 use sort
# to consider all events in sorted order
# when we have all events in sorted order, we trace the number of trains at any given time
# check for trains that have arrived, but the previous trains have not departed yet
# this way we know how many platforms we need at that time and take the maximum of all instances
def find_platform2(arrival, departure):
    n = len(arrival)
    arrival.sort()
    departure.sort()

    max_platform = 1
    num_platform = 1 # track the number of platform at a time
    i = 1 # track the arrival list
    j = 0 # track the departure list
    # since the list is already sorted, the arrival[i+1] is always bigger then arrival[i]
    # so only need to compare the later arrival time with the previous departure time
    while i < n and j < n:
        if arrival[i] <= departure[j]:
            # train j has not left yet and the new train arrives, add 1
            num_platform += 1
            i += 1

            if num_platform > max_platform:
                max_platform = num_platform
        else: # else decrement number of platform needed
            num_platform -= 1
            j += 1
        
    return max_platform






print(find_platform2([200, 210, 300, 320, 350, 500],[230, 240, 320, 430, 400, 520]))
'''
The time complexity will now be O(nlogn)O(nlogn), 
because we used sorted lists and greedily kept track of the trains that have arrived but haven’t left yet.
'''