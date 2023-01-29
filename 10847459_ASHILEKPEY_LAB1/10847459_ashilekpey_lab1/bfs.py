#represent all the structure in a graph
#initialize queues for tracking 
#check for goal 


tree = {
    5 : [3,7],
    3 : [2,4],
    7 : [8],
    2 : [],
    4 : [8],
    8 : []
}

#queues initialization
visited = []
toVisit = []

def bfs(visited,tree,startNode,goal):
    toVisit.append(startNode)

    while toVisit:
        currentNode = toVisit.pop(0)
        visited.append(currentNode)
        if currentNode == goal:
            break
        for child in tree[currentNode]:
            if child not in visited:
                toVisit.append(child)
    print(f"Nodes Visited: {visited}")
    print(f"Nodes Still in Queue: {toVisit}")

bfs(visited,tree,5,7)