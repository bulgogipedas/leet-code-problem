class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n  # Mengambil modulus untuk menangani k yang lebih besar dari n
        
        # Fungsi untuk membalikkan bagian dari array
        def reverse(start: int, end: int) -> None:
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start, end = start + 1, end - 1
        
        # Langkah 1: Balikkan seluruh array
        reverse(0, n - 1)
        # Langkah 2: Balikkan bagian pertama dari array
        reverse(0, k - 1)
        # Langkah 3: Balikkan bagian kedua dari array
        reverse(k, n - 1)