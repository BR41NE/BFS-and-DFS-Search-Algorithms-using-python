#represent the info in the form of a graph or trees 
#initialize queues for tracking 
#check for goal 

tree = {
    0 : [1,2],
    1 : [3,4],
    2 : [5,6],
    3 : [],
    4 : [],
    5 : [],
    6 : [],
}
tree1 = {
    0 : []
}
tree2 = {
    0 : [1,2],
    1 : [],
    2 : [],

}

#queues initialization
visited = []
toVisit = []
temp = []
m= 3

def partialTree(tree,index):
    t = {}
    if index == 0:
        t = tree1
    elif index ==1:
        t = tree2
    elif index == 2:
        t = tree
    return t


def dfs(visited,tree,startNode,goal):
    toVisit.append(startNode)
    main = 16
    numberOfNodees = len(tree)
    level = 0
    while toVisit:
        #set current location by popping first 
        # in queue
        
        currentNode = toVisit.pop(0)
        visited.append(currentNode)
        if currentNode == goal:
            main = currentNode
            break
        if level >= numberOfNodees:
            break
        for eachChild in tree[currentNode]:
            if eachChild not in visited:
                temp.append(eachChild)
        if len(toVisit) != 0:
            for each in toVisit:
                temp.append(each)
            toVisit.clear()
        if len(temp) != 0:
            for each in temp:
                toVisit.append(each)
            temp.clear()
        level+=1
   
    return main

def ifs(visited,tree,startNode,goal,level):
    d = 0
    while d < level:
        print(f"Iteration level: {d} ")
        partT = partialTree(tree,d)
        re = dfs(visited,partT,startNode,goal)
        d+=1
        if re in tree:
            print(f"Nodes Visited: {visited}")
            print(f"Nodes Still in Queue: {toVisit}")
            break
        else:
            print("Goal not in this iteration")
            toVisit.clear()
            temp.clear()
            visited.clear()
        print(" ")
            

ifs(visited,tree,0,5,m)