to_graph=[1,1,4,1,2,3,5,]
from_graph=[2,3,6,6,4,5,6]
weights=[1,1,4,1,2,2,3]
total_cost=sum(weights)
graph=[]

for i in range(len(to_graph)):
    graph.append([weights[i],to_graph[i],from_graph[i]])

graph.sort()

visited=set()
mc_sp_tree=[]
min_cost=0

for i in range(len(graph)):
    if graph[i][1] not in visited or graph[i][2] not in visited:
        mc_sp_tree.append(graph[i])
        visited.add(graph[i][1])
        visited.add(graph[i][2])
        min_cost+=graph[i][0]

print(mc_sp_tree)
print(min_cost)
print(total_cost-min_cost)
        