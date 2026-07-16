class Solution {
    public void reverseString(char[] s) {
        int left = 0;
        int right = s.length - 1;
        while (left < right) {
                char leftChar = s[left];
                char rightChar = s[right];
                s[left] = rightChar;
                s[right] = leftChar;
                left += 1;
                right -= 1;
        }
    }
}