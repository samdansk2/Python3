graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}

visited=[]
queue=[]

def bfs(graph,visited,node):
    visited.append(node)
    queue.append(node)

    while(queue):
        m=queue.pop(0)#removes 0 index element

        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
print("The Bfs Solution Is:")
bfs(graph,visited,'5')
print(visited)
    
