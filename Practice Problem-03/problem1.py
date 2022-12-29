file= open('Task-01_input_file.txt','r')
node= int(file.readline())
edge= int(file.readline())

given=[]
for i in file:
    connected=i.split()
    num= int(connected[0])
    var= int(connected[1])
    given.append([num,var])
file.close()
class graph:
    def __init__(self,y):
        self.adj_connection=[[] for i in range(y+1)]
    def edge_added_with(self,a,b):
        self.adj_connection[a].append(b)

graph=graph(node)
for e in given:
     graph.edge_added_with(e[0], e[1])