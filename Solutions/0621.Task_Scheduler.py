"""
Given a characters array tasks, representing the tasks a CPU needs to do, where each letter represents a different task. Tasks could be done in any order. Each task is done in one unit of time. For each unit of time, the CPU could complete either one task or just be idle.

However, there is a non-negative integer n that represents the cooldown period between two same tasks (the same letter in the array), that is that there must be at least n units of time between any two same tasks.

Return the least number of units of times that the CPU will take to finish all the given tasks.

 

Example 1:

Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: 
A -> B -> idle -> A -> B -> idle -> A -> B
There is at least 2 units of time between any two same tasks.
Example 2:

Input: tasks = ["A","A","A","B","B","B"], n = 0
Output: 6
Explanation: On this case any permutation of size 6 would work since n = 0.
["A","A","A","B","B","B"]
["A","B","A","B","A","B"]
["B","B","B","A","A","A"]
...
And so on.
Example 3:

Input: tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2
Output: 16
Explanation: 
One possible solution is
A -> B -> C -> A -> D -> E -> A -> F -> G -> A -> idle -> idle -> A -> idle -> idle -> A
 

Constraints:

1 <= task.length <= 104
tasks[i] is upper-case English letter.
The integer n is in the range [0, 100].
"""


"""
间隔k个位置安排座位的问题，都是task schedule的做法！
我们按频率从大到小去坐n个位置，pop出来之后需要将freq-=1然后push回去, pop出来再add back回去的思想很重要！!
"""
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freqs = collections.Counter(tasks)
        hq = []
        for task, freq in freqs.items():
            heappush(hq, (-freq, task))     # 以freq维护一个最大堆
            
        cnt = 0         # record how many seats were taken
        addback = []    # 没执行完的任务需要重新放回hq里面去
        while len(hq) > 0:
            
            # 先预设有n + 1个座位，eg: n = 3， 那就先预设四个座位: _ _ _ _
            # 每进一次循环代表占领一个座位的位置，让高频的去占领那4个座位
            # 同时将高频的那四个的freq分别减1
            for _ in range(n + 1):
                cnt += 1            # update cnt wheather or not(idle) a task is seated
                
                if len(hq) > 0:     # 遍历一遍hq的所有元素，这些元素分别freq分别减1
                    freq, task = heappop(hq)
                    freq = -freq
                    freq -= 1
                    if freq > 0:    # 没执行完的任务需要重新放回hq里面去
                        addback.append((-freq, task))
                        
                if len(hq) == 0 and len(addback) == 0:
                    return cnt      # if all tasks are seated, 就不要再继续cnt+1了，必须在这个for loop里面停止
            
            # 没执行完的任务现在不在hq里面，把他们放到hq里去
            while len(addback) > 0:
                heappush(hq, addback.pop())
        

"""
https://www.youtube.com/watch?v=s8p8ukTyA2I
"""
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        #each task 1 unit time
        #minimize idle time
        
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapify(maxHeap)
        
        time = 0
        q = deque()    # pairs of (-cnt, idleTime)
        while maxHeap or q:
            time += 1
            if maxHeap:
                cnt = 1 + heappop(maxHeap)
                if cnt:
                    q.append([cnt, time + n])
            if q and q[0][1] == time:   #注意这里，后进入Q的值肯定idletime更长，所以取第一个元素就可以
                heappush(maxHeap, q.popleft()[0])
                
        return time
                
