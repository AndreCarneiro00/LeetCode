import java.util.Map;
import java.util.HashMap;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> mapper = new HashMap<Integer, Integer>();
        int numsLen = nums.length;
        for (int i = 0; i < numsLen; i++) {
            int complement = target - nums[i];
            if (mapper.containsKey(complement)) {
                return new int[] {mapper.get(complement), i};
            }
            mapper.put(nums[i], i);
        }
        return new int[] {};
    }
}