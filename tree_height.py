def compute_tree_height(n, parents):
    # Create an adjacency list to represent the tree
    tree = [[] for _ in range(n)]
    for i in range(n):
        if parents[i] != -1:
            tree[parents[i]].append(i)

    # Define a recursive function to calculate the height
    def calculate_height(node):
        if not tree[node]:
            return 1
        else:
            subtree_heights = [calculate_height(child) for child in tree[node]]
            return 1 + max(subtree_heights)

    # Find the height starting from the root
    root = parents.index(-1)
    tree_height = calculate_height(root)

    return tree_height

# Input
while True:
    try:
        n = int(input())
        parents = list(map(int, input().split()))
        
        # Check if the input is valid
        if len(parents) != n:
            raise ValueError("Invalid input length. Please enter exactly n parent nodes.")
        
        # Output
        result = compute_tree_height(n, parents)
        print(result)
        break
    except ValueError as e:
        print(f"Error: {e}. Please enter valid integer values.")
