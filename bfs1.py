def bfs(graph,start,goal):
    q=[]
    visited=[]
    q.append(start)
    visited.append(start)
    path=""
    found=False
    while q:
        m=q.pop(0)
        path+=m+" "
        if m==goal:
            found=True
            break;
        for neighbour in graph.get(m,[]):
            if neighbour not in visited:
                q.append(neighbour)
                visited.append(neighbour)
    if found:
        print("goal node is found")
        print("path: ",path)
    else:
        print("goal node not found")
n=int(input("enter the no.of nodes"))
graph={}
print("enter the node and its childs")
for i in range(1,n+1):
    print("node-",i,end='\t')
    key=input()
    print(end='\t')
    value=input().split()
    graph[key]=value
start=input('enter the starting node')
goal=input('enter goal node')
bfs(graph,start,goal)        
        
    
    








