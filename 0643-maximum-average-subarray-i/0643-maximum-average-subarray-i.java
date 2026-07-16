class Solution {
    public double findMaxAverage(int[] nums, int k) {
        int left = 0;
        int right = k - 1;
        if (right - left == 0) {
            return Arrays.stream(nums).max().getAsInt();
        }
        double curr = Arrays.stream(Arrays.copyOfRange(nums, left, k)).sum();
        double answer = curr;
        while (right < nums.length - 1) {
            curr = curr - nums[left] + nums[right + 1];
            answer = Math.max(answer, curr);
            left += 1;
            right += 1;
        }

        return answer / k;
    }
}