import java.util.Map;
import java.util.HashMap;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> mapper = new HashMap<Integer, Integer>();
        int numsLen = nums.length;
        for (int i = 0; i < numsLen; i++) {
            mapper.put(nums[i], i);
        }
        for (int i = 0; i < numsLen; i++) {
            int complement = target - nums[i];
            if (mapper.containsKey(complement)
            && mapper.get(complement) != i) {
                return new int[] {i, mapper.get(target - nums[i])};
            }
        }
        return new int[] {};
    }
}