//Solution 1: Brute Force
class Solution {
    public int leastInterval(char[] tasks, int n) {
        int[] count = new int[26];
        int max = 0;
        int maxCount = 0;
        
        for (char c: tasks){
            count[c-'A']++;
            max = Math.max(count[c-'A'], max);
        }
        
        for (int i: count){
            if (i == max)
                maxCount++;
        }
        
        return Math.max(tasks.length, (max-1) * (n+1) + maxCount);
    }
}

//Solution 2: PriorityQueue
class Solution {
    public int leastInterval(char[] tasks, int n) {
        Map<Character, Integer> task_counter = new HashMap<>();
        for(Character task: tasks) {
            task_counter.put(task, task_counter.getOrDefault(task,0) + 1);    
        }
        PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());
        pq.addAll(task_counter.values());
        
        int time = 0;
        while(pq.size() > 0) {
            List<Integer> add_back = new ArrayList<>();
            
            for(int i= 0; i <= n; i++) {
                if(pq.size() > 0) {
                    int count = pq.poll(); 
                    count--;
                    if(count > 0) { 
                        add_back.add(count);
                    }  
                }
                
                time += 1; 
                if(pq.size() == 0 && add_back.size() == 0) { 
                    break;
                }  
            }   
            pq.addAll(add_back);  
        }
        return time;
    }
}
