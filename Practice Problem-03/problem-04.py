file= open('Task-04_input_file.txt', 'r')
read= int(file.readline())
Tnode_1= 0
Tnode_2= 0
list1= []
list2= []
for i in range(read):
    x=file.readline().split()
    if i==0:
        gr1=int(x[0])
        Tnode_1+=gr1
        graph_01= int(x[1])
        for j in range(graph_01):
            node_connect= file.readline().split()
            node_01= int(node_connect[0])
            node_02= int(node_connect[1])
            list1.append([node_01, node_02])
            list1.append([node_02, node_01])
    if i==1:
        gra2= int(x[0])
        Tnode_2+= gra2
        graph_02= int(x[1])
        for i in range(graph_02):
            node_connect= file.readline().split()
            node_01= int(node_connect[0])
            node_02= int(node_connect[1])
            list2.append([node_01, node_02])
            list2.append([node_02, node_01])
#-----------------------------------------------
class Graph:
    def __init__(self, T_nodes_num):
        self.adj_connection = [[] for j in range(T_nodes_num + 1)]

    def edge_added_with(self, a, b):
        self.adj_connection[a].append(b)

graph1 = Graph(int(Tnode_1))
for y in list1:
    graph1.edge_added_with(y[0], y[1])
graph2 = Graph(Tnode_2)
for y in list2:
    graph2.edge_added_with(y[0], y[1])

#------------------------------------------
printed1 = [] #for graph -01
def Graph1_bfs(visited, graph, node, end):
    queue_list = []
    visited[node] = 1
    queue_list.append(node)
    while len(queue_list):
        a = queue_list.pop(0)
        printed1.append(a)
        if a == end:
            return
        for idx in graph.adj_connection[a]:
            if visited[idx] == 0:
                visited[idx] = 1
                if idx == 4:
                    queue_list.pop(-1)
                    queue_list.append(idx)
                else:
                    queue_list.append(idx)

given = [0 for i in range(Tnode_1+1)]
source= list1[0][0]
point= Tnode_1
Graph1_bfs(given, graph1, source, point)
#----------------------------------------------------------------------

num= [] #for graph-02
def Graph2_bfs(visited,graph,node,end):
    queue_list = []
    visited[node] = 1
    queue_list.append(node)
    while len(queue_list):
        a=queue_list.pop(0)
        num.append(a)
        if a== end:
            return
        for idx in graph.adj_connection[a]:
            if visited[idx]== 0:
                visited[idx]= 1
                if idx==4:
                    queue_list.pop(-1)
                    queue_list.append(idx)
                else:
                    queue_list.append(idx)

given_2 = [0 for i in range(Tnode_2+1)]
source_node2 = list2[0][0]
end_point2 = Tnode_2
Graph2_bfs(given_2, graph2, source_node2, end_point2)
file.close()

#------------------------------------------------------------------------
output_file = open('problem-04_output.txt', 'w')
grp1_minimum_numberOFbridges = len(printed1)-1
output_file.write(f"{grp1_minimum_numberOFbridges}\n")
grp2_minimum_numberOFbridges = len(num)-1
output_file.write(f"{grp2_minimum_numberOFbridges}")
output_file.close()
