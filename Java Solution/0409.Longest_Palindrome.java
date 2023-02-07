//Solution: Hashmap record the frequency of character

class Solution {
    public int longestPalindrome(String s) {
        char[] ch = s.toCharArray();
        Map<Character, Integer> map = new HashMap<>();
        int sum = 0;
        int flag = 0;
        for (char c : ch) {
            map.put(c, map.getOrDefault(c, 0) + 1);
        }
        for (Map.Entry<Character, Integer> entry : map.entrySet()) {
            if (entry.getValue() % 2 == 0) {
                sum += entry.getValue();
            } else {
                sum += entry.getValue() - 1;
                flag = 1;
            }
        }
        return sum + flag;
    }
}

