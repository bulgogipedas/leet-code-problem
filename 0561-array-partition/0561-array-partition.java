class Solution {
    public int arrayPairSum(int[] nums) {
        int[] freq = new int[20001];

        // Count frequencies
        for (int num : nums) {
            freq[num + 10000]++;
        }

        int sum = 0;
        boolean take = true;

        // Simulate sorted order from -10000 to 10000
        for (int i = 0; i < freq.length; i++) {
            int value = i - 10000;

            while (freq[i] > 0) {
                if (take) {
                    sum += value;
                }

                take = !take;
                freq[i]--;
            }
        }

        return sum;
    }
}