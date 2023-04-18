import heapq

def heuristic(a, b):
    return abs(b[0] - a[0]) + abs(b[1] - a[1])

def astar(graph, start, end):
    frontier = []
    heapq.heappush(frontier, (0, start))
    camefrom = {}
    costsofar = {}
    camefrom[start] = None
    costsofar[start] = 0
    while frontier:
        currentcost, currentnode = heapq.heappop(frontier)
        if currentnode == end:
            break
        for nextnode in graph.neighbors(currentnode):
            newcost = costsofar[currentnode] + graph.cost(currentnode, nextnode)
            if nextnode not in costsofar or newcost < costsofarnext_node:
                costsofarnext_node = newcost
                priority = newcost + heuristic(end, nextnode)
                heapq.heappush(frontier, (priority, nextnode))
                camefrom[nextnode] = currentnode
    return camefrom, costsofar
