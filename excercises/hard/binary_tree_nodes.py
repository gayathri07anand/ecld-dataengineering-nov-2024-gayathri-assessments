def type_of_node(N, P, node):
    if node not in N:
        return "Not exist"
    node_index = N.index(node)
    parent = P[node_index]
    if parent == -1:
        return "Root"
    
    
    leaf = [n for n, p in zip(N, P) if p == node]
    if not leaf:
        return "Leaf"
    return "Inner"
    
    
    

# Test cases
print(type_of_node([1, 3, 6, 9, 2, 8, 5], [2, 2, 8, 8, 5, 5, -1], 5))  # "Root"
print(type_of_node([1, 3, 6, 9, 2, 8, 5], [2, 2, 8, 8, 5, 5, -1], 6))  # "Leaf"
print(type_of_node([1, 3, 6, 9, 2, 8, 5], [2, 2, 8, 8, 5, 5, -1], 2))  # "Inner"
print(type_of_node([1, 3, 6, 9, 2, 8, 5], [2, 2, 8, 8, 5, 5, -1], 10))  # "Not exist"
