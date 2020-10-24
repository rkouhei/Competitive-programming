import networkx as nx

N, u, v = map(int, input().split())
tree = nx.Graph()
for i in range(N-1) :
  tmp = list(map(int, input().split()))
  tree.add_node(tmp[0])
  tree.add_node(tmp[1])
  tree.add_edge(tmp[0],tmp[1])

print(tree.nodes)
print(tree.edges)

cnt = 0
print(tree[2])
# while u != v :
#   takahashi = tree[u]

#   aoki = tree[v]