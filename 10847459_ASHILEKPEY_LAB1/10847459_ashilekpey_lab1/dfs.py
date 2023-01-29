#represent the info in the form of a graph or trees 
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
temp = []
def dfs(visited,tree,startNode,goal):
    toVisit.append(startNode)

    while toVisit:
        #set current location by popping first in queue
        currentNode = toVisit.pop(0)
        #set current as visited
        visited.append(currentNode)
        #check if is goal
        #if goal break
        if currentNode == goal:
            break
        #else
        #put children in temp
        for eachChild in tree[currentNode]:
            if eachChild not in visited:
                temp.append(eachChild)
        #add tovisit to the end
        if len(toVisit) != 0:
            for each in toVisit:
                temp.append(each)
        toVisit.clear()   

        # #move all back to tovisit
        if len(temp) != 0:
            for each in temp:
                toVisit.append(each)
        temp.clear()
           
    print(f"Nodes Visited: {visited}")
    print(f"Nodes Still in Queue: {toVisit}")
dfs(visited,tree,5,8)