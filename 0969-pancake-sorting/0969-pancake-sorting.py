class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        res = []
    
        for size in range(len(arr), 1, -1):
            max_index = arr.index(max(arr[:size]))

            if max_index != size - 1:
                # flip to front
                arr[:max_index+1] = reversed(arr[:max_index+1])
                res.append(max_index + 1)

                # flip to correct position
                arr[:size] = reversed(arr[:size])
                res.append(size)

        return res