/*
Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

A palindrome string is a string that reads the same backward as forward.

 

Example 1:

Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]
Example 2:

Input: s = "a"
Output: [["a"]]
*/

class Solution {
    public List<List<String>> partition(String s) {
        List<List<String>> results = new ArrayList<>();
        if (s == null) {
            return results;
        }
        help(s, 0, new ArrayList<String>(), results);
        return results;
    }
    
    //从S的startIndex这个位置去切分，后面一段切成一个个回文串，前面切的已经放在partition里面了，一起放在result
    private void help(String s,
                      Integer startIndex,
                      List<String> partition,
                      List<List<String>> results) {
        
        if (startIndex == s.length()) {
            results.add(new ArrayList<String>(partition));
        }
        
        for (int i = startIndex; i < s.length(); i++) {
            String subString = s.substring(startIndex, i + 1);
            if (!isPslindrome(subString)) {
                continue;
            }
            partition.add(s.substring(startIndex, i + 1));
            help(s, i + 1, partition, results);
            partition.remove(partition.size() - 1);
        } 
    }
    
    //判断s是不是回文串，回文串就是对称的字符串
    private boolean isPslindrome(String s) {
        for (int i = 0, j = s.length() - 1; i < j; i++, j--) {
            if (s.charAt(i) != s.charAt(j)) {
                return false;
            }
        }
        return true;
    }
}
