from problem1 import graph, node
file= open('problem2output.txt', 'w')
file.write("Places: ")
here=[]
def BFS(given,graph,node,end):
    que=[]
    given[node]= 1
    que.append(node)
    while len(que)!= 0:
        x=que.pop(0)
        file.write(f'{x} ')
        here.append(x)
        if x==end:
            break
        for i in graph.adj_connection[x]:
            if given[i]==0:
                given[i]=1
                que.append(i)
given=[0]*(node+1)
source=1
end=node
BFS(given,graph,source,end)
file.close()