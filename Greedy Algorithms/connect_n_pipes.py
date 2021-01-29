'''
Implement a function that connects n pipes of different lengths, into one pipe. 
You can assume that the cost to connect two pipes is equal to the sum of their lengths. 
We need to connect the pipes with minimum cost.
'''
def min_cost(pipes):
    total_cost = 0
    cost = 0
    pipes.sort()
    for i in range(0,len(pipes)-1):
        cost = pipes[i] + pipes[i+1]
        pipes[i+1] = cost
        total_cost = total_cost + cost
    return total_cost
    

pipes = [5,6,7,8]
print(min_cost(pipes))