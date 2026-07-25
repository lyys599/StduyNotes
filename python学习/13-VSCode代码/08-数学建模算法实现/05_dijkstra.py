# 本文件对应同名主题笔记。建议先自己手敲，再运行本文件核对。
import heapq

graph = {
    "A": [("B", 2), ("C", 5)],
    "B": [("C", 1), ("D", 4)],
    "C": [("D", 1)],
    "D": [],
}
distances = {node: float("inf") for node in graph}
distances["A"] = 0
queue = [(0, "A")]
while queue:
    distance, node = heapq.heappop(queue)
    if distance != distances[node]:
        continue
    for neighbor, weight in graph[node]:
        candidate = distance + weight
        if candidate < distances[neighbor]:
            distances[neighbor] = candidate
            heapq.heappush(queue, (candidate, neighbor))
print(distances)
