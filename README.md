# leetCode-java
LeetCode coding notes

## [Binary_Search]()

### [二分搜索模板]<br>
- [0704.Binary Search]   (!!!E) <br>
九章模板：1.start + 1 < end; 2.start + (end - start) / 2; 3.A[mid] ==, <, >  mid 4.A[start] A[end] ? target
- [0034.Find_First_and_Last_Position_of_Element_in_Sorted_Array](Solutions/0034.Find_First_and_Last_Position_of_Element_in_Sorted_Array.java) (!!M) <br>
用两次二分分别找first pos of target and last pos of target. 想找first position of target，要保证两点：1. while循环里的判断要往左逼，也就是if nums[mid] >= target: end = mid； 2. 就把start放在后面更新，这样如果出现nums[end]和nums[start]都等于target的情况的话，first可以被后面较小的start替换掉，因为start肯定是小于end的。
Follow up: In a sorted array [1,3,4.......], search the elements that are in a certain range eg:[10, 100]. solution: 用两次二分分别找first position of 10 and last position of 100. Then the elements between the two positions should be in range [10, 100]. <br>

### [第一境界：二分位置之ooxx]<br>
- [0278.First Bad Version](Solutions/0278.First_Bad_Version.java) (E) <br>
- [0702.Search in a Sorted Array of Unknown Size](Solutions/0702.Search_in_a_Sorted_Array_of_Unknown_Size.java) (M) <br>

### [第二境界：不能00xx, half-half]<br>
找不到一个严格的分界点是左派还是右派，所以可以考虑是half-half<br>
- [0278.First Bad Version](Solutions/0278.First_Bad_Version.java) (E) <br>
- [0153.Find Minimum in Rotated Sorted Array](Solutions/0153.Find_Minimum_in_Rotated_Sorted_Array.java) (!!M) <br>
与153类似，只是array里可能有duplicates，采用153的解法三，唯一不同的是：nums[mid] == nums[end]: end -= 1, 注意不能drop掉一半，因为eg: nums=[2,2,2,2,2,1,2,2,2,2,2,2........], 由于不知道mid是1前面的2还是1后面的2，所以无法确定是drop前面还是drop后面，只能保险地把end往前挪一位，所以154这题in extreme case, 时间复杂度是O(N). 这题用nums[end]与nums[mid]比较能work的原因是end永远不可能出现在最小值的左边。<br>
- [0033.Search_in_Rotated_Sorted_Array](Solutions/0033.Search_in_Rotated_Sorted_Array.java) (M) <br>
画个图分几个区间讨论就可以了, 分target在左边区间和target在右边区间讨论. <br>

### [第三境界：Binary Search on Result]<br>
往往没有给你一个数组让你二分 而且题目压根看不出来是个二分法可以做的题，同样是找到满足某个条件的最大或者最小值
- [0069.Sqrt(x)](Solutions/0069.Sqrt(x).java)(!!E)<br>
- [0183.wood cut](Solutions/0183.wood_cut.java)(H Lintcode)<br>
minimum/maximum to satisfy some condition 的问题: If we can cut into pieces with lens, then we can also cut into prices with len - 1, So this is a OOOXXX problem, to find the last O.<br>
- [0437.Copy Books](Solutions/0437.Copy_Books.java)(!!M Lintcode) <br>
minimum/maximum to satisfy some condition 的问题: OOOXXX problem, to find the first O. 二分法不难想，难想的是比较mid时的那个helper function, helper function return if k people can finish all the pages in the midTime. Algorithm: greedy. 只有上一个人无法在mid时间内完成的情况下，我们才加一个人进来
- [0875.Koko Eating Bananas](Solutions/0875.Koko_Eating_Bananas.java)(M)<br>
minimum/maximum to satisfy some condition 的问题: If Koko can finish eating all the bananas (within H hours) with an eating speed of K, she can finish with a larger speed too. So it is a OOOXXX problem trying to find the first X. end is set to be max(piles). Every time find if it posible to eat all the bananas with speed mid. if yes, then drop the right part, if no, then drop the left.

回答：this is a good question,二分的问题，永远的解决办法是，某一部分满足条件，某一部分不满足条件，就可以去除不满足条件的部分

## [Binary_Tree & Divide Conquer](/Data-Structure.py) 

classic binary tree & divide conquer
- [0226.Invert Binary Tree](Solutions/0226.Invert_Binary_Tree.java) (E)
- [0100.Same Tree](Solutions/0100.Same_Tree.java) (E)

time complexity training II <br>
O(n)的时间，把n的问题，变成了2个n/2的问题，复杂度是多少？  nlogn:merge sort//quick sort <br>
O(1)的时间，把n的问题，变成了1个n/2的问题，复杂度是多少？  logn <br>
O(1)的时间，把n的问题，变成了2个n/2的问题，复杂度是多少？  n （为什么）<br>

解法：1.Non-Recursion 2.Recursion：Traverse 3.Recursion：Divide & Conquer 4.Recursion：Traverse + Divide & Conquer

区别：全局变量和局部变量 <br>
递归三要素：定义-拆解-结束条件 <br>

非递归的 前序-中序-后序算法要背诵   TODO： <br>

- [0144.Binary Tree Preorder Traversal](Solutions/0144.Binary_Tree_Preorder_Traversal.java) (M) memorize the iterative version using stack<br>
preorder前序遍历: 1.非递归算法 (recommend) 2.递归算法：分治法 3.递归算法：遍历法  TODO :只写了一个方法 <br>
分治法和遍历法的区别，遍历法用了全局变量

- [0094.Binary Tree Inorder Traversal.java](Solutions/0094.Binary_Tree_Inorder_Traversal.java)(M) memorize the iterative version using stack solution 2: in order traversal of BST (iteratively) - O(k+H) where H is height of tree. solution 1: trivial - in order traversal of BST - O(N), O(N).<br>
inorder中序遍历: 1.非递归算法 (recommend) 2.递归算法：分治法 3.递归算法：遍历法   TODO :只写了一个方法 <br>

- [0145.Binary Tree Postorder Traversal](Solutions/0145.Binary_Tree_Postorder_Traversal.java) (M) memorize the iterative version using stack<br>
postorder后序遍历: 1.非递归算法 (recommend) 2.递归算法：分治法 3.递归算法：遍历法 TODO :只写了一个方法 <br>

碰到二叉树的问题，就想想整棵树在该问题上的结果
和左右儿子在该问题上的结果之间的联系是什么

- [0104.Maximum Depth of Binary Tree.java](Solutions/0104.Maximum_Depth_of_Binary_Tree.java)(E) <br>
rootDepth = max(leftDepth, rightDepth) + 1 <br>
- [0480.Binary Tree paths](Solutions/0480.Binary_Tree_paths.java)(LintCode) <br>
- [0596.minimum subtree.java](Solutions/0596.minimum_subtree.java)(LintCode) <br>
Divide and Conquer的方法输出以root为根的subTree的subSum，然后每次与minSum打擂台进行比较，注意python中定义全局变量可以用self.minSum = float("inf"), self.minNode = None，在主函数中定义这两个变量就可以了. 这种题应该是送分题！<br>
- [0110.Balanced Binary Tree.java](Solutions/0110.Balanced_Binary_Tree.java)(E) <br>
helper function return (if the tree is balanced, maxDepth); rootIsBalan = leftIsBalan and rightIsBalan and abs(leftMaxDepth - rightMaxDepth) <= 1
- [1120.Maximum Average Subtree](Solutions/1120.Maximum_Average_Subtree)(E) <br>
总结：二叉树的通用时间复杂度计算公式  =O(二叉树的节点个数N * 每个节点的处理时间)

- [0114.Flatten Binary Tree to Linked List](Solutions/0114.Flatten_Binary_Tree_to_Linked_List.java)<br>

最近公共祖先 Lowest Common Ancestor
situation1: has parent note 
situation2: do not has parent note example:0236
situation3: a,b exist in binary tree?
situation4: binary search tree example:0235
- [0236.Lowest Common Ancestor of a Binary Tree.java](Solutions/0236.Lowest_Common_Ancestor_of_a_Binary_Tree.java)<br>
- [0235.Lowest Common Ancestor of a Binary Search Tree.java](Solutions/0235.Lowest_Common_Ancestor_of_a_Binary_Search_Tree)<br>

最长连续序列 Binary Tree Longest Consecutive Sequence
situation1: 二叉树不可转弯 example:0298
situation2: 可转弯 example:0549
situation3: 多叉树   所有子树最长递增和最长递减
- [0298.Binary Tree Longest Consecutive Sequence](Solutions/0298.Binary_Tree_Longest_Consecutive_Sequence.java)(!!M)<br>
helper function returns (the LCS ended with root, without root)
- [0549.Binary Tree Longest Consecutive Sequence II](Solutions/0549.Binary_Tree_Longest_Consecutive_Sequence_II.java)(!!M)<br>
helper function returns (the LCS ended with root decreasing, increasing, without root, pass root)

TODO：https://leetcode.com/problems/binary-tree-longest-consecutive-sequence-ii/  <br>

路径相关的题目：

二叉树的路径和:Binary Tree Path Sum I && II && III
situation1: include root (a.return boolean  b.return all path and then print) example:0112
situation2: can not include root example:0437 
situation3: any to any can make a turn
- [0112.Path Sum](Solutions/0112.Path_Sum.java)(E)<br>
求path, 第一反应当然是dfs了
- [0113.Path Sum II](Solutions/0113.Path_Sum_II.java)(!!M)<br>    TODO
Solution 1: 碰到打印所有路径的问题，第一反应就是带backtracking the dfs
- [0437.Path Sum III](Solutions/0437.Path_Sum III)(!!M)  TODO<br>
不需要从根节点出发，solution 1: dfs every node in the tree. at each node, do a backtrack to find how many root-to-any_node paths are there. solution 2: dfs + memorization. 用 HashMap 来建立路径之和跟其个数之间的映射，即路径之和为 curSum 的个数为 m[curSum].
TODO:
1.https://leetcode.com/problems/path-sum-iii/ 
2.binary tree maximum path sum  还有一个相关的题  <br>

BST

TODO:思考LCA建立在BST的基础之上

- [0098.Validate Binary Search Tree.java](Solutions/0098.Validate_Binary_Search_Tree.java)(M)<br>
注意判断条件不仅仅是left.val<root.val<right.val而是max of left < root < min of right; helper函数返回以root为根的树(是不是BST，max and min value in the tree); if (isLeftBST and isRightBST and maxLeft < root.val < minRight): return True

TODO:运行失败convert binary search tree to doubly linked list:https://leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/ <br>
 TODO ：Question:全局变量---变量
 

## [Breadth First Search](/Data-Structure.py) 
求最短的路径就可以用BFS

分层遍历三层循环 
1.queue！= null 
2.size = queue.size 当前这一层的每个节点 
3.for循环出当前层的每个节点的下一个单词

非分层遍历二层循环
1.queue！= null 
2.for循环出当前节点的下一个单词

### [a.二叉树上的宽搜 BFS in Binary Tree模板](/Data-Structure.py) 
1.把源节点放入q中
2.while循环：把源节点一个个弹出q，与此同时把刚刚弹出来的节点的邻居（们）加入q
能够用BFS解决的问题，一定不要用DFS去做

 二叉树上的宽度优先搜索 BFS in Binary Tree
- [0449.Serialize and Deserialize BST](Solutions/0449.Serialize_and_Deserialize_BST)<br>
Same as 297. Solution says since BST, the answer could be as compact as possible. Don't know how?
- [0102.Binary Tree Level Order Traversal](Solutions/0102.Binary_Tree_Level_Order_Traversal.java)<br>
 
### [b.图上的宽搜 BFS in Graph](/Data-Structure.py) 
判断图是不是树？
1.边树刚好等于n-1，点数和边数差1
2.n-1条边一定要把整个图连起来，判断连通性，就是通过一个点把其他的点都能找到
图上的宽搜 BFS in Graph，和树上有什么区别？图中存在环，存在环意味着，同一个节点可能重复进入队列
- [0261.Graph Valid Tree](Solutions/0261.Graph_Valid_Tree.java) (!!!M) <br>
- [0133.Clone Graph](Solutions/0133.Clone_Graph.java) (!!!M) <br>
- [0618.Search Graph Nodes](Solutions/0618.Search_Graph_Nodes.java) (leetcode)  图的遍历(由点及面) <br>
如何找所有最近的value=target的点? 加上层序遍历

b.1 拓扑排序 Topological Sorting
- [0127.Topological Sorting.java ](Solutions/0127.Topological_Sorting.java) (!!LintCode)  <br>
有向图的问题，可以检测有向图是否有环！必考，其实也非常模板化，一定要记住。Three steps: 1. 从数字关系求出每个节点的inDegrees（就是找节点与相邻节点的依赖关系） (inDegrees = collections.defaultdict(int))，key是node, val是这个node的indegree值; 2. 和每个节点的neighbors （neighbors = collections.defaultdict(list)), key是node, val是装有这个node的neighbor的list; 3. 然后 BFS，背诵模板就可以了。
相关题目一定要做 TODO

### [c.矩阵中的宽度优先搜索BFS in Matrix](/Data-Structure.py) 
图的遍历(由点及面) Number of Islands 经典矩阵宽度优先搜索 
- [0200.Number_of_Islands.java](Solutions/0200.Number_of_Islands.java) (!!LintCode) <br>
图的遍历(层级遍历)  同：https://leetcode.com/problems/rotting-oranges/ 复习时可做
- [0598.Zombie in Matrix](Solutions/0598.Zombie_in_Matrix.java) (!!LintCode) <br>
简单图最短路径 
- [0611.Knight Shortest Path](Solutions/0611.Knight_Shortest_Path.java) (!!LintCode) <br>
- [0573.Build Post Office II](Solutions/0573.Build_Post_Office_II.java) (!!LintCode) <br>

## [Depth_First_Search](/Data-Structure.py) 
碰到让你找所有方案的题，一定是DFS  
90%DFS的题，要么是排列，要么是组合
DFS更节约空间 
DFS算法有时候=回溯算法

递归三要素：• 递归的定义 • 递归的拆解 • 递归的出口
一般来说，如果面试官不特别要求的话，DFS都可以使用递归(Recursion)的方式来实现。 递归三要素是实现递归的重要步骤:

### [组合搜索问题 Combination](/Data-Structure.py) 
n个元素的数组，组合个数为2^n次方

 问题模型:求出所有满足条件的“组合”。 <br>
 判断条件:组合中的元素是顺序无关的。 <br>
 时间复杂度:与 2^n 相关。<br>

subset问题
- [0078.Subsets](Solutions/0078.Subsets.java) (M) <br>
- [0090.Subsets_II](Solutions/0090.Subsets_II) (M) <br>

combination sum
- [0039.Combination Sum](Solutions/0039.Combination_Sum.java) (M) <br>
- [0040.Combination_Sum_II](Solutions/0040.Combination_Sum_II.java) (M) <br>
 
Palindrome Partitioning 解题思路：字母和字母之间的位置当成切和不切，从s的startIndex进行切分
- [0131.Palindrome Partitioning](Solutions/0131.Palindrome_Partitioning.java) <br>

时间复杂度通用公式：
搜索的时间复杂度：O(答案总数 * 构造每个答案的时间)   不能明显知道答案个数，就用s，所以为s*n      通用的DFS时间复杂度计算公式 O(答案个数 * 构造每个答案的时间)
举例Subsets问题，求所有的子集，子集个数一共2^n，每个集合的平均长度是O(n)的，所以时间复杂度为O(n*2^n),同理Permutations问题的时间度咋读为O（n*n!）

### [排列搜索问题 Permutation](/Data-Structure.py) 
全排列=n！
问题模型:求出所有满足条件的“排列”。 
判断条件:组合中的元素是顺序“相关”的。 
时间复杂度:与 n! 相关。
- [0046.Permutations.java](Solutions/0046.Permutations.java) (M) <br>
- [0047.Permutations_II](Solutions/0047.Permutations_II.java) (M) <br>


### [图中的搜索 Search in a Graph](/Data-Structure.py)  

N皇后问题（一）·N-Queens  TODO
N皇后问题（二）·N-Queens  TODO


- [0127.Word Ladder](Solutions/0127.Word_Ladder.java) (M) <br>
Word Ladder II：TODO 太难了
求出所有的最短路径，碰到让你找所有方案的题，一定是DFS，所以一定用到了DFS；如果单纯用DFS，相当于要求出所有的路径，然后比较最短的路径，时间复杂度高。
所以要用BFS+DFS，用BFS每次获取距离终点最近的点，怎么得到每个点到终点的距离？从终点开始做DFS

求一个值在不在hash表中的算法复杂度？O(1)? 更准确的说法O(L)  L为这个值的长度

### [必背程序]()
Tree Traversal(二叉树) 用到栈 <br>
http://www.jiuzhang.com/solutions/binary-tree-preorder-traversal/ <br>
http://www.jiuzhang.com/solutions/binary-tree-inorder-traversal/ <br>
http://www.jiuzhang.com/solutions/binary-tree-postorder-traversal/ <br>
http://www.jiuzhang.com/solutions/binary-search-tree-iterator/ <br>
Combination <br>
http://www.jiuzhang.com/solutions/subsets/ <br>
Permutation（没懂）<br>
http://www.jiuzhang.com/solutions/permutations/ <br>

### [Stack-Non Recursion]()


总结：BFS和DFS区别，BFS擅长求点，DFS擅长求路径

DFS不回溯的题目：Number of Islands，因为就是要找点，不是要找路径


## [链表与数组 Linked List & Array](/Data-Structure.py) 

### [Linked List]()
a.Dummy Node <br>
如何使用 Dummy Node
head = dummy 这句话总是需要么? 
什么时候使用 Dummy Node? 结构变化，会导致头部变化，就可以用Dummy Node
Dummy Node 是否需要删除? 不用，Java会自动删除
使用 Dummy Node 算面试官会说我耗费了额外空间么? 
Dummy Node 非用不可么? 不是，写起来可能很麻烦
Dummy Node 初始化的值重要么?  不重要
链表的问题都需要用到 Dummy Node 么?  90%都可以用到
总结：链表的题一般就使用dummy node

- [0206.Reverse Linked List.java](Solutions/0206.Reverse_Linked_List.java)<br>
- [0025.Reverse Nodes in k-Group](Solutions/0025.Reverse_Nodes_in_k-Group.java)<br>
- [0138.Copy List with Random Pointer](Solutions/0138.Copy_List_with_Random_Pointer.java)<br>
 方法1：先复制点，再复制边，记录下来新老节点的映射关系，用hashMap存储。  缺点：用了额外的存储空间  （nextTime可以用下这个方法）<br>  
 方法2：记住，讨巧的方式，改变链表结构变成1-1’-2-2‘-3-3’ 再分离，不用额外的空间 <br>
 解题时：复杂问题先分成几个小问题，定好小问题的输入和输出，再写小问题 <br>

 Linked List Cycle  
 常规解法1：extra空间 用hashSet
 非常规解法2：快慢指针
- [0141.Linked List Cycle](Solutions/0141.Linked_List_Cycle.java)<br>
- [0160.Intersection of Two Linked Lists](Solutions/0160.Intersection_of_Two_Linked_Lists.java)<br>
 follow up:判断两个链表是不是有交集，并且求出相交点；
 解法：两个链表连起来看有没有环，将一个链表的头尾相连，判断有没有环，有环说明是相交的，然后求出相交点。

 Sort List 必须会这两个算法（） 2个小视频 merge sort / quick sort  heap也看小视频  （TODO）
 问:哪些排序算法时间复杂度是 O(nlogn) 的? merge sort / quick sort / heap sort
 
### [Array]()
子数组Subarray:令PrefixSum[i] = A[0] + A[1] + ... A[i - 1], PrefixSum[0] = 0。易知构造PrefixSum耗费O(n)时间和O(n)空间，如需计算子数组从下标i到下标j之间的所有数之和，则有 Sum(i~j) = PrefixSum[j + 1] - PrefixSum[i]
- [0053.Maximum Subarray](Solutions/0053.Maximum_Subarray.java)<br>
- [0604.Window Sum.java](Solutions/0604.Window_Sum.java)<br>
- [0138.Subarray Sum](Solutions/0138.Subarray_Sum.java) （lintcode）<br>
Subarray Sum Closest 求出来后排个序 （lintcode） TODO

Sorted Array 
1.Merge Two Sorted Arrays（lintcode）TODO
2.将小数组归并到大数组里，从后往前merge  - [0088.Merge Sorted Array](Solutions/0088.Merge_Sorted_Array.java)<br> 
3.两个数组的交 简单题应该会很多种方法  相关问题TODO
 hash  time O(n+m)  space O(min(n,m))  一个数组放进去，另一个数组进行遍历在不在hash中
 merge two sorted arrays  time O(nlogn + mlogm)  space O(1)  先把两个数组排序，再用两个指针遍历merge
 Binary Search(n << m)  time O(nlogn + mlogn)  space O(1) 一个数组先排序，遍历另一个数组，查找在不在已经排好序的数组中，把小的数组排序，然后for循环大的数组
4.数组内积（点乘）  设计：数组index和value的形式，index相同的才乘起来。
 
 - [0004.Median_of_Two_Sorted_Arrays](Solutions/0004.Median_of_Two_Sorted_Arrays.java)<br>
 
 相关问题：TODO
 小视频:Quick select 算法
 kth largest element 从大到小第K个数 
 median:掌握quick select 做法 logn ，等于kth largest element 
 2个数组的中位数，就是合并后从小到大第k个数  
 时间复杂度倒推算法 logk
 
java知识点： 
一个node.next==null
node.next占个字节
说明node占8个字节
null在编译后值为0，所以还是占4个字节
 
## [两根指针 Two Pointes]()
同向双指针  相向双指针
一般适合时间复杂度要求是O（n）的

### [partition]()
快排 quick sort：<br>
1.Partition Array （lintcode） 注意：4个地方的判断语序写成一样的 - [0031.Partition Array](Solutions/0031.Partition_Array.java) <br>
2.（小视频TODO） Quick Select// Kth-largest-element   <br>
3.Related Questions（related questions）  <br>
4.Sort Colors 三分的问题  - [0075.Sort Colors](Solutions/0075.Sort_Colors.java) <br>   
解法：分成两个部分 vs 分成三个部分 1)2次partition，先分0和1-2，再分1-2  2)只能1次循环    下次尝试1这个方法   <br>
 
排序 Rainbow sort    待写，低频下次再写 
烙饼排序 先解决最下面的变成最大  
睡眠排序  （不考）
面条排序  （不考）
猴子排序：洗牌算法  （不考）
 
### [Two Sum]()
模板必记：可以循环其中一个变量，然后研究另外一个变量如何变化
1.two sum 
方法：1.hashmap 2.先排序 低空间复杂度 two pointers  
2.two-sum-data-structure-design 只能使用HashMap  
3.two-sum-input-array-is-sorted 使用Two Pointers会更快
4.Two Sum - Unique pairs   是否可以先去重？不能
5.3Sum  统计所有的和为0的三元组（Triples）
6.two sum计数问题 统计所有和 <= target 的配对数
7.two sum计数问题 统计所有和 >= target 的配对数
8.Two Sum Closest 
9.Follow Up: 3Sum Closest
 
related questions (下次写)
4Sum
Two Sum - difference equals to target (同向双指针)


 
 



 
 
 












