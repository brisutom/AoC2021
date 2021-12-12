from collections import defaultdict


def find_all_paths(graph, start, end, path=[], visited_twice=False):
    path = path + [start]
    if path.count(start) >= 2 and start.islower():
        visited_twice = True
    if start == end:
        return [path]
    if start not in graph:
        return []
    paths = []
    for node in graph[start]:
        if node not in set(path) or node.isupper() or (node != "start" and
                                                       not visited_twice):
            newpaths = find_all_paths(graph, node, end, path, visited_twice)
            for newpath in newpaths:
                paths.append(newpath)
    return paths


lines = [x.strip("\n").split("-") for x in open("input.txt")]
graph = defaultdict(lambda: [])

for node_from, node_to in lines:
    graph[node_from].append(node_to)
    graph[node_to].append(node_from)

all_paths = find_all_paths(graph, "start", "end")
print(len(all_paths))
