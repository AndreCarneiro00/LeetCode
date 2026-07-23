class Solution {
    public int waysToSplitArray(int[] nums) {
        long[] prefixSum = new long[nums.length];
        prefixSum[0] = nums[0];
        for (int i = 1; i < nums.length; i++) {
            prefixSum[i] = prefixSum[i - 1] + nums[i];
        }
        int counter = 0;
        for (int i = 0; i < prefixSum.length - 1; i++) {
            long leftSum = prefixSum[i];
            long rightSum = prefixSum[prefixSum.length - 1] - prefixSum[i];
            if (leftSum >= rightSum) {
                counter++;
            }
        }
        return counter;
    }
}