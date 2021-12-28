# leetCode-java
LeetCode coding notes

## [Binary_Search](/Data-Structure.py) 

二分搜索模板<br>
- [0704.Binary Search]   (!!!E) <br>
九章模板：1.start + 1 < end; 2.start + (end - start) / 2; 3.A[mid] ==, <, >  mid 4.A[start] A[end] ? target
- [0034.Find_First_and_Last_Position_of_Element_in_Sorted_Array](Solutions/0034.Find_First_and_Last_Position_of_Element_in_Sorted_Array.java) (!!M) <br>
用两次二分分别找first pos of target and last pos of target. 想找first position of target，要保证两点：1. while循环里的判断要往左逼，也就是if nums[mid] >= target: end = mid； 2. 就把start放在后面更新，这样如果出现nums[end]和nums[start]都等于target的情况的话，first可以被后面较小的start替换掉，因为start肯定是小于end的。
Follow up: In a sorted array [1,3,4.......], search the elements that are in a certain range eg:[10, 100]. solution: 用两次二分分别找first position of 10 and last position of 100. Then the elements between the two positions should be in range [10, 100]. <br>

第一境界：二分位置之ooxx<br>
- [0278.First Bad Version](Solutions/0278.First_Bad_Version.java) (E) <br>
- [0702.Search in a Sorted Array of Unknown Size](Solutions/0702.Search_in_a_Sorted_Array_of_Unknown_Size.java) (M) <br>

第二境界：不能00xx, half-half,找不到一个严格的分界点是左派还是右派，所以可以考虑是half-half<br>
- [0278.First Bad Version](Solutions/0278.First_Bad_Version.java) (E) <br>
- [0153.Find Minimum in Rotated Sorted Array](Solutions/0153.Find_Minimum_in_Rotated_Sorted_Array.java) (!!M) <br>
与153类似，只是array里可能有duplicates，采用153的解法三，唯一不同的是：nums[mid] == nums[end]: end -= 1, 注意不能drop掉一半，因为eg: nums=[2,2,2,2,2,1,2,2,2,2,2,2........], 由于不知道mid是1前面的2还是1后面的2，所以无法确定是drop前面还是drop后面，只能保险地把end往前挪一位，所以154这题in extreme case, 时间复杂度是O(N). 这题用nums[end]与nums[mid]比较能work的原因是end永远不可能出现在最小值的左边。<br>
- [0033.Search_in_Rotated_Sorted_Array](Solutions/0033.Search_in_Rotated_Sorted_Array.java) (M) <br>
画个图分几个区间讨论就可以了, 分target在左边区间和target在右边区间讨论. <br>

第三境界：Binary Search on Result，往往没有给你一个数组让你二分 而且题目压根看不出来是个二分法可以做的题，同样是找到满足某个条件的最大或者最小值
 
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

模板
1.把源节点放入q中
2.while循环：把源节点一个个弹出q，与此同时把刚刚弹出来的节点的邻居（们）加入q

 二叉树上的宽度优先搜索 BFS in Binary Tree
0449.Serialize_and_Deserialize_BST.java
0102.Binary_Tree_Level_Order_Traversal.java
 
图上的宽搜 BFS in Graph，和树上有什么区别？图中存在环，存在环意味着，同一个节点可能重复进入队列













