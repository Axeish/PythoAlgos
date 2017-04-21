class Graph:
    def __init__(self,value):
        self.value = value
        self.neighbours = []




# def BFS(node, start, end):


a = Graph('a')
b=Graph('b')
c=Graph('c')
d=Graph('d')
e=Graph('e')
a.neighbours.append(b)
a.neighbours.append(c)
b.neighbours.append(d)
b.neighbours.append(e)


#undirected
c.neighbours.append(a)
d.neighbours.append(b)
e.neighbours.append(b)
b.neighbours.append(a)

def BFS(node, start, end):
    queue=[]
    visited =[]