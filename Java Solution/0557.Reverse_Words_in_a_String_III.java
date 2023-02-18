class Solution {
    public String reverseWords(String s) {
        StringBuilder sb = new StringBuilder();
        String[] words = s.split(" ");
        for (int i = 0; i < words.length; i++) {
            for (int j = words[i].length() - 1; j >= 0; j--) {
                sb.append(words[i].charAt(j));
            }
            sb.append(" ");
        }
        return sb.toString().trim();
    }
}
