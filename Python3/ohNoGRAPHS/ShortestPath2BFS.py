import sys, heapq
input = sys.stdin.readline

def BFS(adj, src, dest, n, pred, dist):
	queue = []
	visited = [0 for i in range(n)];
	for i in range(n):
		dist[i] = sys.maxsize
		pred[i] = -1
	visited[src] = 1
	dist[src] = 0
	queue.append(src)
	while (len(queue) != 0):
		u = queue[0]
		queue.pop(0)
		for i in range(len(adj[u])):
			if (visited[adj[u][i]] == 0):
				visited[adj[u][i]] = 1
				dist[adj[u][i]] = dist[u] + 1
				pred[adj[u][i]] = u
				queue.append(adj[u][i])
				if (adj[u][i] == dest):
					return 1
	return 0

def solve(adj, s, dest, n):
	pred=[0 for i in range(n)]
	dist=[0 for i in range(n)]
	if (BFS(adj, s, dest, n, pred, dist) == 0):
		return -1	# src and dest are not connected in graph
	path = []
	crawl = dest
	path.append(crawl)
	while (pred[crawl] != -1):
		path.append(pred[crawl])
		crawl = pred[crawl]
	return dist[dest]

def main():
	n = int(input())	# 5
	adj = [[],]
	for i in range(n):
		adj.append(list(map(int, input().split())))
	src, dest = map(int, input().split())
	ans = solve(adj, src, dest, n)
	print(ans)

if __name__ == '__main__':
	main()	
