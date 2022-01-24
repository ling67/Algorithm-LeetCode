/*
A gene string can be represented by an 8-character long string, with choices from 'A', 'C', 'G', and 'T'.

Suppose we need to investigate a mutation from a gene string start to a gene string end where one mutation is defined as one single character changed in the gene string.

For example, "AACCGGTT" --> "AACCGGTA" is one mutation.
There is also a gene bank bank that records all the valid gene mutations. A gene must be in bank to make it a valid gene string.

Given the two gene strings start and end and the gene bank bank, return the minimum number of mutations needed to mutate from start to end. If there is no such a mutation, return -1.

Note that the starting point is assumed to be valid, so it might not be included in the bank.

 

Example 1:

Input: start = "AACCGGTT", end = "AACCGGTA", bank = ["AACCGGTA"]
Output: 1
Example 2:

Input: start = "AACCGGTT", end = "AAACGGTA", bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]
Output: 2
Example 3:

Input: start = "AAAAACCC", end = "AACCCCCC", bank = ["AAAACCCC","AAACCCCC","AACCCCCC"]
Output: 3
*/

class Solution {
    public int minMutation(String start, String end, String[] bank) {
        
        if (start.equals(end)) {
            return 0;
        }
        
        Queue<String> queue = new LinkedList<>();
        Set<String> hash = new HashSet();
        
        Set<String> dict = new HashSet<>();
        for (String str: bank) {
            dict.add(str);
        }    
    
        queue.offer(start);
        hash.add(start);
        
        int depth = 0;
        while (!queue.isEmpty()) {
            depth++;
            int size = queue.size();
            for (int i = 0; i < size; i++) {
                String head = queue.poll();
                for (String next : getNext(head, dict)) {
                    if (hash.contains(next)) {
                        continue;
                    }
                    if (next.equals(end)) {
                        return depth;
                    }
                    hash.add(next);
                    queue.offer(next);
                }
            }
        }
        return -1;
    }
  
    //获取str的下一个
    private ArrayList<String> getNext(String word, Set<String> dict) {
        ArrayList<String> nextWords = new ArrayList<>();
        for (char c = 'A'; c <= 'Z'; c++) {
            for (int i = 0; i < word.length(); i++) {
                if (c == word.charAt(i)) {
                    continue;
                }
                String newWord = replace(word, i, c);
                if (dict.contains(newWord)) {
                    nextWords.add(newWord);
                }
            }
        }
       return nextWords;
    }
    
    private String replace(String word, int index, char c) {
        char[] chars = word.toCharArray();
        chars[index] = c;
        return new String(chars);
    }
    
}
