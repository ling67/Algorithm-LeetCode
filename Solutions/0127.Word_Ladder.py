/*
A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.

 

Example 1:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.
Example 2:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: 0
Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.
*/

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)
        if endWord not in word_set:
            return 0
        
        q = collections.deque()
        visited = set()
        q.append(beginWord)
        visited.add(beginWord)
        
        steps = 0
        while len(q) > 0:
            steps += 1
            lens = len(q)
            for _ in range(lens):
                curr_word = q.popleft()
                if curr_word == endWord:
                    return steps
                for next_word in self._get_next(word_set, curr_word):
                    if next_word not in visited:
                        q.append(next_word)
                        visited.add(next_word)
        return 0
    
    def _get_next(self, word_set, curr_word):
        res = []
        for i, ch in enumerate(curr_word):
            for letter in "abcdefghijklmnopqrstuvwxyz":
                if letter == ch:
                    continue
                next_word = curr_word[:i] + letter + curr_word[i+1:]
                if next_word in word_set:
                    res.append(next_word)
        return res
       

class Solution {
    
    //可以转换成起点到终点的最短路径  分层遍历三层循环 1.queue！= null 2.size = queue.size 当前这一层的每个节点 3.for循环出当前循环的每个节点的下一个单词
    public int ladderLength(String beginWord, String endWord, List<String> wordList) {

        if (wordList == null || wordList.size() == 0) {
            return 0;
        }
        
        if (beginWord.equals(endWord)) {
            return 1;
        }
        
        Set<String> dict = new HashSet<>();
        for (String word : wordList) {
            dict.add(word);
        }
        
        dict.add(beginWord);
        dict.add(endWord);
        
        //分层BFS遍历
        HashSet<String> hash = new HashSet<String>();
        Queue<String> queue = new LinkedList<String>();
        queue.offer(beginWord);
        hash.add(beginWord);
        
        int length = 1;
        while(!queue.isEmpty()) {
            length++;
            int size = queue.size();  //记录当前层数大小
            for (int i = 0; i < size; i++) {
                String word = queue.poll();
                for (String nextWord : getNextWords(word, dict)) {
                    if (hash.contains(nextWord)) {
                       continue; 
                    }
                    if (nextWord.equals(endWord)) {
                        return length;
                    }
                    hash.add(nextWord);
                    queue.offer(nextWord);
                }
            }
        }
        return 0;
    }
    
    private ArrayList<String> getNextWords(String word, Set<String> dict) {
        ArrayList<String> nextWords = new ArrayList<String>();
        for (char c = 'a'; c <= 'z'; c++) {
            for (int i = 0; i < word.length(); i++) {
                if (c == word.charAt(i)) {
                    continue;
                }
                String nextWord = replace(word, i, c);
                if (dict.contains(nextWord)) {
                    nextWords.add(nextWord);
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
