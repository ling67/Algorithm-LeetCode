参考资料汇总：<br>
leedcode刷题讲解：https://www.cnblogs.com/grandyang/p/4606334.html  https://grandyang.com/<br>
YouTube算法讲解：https://www.youtube.com/watch?v=1QZDe28peZk&list=PLRdD1c6QbAqJn0606RlOR6T3yUqFWKwmX   <br>
YouTube算法课：https://www.youtube.com/watch?v=1QZDe28peZk&list=PLRdD1c6QbAqJn0606RlOR6T3yUqFWKwmX   <br>
算法讲解（带你刷题）：https://labuladong.github.io/algo/2/19/33/    <br>
leetcode常见考点：https://www.1point3acres.com/bbs/thread-840864-1-1.html
准备：https://www.1point3acres.com/bbs/thread-840857-1-1.html
https://www.cnblogs.com/grandyang/p/4606334.html
https://labuladong.github.io/algo/2/

[规律总结]()

1.移动窗口第一类模板 <br>
优化类型: <br>
  优化思想通过两层for循环而来  <br>
  外层指针依然是依次遍历  <br>
  内层指针证明是否需要回退 <br>
**规律1：见到窗口满足什么条件求最大最小，滑动窗口**

2.堆  <br>
见到集合求Min/max 就用堆  <br>
见到数组先排序  <br>
  **规律1：见到需要维护一个集合的最小值/最大值的时候要想到用堆**   <br>
  **规律2：第k小的元素，Heap用来维护当前候选集合。**  <br>
  **规律3：见到数组要想到先排序**   <br>

3.Union Find 并查集 <br>
并查集：一种用来解决集合查询合并的数据结构 支持O(1)find/O(1)union  <br>
**考点：**   <br>
并查集原生操作:   <br>
  查询两个元素是否在同一个集合内 find 操作   <br>
  合并两个元素所在的集合 union 操作  <br>
并查集的派生操作:   <br>
  查询某个元素所在集合的元素个数   <br>
  查询当前集合的个数   <br>

4.Trie 字典树   <br>
**考点**   <br>
Trie直接实现   <br>
利用Trie树前缀特性解题   <br>
矩阵类字符串一个一个字符深度遍历的问题（DFS + Trie）   <br>
  
5.Heap
求集合的最大值

6.Stack  <br>
支持操作:O(1) Push / O(1) Pop / O(1) Top   <br>
**规律**   <br>
 利用栈暂且保存有效信息   <br>
 翻转栈的运用   <br>
 栈优化dfs，变成非递归   <br>
 单调栈：Monotonous stack 找每个元素左边或者右边 第一个比它自身小/大的元素 用单调栈来维护   <br>
 
7.二分法深入
找满足某个条件最大值/最小值：二分性
二分法——二分答案：Binary Search on Result.往往没有给你一个数组让你二分,同样是找到满足某个条件的最大或者最小值
解题方法：通过猜值判断是否满足题意不对去搜索可能解 1.找到可行解范围 2.猜答案 3.检验条件 4.调整搜索范围
 
8.扫描线  Sweep-Line
扫描问题的思路: 1.事件往往是以区间的形式存在 2.区间两端代表事件的开始和结束 3.需要排序
• 见到区间需要排序就可以考虑扫描线
 
0391.Number_of_Airplanes_in_the_Sky.py
扫描线做法：碰到interval的start，也就是起飞一架飞机，当前天上的飞机数++。碰到interval的end，也就是降落一架飞机，当前天上的飞机数--。 Step 1: 我们分别把所有的start和所有的end放进两个数组，并排序。Step 2: 然后从第一个start开始统计，碰到start较小就加一，碰到end较小就减一。并且同时维护一个最大飞机数的max。

线性数据结构：queue stack deque
O(n) stack(monostack) queue deque

9.双端队列 deque
• 只用掌握sliding windows maximum这一道题目 • 维护一个候选可能的最大值集合
0239.Sliding_Window_Maximum.py
heapq的方法是O(NK); deque O(N): Iterate over the array. At each step: I. Clean the deque: 1. Keep only the indexes of elements from the current sliding window; 2. Remove indexes of all elements smaller than the current one, since they will not be the maximum ones. eg: [1,2,7,3,5,4], k = 3, because of 7, 1 and 2 will never be in res; II. Append the current element to the deque. Append deque[0] to the output.

10.动态规划滚动数组  
滚动数组
 
 
