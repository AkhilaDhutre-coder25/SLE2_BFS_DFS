from collections import deque
import time

# Same 20-node graph
graph = {
    0: [1, 2],
    1: [3, 4],
    2: [5, 6],
    3: [7, 8],
    4: [9, 10],
    5: [11, 12],
    6: [13, 14],
    7: [15],
    8: [16],
    9: [17],
    10: [18],
    11: [19],
    12: [],
    13: [],
    14: [],
    15: [],
    16: [],
    17: [],
    18: [],
    19: []
}


def bfs(start, goal):
    queue = deque([start])
    visited = {start}
    nodes_expanded = 0

    while queue:
        node = queue.popleft()
        nodes_expanded += 1

        if node == goal:
            return nodes_expanded

        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

    return nodes_expanded


# Number of repetitions for profiling
REPETITIONS = 50000

times = []

for run in range(3):

    start_time = time.perf_counter()

    for _ in range(REPETITIONS):
        nodes = bfs(0, 19)

    end_time = time.perf_counter()

    elapsed = (end_time - start_time) * 1000
    times.append(elapsed)


print("========== BFS RESULTS ==========")
print("Run 1:", times[0], "ms")
print("Run 2:", times[1], "ms")
print("Run 3:", times[2], "ms")

average = sum(times) / 3

print("Average:", average, "ms")
print("Nodes Expanded (one search):", nodes)
print("Total Repetitions:", REPETITIONS)