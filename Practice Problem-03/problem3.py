from problem1 import graph, node
file= open('problem-03output.txt','w')
here=[]
def DFS_Visit(graph,node,end,visit):
    visit[node]=1
    here.append(node)
    if node==end:
        return
    for i in graph.adj_connection[node]:
        if visit[end]== 1:
            return
        if visit[i]== 0:
            DFS_Visit(graph,i,end,visit)

def DFS(graph,end,node,visit):
    for a in graph.adj_connection[node]:
        if visit[a]== 0:
            DFS_Visit(graph,node,end,visit)
        else:
            return
visit=[0]*(node+1)
DFS(graph,12,1,visit)
result= " ".join(str(i) for i in here)
file.write("Places: ")
file.write(result)
file.close()