class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n

        rotate = nums[-k:] + nums[:-k]
        for i in range(n):
            nums[i] = rotate[i]
