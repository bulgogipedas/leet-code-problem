class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_indices = {}  # Dictionary to store indices of visited numbers
        
        for i, num in enumerate(nums):
            complement = target - num
            
            if complement in num_indices:
                return [num_indices[complement], i]
            
            num_indices[num] = i  # Save the index of the current number in the dictionary
        
        # If no solution is found
        return []
