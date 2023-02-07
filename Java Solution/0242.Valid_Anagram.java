// Solution: string transfer to char[], sort array, then compare the array.

class Solution {
    public boolean isAnagram(String s, String t) {
        char[] ch1 = s.toCharArray();
        char[] ch2 = t.toCharArray();
        Arrays.sort(ch1);
        Arrays.sort(ch2);
        return Arrays.equals(ch1, ch2);   //length is the same, and every element in the same index is same 
    }
}
