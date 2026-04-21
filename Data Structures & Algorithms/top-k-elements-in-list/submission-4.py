class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            if num in counts:
                counts[num] += 1
            elif num not in counts:
                counts[num] = 1
        
        keys = [key for key in counts.keys()]
        values = [v for v in counts.values()]

        result = []
        for t in range(k):
            max = 0
            target = 0
            for i in range(len(values)):
                if values[i] > max:
                    max = values[i]
                    target = i

            result.append(keys[target])

            keys.pop(target)
            values.pop(target)

        return result