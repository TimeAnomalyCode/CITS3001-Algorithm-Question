#!/usr/bin/env python3
import sys
from collections import deque


def fail(msg):
    print(msg)
    sys.exit(43)


def topological_sort(adj):
    n = len(adj)
    indegree = [0] * n
    res = []
    queue = deque()

    for i in range(n):
        for next_node in adj[i]:
            indegree[next_node] += 1

    for i in range(n):
        if indegree[i] == 0:
            queue.append(i)

    # Kahn's algorithm
    while queue:
        top = queue.popleft()
        res.append(top)

        for next_node in adj[top]:
            indegree[next_node] -= 1
            if indegree[next_node] == 0:
                queue.append(next_node)

    return len(res) == n


adjlist = []
start_node = ()
dictionary = []

# Nodes, relations, dictionary
line = sys.stdin.readline()
node_relation_dictionary_line = line.split()
if len(node_relation_dictionary_line) != 3:
    fail("Nodes, Relations and Dictionary are not present / too many")
elif not all(p.isdigit() for p in node_relation_dictionary_line):
    fail("Nodes, Relations and Dictionary are not digits")

adjlist = [[] for _ in range(int(node_relation_dictionary_line[0]))]

# Dictionary
line = sys.stdin.readline()
dictionary_line = line.split()
if dictionary_line != sorted(dictionary_line):
    fail("The dictionary is not sorted")
elif not all(p.isalpha() for p in dictionary_line) or not all(
    p.isupper() for p in dictionary_line
):
    fail("The dictionary contains other than letters or is not capitalized")

dictionary = dictionary_line

# Start Node
line = sys.stdin.readline()
start_node_line = line.split()
if len(start_node_line) != 2:
    fail("Start Node is not present / too many")
elif not start_node_line[0].isdigit():
    fail("Start Node number is not a digit")
elif not start_node_line[1].isalpha() or not start_node_line[1].isupper():
    fail("Start Node letter is not a letter or capitalized")

start_node = (start_node_line[0], start_node_line[1])

# Relations
for _ in range(int(node_relation_dictionary_line[1])):
    line = sys.stdin.readline()
    relations_line = line.split()

    if len(relations_line) != 3:
        fail("One of the relations is not present / too many")
    elif not relations_line[0].isdigit():
        fail("Source node is not a digit")
    elif not relations_line[1].isdigit():
        fail("Destination node is not a digit")
    elif not relations_line[2].isalpha() or not relations_line[2].isupper():
        fail("Letter is not a letter or capitalized")

    adjlist[int(relations_line[0])].append(int(relations_line[1]))

if not topological_sort(adjlist):
    fail("The Graph is not a DAG and contains cycles")

sys.exit(42)
