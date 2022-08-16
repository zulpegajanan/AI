visited = set() 
def dfs(visited, graph, node):   
    if node not in visited:
        print (node, end = " ")
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)
            
visited = [] 
queue = []     
def bfs(visited, graph, node): 
  visited.append(node)
  queue.append(node)
  while queue:          
    m = queue.pop(0) 
    print (m, end = "==>") 
    for neighbour in graph[m]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)


ch=100

while(ch!=4):
     print("\n1.Create A Graph\n2.BFS Search\n3.DFS search\n4.Exit",end=" ")
     ch=int(input())
     if(ch==1):
          total=int(input("enter total number of node in this graph "))
          graph={}
          for i in range(total):
               a=[]
               print("\nhow many node conected to ", i," ==> ")
               con=int(input())
               for x in range(con):
                    node=int(input("enter index :"))
                    a.append(node)
               graph[i]=a

          print(graph)
          
     elif(ch==2):
          root=int(input("enter root node of graph "))
          print("\nFollowing is the Breadth-First Search")
          bfs(visited, graph, root)
     elif(ch==3):
          root=int(input("enter root node of graph "))
          print("Following is the Depth-First Search")
          dfs(visited, graph, root)
     else:
          print("===========** THANK YOU **=============")
