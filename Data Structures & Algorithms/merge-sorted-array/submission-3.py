class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        output = []
        left = 0
        right = 0
        while left < m and right < n:
            if nums1[left] < nums2[right]:
                output.append(nums1[left])
                left += 1
            else:
                output.append(nums2[right])
                right += 1

        while left < m:
            output.append(nums1[left])
            left += 1

        while right < n:
            output.append(nums2[right])
            right += 1

        nums1[:] = output