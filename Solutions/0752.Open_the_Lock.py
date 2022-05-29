/*
You have a lock in front of you with 4 circular wheels. Each wheel has 10 slots: '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'. The wheels can rotate freely and wrap around: for example we can turn '9' to be '0', or '0' to be '9'. Each move consists of turning one wheel one slot.

The lock initially starts at '0000', a string representing the state of the 4 wheels.

You are given a list of deadends dead ends, meaning if the lock displays any of these codes, the wheels of the lock will stop turning and you will be unable to open it.

Given a target representing the value of the wheels that will unlock the lock, return the minimum total number of turns required to open the lock, or -1 if it is impossible.

 

Example 1:

Input: deadends = ["0201","0101","0102","1212","2002"], target = "0202"
Output: 6
Explanation: 
A sequence of valid moves would be "0000" -> "1000" -> "1100" -> "1200" -> "1201" -> "1202" -> "0202".
Note that a sequence like "0000" -> "0001" -> "0002" -> "0102" -> "0202" would be invalid,
because the wheels of the lock become stuck after the display becomes the dead end "0102".
Example 2:

Input: deadends = ["8888"], target = "0009"
Output: 1
Explanation: We can turn the last wheel in reverse to move from "0000" -> "0009".
Example 3:

Input: deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"], target = "8888"
Output: -1
Explanation: We cannot reach the target without getting stuck.
 

Constraints:

1 <= deadends.length <= 500
deadends[i].length == 4
target.length == 4
target will not be in the list deadends.
target and deadends[i] consist of digits only.
*/

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if target in deadends:
            return -1
        
        q = collections.deque()
        visited = set()
        q.append("0000")
        visited.add("0000")
        
        layer = -1
        while len(q) > 0:
            size = len(q)
            layer += 1
            for _ in range(size):
                curr = q.popleft()
                if curr == target:
                    return layer
                if curr in deadends:
                    continue
                for next_str in self.getNext(curr):
                    if next_str not in visited:
                        q.append(next_str)
                        visited.add(next_str)
        return -1
    
    def getNext(self, curr):
        res = []
        for i in range(len(curr)):
            curr_num = int(curr[i])
            for delta in [-1, 1]:
                next_num = (curr_num + delta) % 10
                next_node = curr[:i] + str(next_num) + curr[i+1:]
                res.append(next_node)
        return res
                
            
            

class Solution {
    public int openLock(String[] deadends, String target) {
        
        Set<String> deadSet = new HashSet<>();
        for (String str : deadends) {
            if (str.equals("0000") || str.equals(target)) {    // 注意判断
                return -1;
            }
            deadSet.add(str);
        }
        
        Queue<String> queue = new LinkedList<String>();
        Set<String> hash = new HashSet<>();
        
        queue.offer("0000");
        hash.add("0000");
        
        int depth = -1;
        while (!queue.isEmpty()) {
            depth++;
            int size = queue.size();
            for (int i = 0; i < size; i++) {
                String head = queue.poll();
                if (head.equals(target)) {
                    return depth;
                }
                ArrayList<String> next = getNext(head, deadSet);
                for (String str : next) {
                    if (hash.contains(str)) {
                        continue;
                    }
                    queue.offer(str);
                    hash.add(str);
                }
            }
        }
        return -1;   
    }
    
    private ArrayList<String> getNext(String target, Set<String> dic) {
        ArrayList<String> nextWords = new ArrayList<>();
        for (int i = 0; i < target.length(); i++) {
            char c = target.charAt(i);
            char before = 0;
            char after = 0;

            if (c == '9') {
                after = '0';
                before = '8'; 
            } else if (c == '0'){
                after = '1';
                before = '9'; 
            }else {
                int af = c + 1;
                int bf = c - 1;
                after = (char)af;
                before = (char)bf;
            }
            
            String bfWord = replace(target, i, before);
            String afWord = replace(target, i, after);
            
            if (!dic.contains(bfWord)) {
                nextWords.add(bfWord);
            }
            if (!dic.contains(afWord)) {
                nextWords.add(afWord);
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
