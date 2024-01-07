# t=int(input())
# for _ in range(t):
# 	n,m=list(map(int,input().split()))
# 	print(min(m,n)+abs(m-n))



from collections import deque



# def BFS(u):
# 		visited = [False for i in range(n+ 1)]
# 		distance = [-1 for i in range(n + 1)]
# 		distance[u] = 0
# 	    queue = deque()
# 	    queue.append(u)
# 	    visited[u] = True

# 	    while queue:
 
#             front = queue.popleft()
 
#             for i in adj[front]:
#                 if not visited[i]:
#                     visited[i] = True
#                     distance[i] = distance[front]+1
#                     queue.append(i)
#         maxDis = 0
 
#         # get farthest node distance and its index
#         for i in range(n):
#             if distance[i] > maxDis:
 
#                 maxDis = distance[i]
#                 nodeIdx = i
 
#         return nodeIdx, maxDis
# def count_leaf_nodes(graph, node, parent=None):
#     if not graph.adjacency_list[node]:
#         # If the node has no neighbors, it is a leaf node
#         return 1

#     leaf_count = 0
#     for neighbor in graph.adjacency_list[node]:
#         if neighbor != parent:
#             leaf_count += count_leaf_nodes(graph, neighbor, node)

#     return leaf_count


# t=int(input())
# for _ in range(t):
# 	n=int(input())

# 	adj = {i: [] for i in range(n)}

# 	for _ in range(n):
# 		u,v=list(map(int,input().split()))
# 		adj[u].append(v)
# 		adj[v].append(u)

# 		starting_node = 1
# 		leaf_node_count = count_leaf_nodes(graph, starting_node)


# from math import ceil

# def main():
#     t = int(input())
    
#     for _ in range(t):
#         n = int(input())
        
#         adj = [[] for _ in range(n + 1)]

#         for _ in range(n - 1):
#             u, v = map(int, input().split())
#             adj[u].append(v)
#             adj[v].append(u)

#         count_leaf = 0
#         for i in range(1, n + 1):
#             if len(adj[i]) == 1:
#                 count_leaf += 1

#         print(ceil(count_leaf / 2.0))

# if __name__ == "__main__":
#     main()

def is_lexicographically_sorted(s):
    return s == ''.join(sorted(s))

def min_cyclic_shifts(s,n):
	if(len(s)==1):
		return -1
	n = len(s)
	s += s  

	min_lexico = s
	min_shifts = 0

	for i in range(1, n):
	    current_shift = s[i:i+n]
	    if current_shift < min_lexico:
	        min_lexico = current_shift
	        min_shifts = i

	return min_shifts

t=int(input())

for _ in range(t):
	n=int(input())
	s=input()
	res = ""
	cr = 0
	while (cr < n):
	    mx = s[cr]
	    for i in range(cr + 1, n):
	        mx = max(mx, s[i])
	    lst = cr

	    for i in range(cr,n):
	        if (s[i] == mx):
	            res += s[i]
	            lst = i

	    cr = lst + 1
	if is_lexicographically_sorted(res):
		print(0)

	else:		
		ans=min_cyclic_shifts(res,n)
		print(ans)