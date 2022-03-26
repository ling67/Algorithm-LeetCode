/*
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.



 

Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:

Input: digits = ""
Output: []
Example 3:

Input: digits = "2"
Output: ["a","b","c"]

*/

//backtrack python
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def backtrack(curr_idx, curr_comb):
            if curr_idx == len(digits):
                res.append("".join(curr_comb))   # string is immutable so don't need deep copy
                return
            for ch in phone[digits[curr_idx]]:
                curr_comb.append(ch)
                backtrack(curr_idx + 1, curr_comb)
                curr_comb.pop()
        
        if not digits:
            return[]
        
        phone = {
         '2': ['a', 'b', 'c'],
         '3': ['d', 'e', 'f'],
         '4': ['g', 'h', 'i'],
         '5': ['j', 'k', 'l'],
         '6': ['m', 'n', 'o'],
         '7': ['p', 'q', 'r', 's'],
         '8': ['t', 'u', 'v'],
         '9': ['w', 'x', 'y', 'z']}
        
        res = []
        backtrack(0, [])
        return res
        

//version dfs+backtrack
class Solution {
    
    private static final String[] phone = new String[] { "", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};
    
    public List<String> letterCombinations(String digits) {
        List<String> result = new ArrayList<>();
        if(digits == null || digits.length() == 0) return result;
        char[] input = digits.toCharArray();
        StringBuilder sb = new StringBuilder();
        dfs(result, input, 0, sb);
        return result;
    }
    
    private void dfs(List<String> result, char[] input, int index, StringBuilder sb){
        
        if (index == input.length) {
            result.add(sb.toString());
            return;
        }
        
        int curNumber = input[index] - '0';  
        String curOptions = phone[curNumber];
        int len = sb.length();

        for (int i = 0; i < curOptions.length(); i++) {
            sb.append(curOptions.charAt(i));
            dfs(result, input, index + 1, sb);
            sb.setLength(len);
        }  
    }
}

