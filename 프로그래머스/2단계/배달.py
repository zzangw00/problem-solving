def solution(N, road, K):

    def smallestNode(N):
        min = 1e9
        index = 0
        for i in range(1, N + 1):
            if distance[i] < min and not visited[i]:
                min = distance[i]
                index = i
        return index

    def dijkstra(N, start):
        distance[start] = 0
        visited[start] = True
        for i in graph[start]:
            distance[i[0]] = i[1]
        for i in range(N - 1):
            now = smallestNode(N)
            visited[now] = True
            for j in graph[now]:
                cost = distance[now] + j[1]
                if cost < distance[j[0]]:
                    distance[j[0]] = cost

    answer = 0
    graph = []
    for i in range(N + 1):
        graph.append([])
    visited = [False] * (N + 1)
    distance = [int(1e9)] * (N + 1)
    for i in range(len(road)):
        graph[road[i][0]].append([road[i][1], road[i][2]])
        graph[road[i][1]].append([road[i][0], road[i][2]])

    dijkstra(N, 1)

    for i in distance:
        if i <= K:
            answer += 1

    return answer
