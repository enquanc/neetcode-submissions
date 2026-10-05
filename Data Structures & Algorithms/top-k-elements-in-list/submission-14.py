class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            if num not in counts:
                counts[num] = 1
            else:
                counts[num] += 1
        sorted_counts = sorted(counts.items(), key = lambda x :x[1], reverse = True)

        ans = []
        for num, freq in sorted_counts[:k]:
            ans.append(num)
        return ans