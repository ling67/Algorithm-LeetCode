// split method
class Solution {
    public String reverseWords(String s) {
        String arr[] = s.split(" ");
        StringBuilder str = new StringBuilder();
        for (int i = arr.length - 1; i >= 0; i--) {
            if (arr[i].length() > 0) str.append(arr[i] + " ");
        }
        return str.toString().trim();
    }
}

//two point
