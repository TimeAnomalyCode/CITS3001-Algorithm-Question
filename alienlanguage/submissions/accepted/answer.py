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


def binary_search(arr, x):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = low + (high - low) // 2

        if arr[mid] == x:
            return mid

        elif arr[mid] < x:
            low = mid + 1

        else:
            high = mid - 1

    return -1


# O(w log w)
message = [0]
plus_index = 0
final_index = 0
for w in words:
    marker = w[-1:]
    if w.endswith(("+", ".")):
        w = w[:-1]

    index = binary_search(dictionary, w)

    if index == -1:
        continue

    if marker == "+":
        plus_index += index

    elif marker == ".":
        final_index = index

    message.append(index)

# O(w log w)
message.sort()
if final_index > 0:
    message.append(final_index)
message[0] += plus_index
print("".join(str(m) for m in message))
