// Solution 1: string transfer to char[], sort array, then compare the array.

class Solution {
    public boolean isAnagram(String s, String t) {
        char[] ch1 = s.toCharArray();
        char[] ch2 = t.toCharArray();
        Arrays.sort(ch1);
        Arrays.sort(ch2);
        return Arrays.equals(ch1, ch2);   //length is the same, and every element in the same index is same 
    }
}


//Solution 2:  

I create array of ints with size 26 for all lowercase letters.
In the first loop I count occurences of letters in the first string by incrementing corresponding int in array. For example, if the letter (char) is 'b', then 'b' - 'a' is equal to 1. So, I increment value with index 1: array[1]++.
In the second loop I do the same, but decrement for each letter.
In the third loop I make sure that all values in array are 0. If yes, then the answer is true. If not, then the given strings are not anagrams.

class Solution {
    public boolean isAnagram(String s, String t) {
        int[] a = new int[26];
        for (char c : s.toCharArray()) {
            a[c - 'a']++;
        }
        for (char c : t.toCharArray()) {
            a[c - 'a']--;
        }
        for (int n : a) {
            if (n != 0) return false;
        }
        return true;
    }
}
