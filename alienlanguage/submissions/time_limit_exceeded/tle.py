#!/usr/bin/env python3

num_nodes, num_relations, num_dict = map(int, input().split())
dictionary = [""] + input().split()
start_node_val = tuple(input().split())
graph = {}
for _ in range(num_relations):
    src, dst, val = input().split()
    x = graph.setdefault(src, [])
    x.append((dst, val))


# O(V + E)
def all_paths(adj, start):
    results = []

    def dfs(node, path):
        if node not in adj:
            results.append(path)
            return
        for child, value in adj[node]:
            dfs(child, path + value)

    start_node, start_val = start
    dfs(start_node, start_val)
    return results


words: list[str] = all_paths(graph, start_node_val)


def bad_binary_search(arr, x):
    for i, val in enumerate(arr):
        if val == x:
            return i

    return -1


# O(w log w)
message = []
plus_index = 0
final_index = 0
for w in words:
    marker = w[-1:]
    if w.endswith(("+", ".")):
        w = w[:-1]

    index = bad_binary_search(dictionary, w)

    if index == -1:
        continue

    if marker == "+":
        plus_index += index

    elif marker == ".":
        final_index = index

    message.append(index)

# O(w log w)
# message[0] += plus_index
message.sort()
print(plus_index)
if len(message) > 0:
    print("".join(str(m) for m in message))
if final_index > 0:
    print(final_index)
