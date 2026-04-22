class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        result = []
        def find(index, total, path):
            
            if index == len(nums):
                return

            if total > target:
                return 
            elif total < target:
                # 不加
                # find(index, total, path)
                if index+1 < len(nums):
                    find(index+1, total, path)
                # 加
                path.append(nums[index])
                find(index, total + nums[index], path)
                if index+1 < len(nums):
                    find(index+1, total + nums[index], path)
                path.pop()
            elif total == target:
                if path[:] not in result:
                    result.append(path[:])

        
        find(0, 0, [])
        return result