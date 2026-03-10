class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])

        arrow = 1
        arrow_position = points[0][1]

        for s, e in points:
            if s > arrow_position:
                arrow += 1
                arrow_position = e
            
        return arrow