import heapq


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-stone for stone in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            f = -heapq.heappop(heap)
            s = -heapq.heappop(heap)

            if f != s:
                heapq.heappush(heap, -(f - s))
        
        if heap:
            return -heap[0]
        else:
            return 0

