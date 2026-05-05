class Solution:
    def jump(self, nums: List[int]) -> int:
        farthest = 0
        jumps = 0
        current = 0
        for i in range(len(nums)-1):
            farthest = max(farthest, i + nums[i]) # 2 4 4 4 

            if i == current:  # 00 12 22 34 44
                jumps += 1  # 1 1 2 2
                current = farthest # 2 2 4 4

        return jumps 