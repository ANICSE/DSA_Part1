class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def clone_graph(self, node: 'Node') -> 'Node':
        oldToNew = {}

        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]
            
            copy = Node(node.val)
            oldToNew[node] = copy

            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            
            return copy
        
        return dfs(node) if node else None

def print_graph(node: 'Node'):
    visited = set()

    def dfs(node):
        if node in visited:
            return
        visited.add(node)
        print(f"Node({node.val}) neighbors -> {[n.val for n in node.neighbors]}")
        for neighbor in node.neighbors:
            dfs(neighbor)

    dfs(node)


def main():
    # Create original graph manually
    # Example: 1 -- 2
    #          |    |
    #          4 -- 3

    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)

    node1.neighbors = [node2, node4]
    node2.neighbors = [node1, node3]
    node3.neighbors = [node2, node4]
    node4.neighbors = [node1, node3]

    print("Original graph:")
    print_graph(node1)

    sol = Solution()
    cloned = sol.clone_graph(node1)

    print("\nCloned graph:")
    print_graph(cloned)


if __name__ == "__main__":
    main()
