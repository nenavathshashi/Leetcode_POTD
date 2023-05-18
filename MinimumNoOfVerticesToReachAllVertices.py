from collections import defaultdict
class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        incoming_edges=set()
        total_edges=len(edges)
        for i in range(total_edges):
            incoming_edges.add(edges[i][1])
        non_incoming_edges=[]
        for i in range(n):
            if i not in incoming_edges:
                non_incoming_edges.append(i)
        return non_incoming_edges
