# Using a Python dictionary to act as an adjacency list
graph = {           #Defining a graph in this way! 
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}

visited = set() # Set to keep track of visited nodes of graph.

def dfs(visited, graph, node):  #function for dfs 
    if node not in visited:
        print (node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)  #Recusion! 
# Driver Code
print("Following is the Depth-First Search")
dfs(visited, graph, '8')

# PSEUDOCODE FOR THE DFS
'''
DFS(G, u)                   #There is a Graph and Unvisited List[]
    u.visited = true
    for each v ∈ G.Adj[u]
        if v.visited == false
                               #Same function calling himself again
            DFS(G,v)            # Recursion is used ! 
init() {
    For each u ∈ G
        u.visited = false
     For each u ∈ G
       DFS(G, u)
}
'''