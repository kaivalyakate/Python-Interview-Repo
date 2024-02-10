def countComponents(n: int, edges: list[list[int]]) -> int:
    adj_list = {i: [] for i in range(n)}
    for edge in edges:
        adj_list[edge[0]].append(edge[1])
        adj_list[edge[1]].append(edge[0])

    visited = set()

    def dfs(node):
        if node in visited:
            return None
        
        visited.add(node)
        for i in adj_list[node]:
            dfs(node=i)

    connected_components = 0
    for i in range(0, n):
        if i not in visited:
            connected_components += 1
            dfs(i)
    
    return connected_components


if __name__ == "__main__":
    print(countComponents(n=5, edges=[[0,1],[1,2],[2,3],[3,4]]))