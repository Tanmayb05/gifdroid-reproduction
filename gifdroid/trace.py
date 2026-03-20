import json
import logging
import time
from collections import defaultdict
import itertools

logger = logging.getLogger('gifdroid.trace')


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)
        self.all_paths = []

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def printAllPathsUtil(self, u, d, visited, path):
        """DFS helper: accumulates all simple paths from u to d."""
        visited[u] = True
        path.append(u)
        if u == d:
            self.all_paths.append(path.copy())
        else:
            for i in self.graph[u]:
                if not visited[i]:
                    self.printAllPathsUtil(i, d, visited, path)
        path.pop()
        visited[u] = False

    def printAllPaths(self, s, d):
        """Return all simple paths from s to d via DFS."""
        visited = [False] * self.V
        path = []
        self.printAllPathsUtil(s, d, visited, path)
        return self.all_paths


def read_graph(utg):
    """Parse the UTG JSON and build a directed Graph of screen transitions."""
    t0 = time.time()
    with open(utg, 'r') as f:
        parsed_json = json.loads(f.read())

    vertices = 0
    graph = []
    for event in parsed_json['events']:
        if 'sourceScreenId' not in event or 'destinationScreenId' not in event:
            continue
        s = int(event['sourceScreenId'])
        d = int(event['destinationScreenId'])
        graph.append([s, d])
        if s > vertices:
            vertices = s
        if d > vertices:
            vertices = d

    g = Graph(vertices + 1)
    for s, d in graph:
        g.addEdge(s, d)

    elapsed = time.time() - t0
    logger.debug(f'read_graph: {len(graph)} edges, {vertices + 1} vertices loaded in {elapsed:.2f}s')
    return g


def find_all_paths_in_graph(graph, s, d):
    """Find all simple paths from node s to node d in the UTG."""
    return graph.printAllPaths(s, d)


def calulcate_lcs(X, Y):
    """
    Compute the Longest Common Subsequence of two screen-ID sequences.
    Used to score how well a UTG path covers the observed keyframe sequence.
    """
    m = len(X)
    n = len(Y)
    L = [[0 for x in range(n + 1)] for x in range(m + 1)]
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif X[i - 1] == Y[j - 1]:
                L[i][j] = L[i - 1][j - 1] + 1
            else:
                L[i][j] = max(L[i - 1][j], L[i][j - 1])
    index = L[m][n]
    lcs = [""] * (index + 1)
    lcs[index] = ""
    i = m
    j = n
    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:
            lcs[index - 1] = X[i - 1]
            i -= 1
            j -= 1
            index -= 1
        elif L[i - 1][j] > L[i][j - 1]:
            i -= 1
        else:
            j -= 1
    lcs = lcs[:-1]
    return lcs


def find_execution_trace(utg, index_sequence):
    """
    Find the shortest execution trace(s) that best reproduce the observed keyframe sequence.
      1. Build the UTG graph from the JSON file
      2. Enumerate all paths from screen 0 to the last observed screen
      3. Score each path by LCS length against the keyframe index sequence
      4. Return the shortest path(s) with the maximum LCS score, deduplicated
    """
    t0 = time.time()
    logger.info(f'find_execution_trace: target sequence {index_sequence}')

    # Step 1: build graph and enumerate all paths to the target screen
    graph = read_graph(utg)
    t_paths = time.time()
    paths = find_all_paths_in_graph(graph, 0, index_sequence[-1])
    logger.debug(f'find_execution_trace: {len(paths)} candidate paths found in {time.time() - t_paths:.2f}s')

    # Step 2: score each path by LCS with the observed keyframe sequence
    max_lcs = 0
    max_lcs_paths = []
    for path in paths:
        lcs = calulcate_lcs(path, index_sequence)
        if len(lcs) > max_lcs:
            max_lcs = len(lcs)
            max_lcs_paths = [path]
        elif len(lcs) == max_lcs:
            max_lcs_paths.append(path)

    # Step 3: among best-LCS paths, keep only the shortest (fewest steps)
    if not max_lcs_paths:
        elapsed = time.time() - t0
        logger.warning(
            f'find_execution_trace: no paths found from node 0 to screen {index_sequence[-1]} '
            f'in the UTG (sequence={index_sequence}). Returning empty trace. ({elapsed:.2f}s)'
        )
        return []
    min_len = min(map(len, max_lcs_paths))
    execution_trace = [p for p in max_lcs_paths if len(p) == min_len]
    execution_trace.sort()
    execution_trace = list(k for k, _ in itertools.groupby(execution_trace))

    elapsed = time.time() - t0
    logger.info(
        f'find_execution_trace: {len(execution_trace)} trace(s) found '
        f'(LCS={max_lcs}, length={min_len}) in {elapsed:.2f}s'
    )
    return execution_trace




if __name__ == "__main__":
    # Debug
    graph = Graph(9)
    graph.addEdge(0, 1)
    graph.addEdge(1, 2)
    graph.addEdge(2, 3)
    graph.addEdge(3, 4)
    graph.addEdge(4, 3)
    graph.addEdge(4, 5)
    graph.addEdge(5, 6)
    graph.addEdge(6, 1)
    graph.addEdge(2, 7)
    graph.addEdge(7, 8)
    graph.addEdge(8, 4)
    graph.addEdge(8, 5)
    index = [2,4,5]
    paths = find_all_paths_in_graph(graph, 0, index[-1])
    print(paths)
    trace = find_execution_trace(index, paths)
    print(trace)



    None
