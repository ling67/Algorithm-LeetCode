class Solution {

    private static final String[] phone = new String[] { "", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};

    public List<String> letterCombinations(String digits) {
        List<String> res = new ArrayList<>();
        if (digits == null || digits.length() == 0) return res;
        char[] input = digits.toCharArray();
        StringBuilder sb = new StringBuilder();
        dfs(input, sb, 0, res);
        return res;
    }

    private void dfs(char[] input, StringBuilder sb, int index, List<String> res) {
        if (index == input.length) {
            res.add(sb.toString());
            return;
        }

        int curNumber = input[index] - '0';
        String curOptions = phone[curNumber];
        int len = sb.length();

        //这个for loop是根据当前字符取不取，跟permutation 和 subset不一样
        for (int i = 0; i < curOptions.length(); i++) { 
            sb.append(curOptions.charAt(i));
            dfs(input, sb, index + 1, res);
            sb.setLength(len);
        }
    }
}
