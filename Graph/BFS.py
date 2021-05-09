# BFS algorithm in Python

# BFS pseudocode
import collections
def bfs(graph, root,BFS):

    visited = set()
    queue = collections.deque([root])
    visited.add(root)

    while queue:
        vertex = queue.popleft()
        DFS.append(vertex)
        # print(str(vertex) + " ", end="")

        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)
    return DFS
if __name__ == '__main__':
    BFS = []
    graph = {0: [1, 2], 1: [2], 2: [3], 3: [1, 2]}
    print("Following is Breadth First Traversal: ")
    print(bfs(graph, 0,BFS))