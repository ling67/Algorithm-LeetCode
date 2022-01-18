# leetCode-java

### 01/15 - 完成7题
101, pre-order traversal, in-order traversal, post-order traversal
104, 226, 617, 596 (Lintcode),597 (Lintcode)112, 257, 

655, 298, 549(放弃), 687, 
110, 543, 236, 235, 250, , 1026

第一课：二分搜索 Binary_Search <br>
第二课：二叉树和分治法 Binary_Tree & Divide Conquer <br>
第三课：宽度优先搜索 Breadth First Search <br>
第四课：深度优先搜索 Depth_First_Search  <br>
第五课：链表与数组 Linked List & Array <br>
第六课：两根指针 Two Pointes <br>
第七课：数据结构 Data Structure  <br>
第八课：动态规划 Dynamic Programming <br>
小视频知识点<br>

## [第一课：Binary_Search 二分搜索]()

思想：Binary_Search is a search algorithm that finds the position of a target value within a sorted array. 
Binary search compares the target value to the middle element of the array. 
If they are not equal, we can eliminate the half in which the target cannot lie, and the search continues on the remaining half.
Again taking the middle element to compare to the target value, and repeating this until the target value is found. 
If the search ends with the remaining half being empty, the target is not in the array.

模板(背诵)：<br>
1.start + 1 < end; <br>
2.start + (end - start) / 2; <br>
3.A[mid] ==, <, >  mid <br>
4.A[start] A[end] ? target <br>

回答：this is a good question,二分的问题，永远的解决办法是，某一部分满足条件，某一部分不满足条件，就可以去除不满足条件的部分

### [二分搜索模板]<br>
思想：在排序数组中找值

- [0704.Binary Search](Solutions/0704.Binary_Search.java)   (!!!E) <br> 
- [0034.Find_First_and_Last_Position_of_Element_in_Sorted_Array](Solutions/0034.Find_First_and_Last_Position_of_Element_in_Sorted_Array.java) (!!M) <br>
用两次二分分别找first pos of target and last pos of target. 想找first position of target，要保证两点：1. while循环里的判断要往左逼，也就是if nums[mid] >= target: end = mid； 2. 就把start放在后面更新，这样如果出现nums[end]和nums[start]都等于target的情况的话，first可以被后面较小的start替换掉，因为start肯定是小于end的。
Follow up: In a sorted array [1,3,4.......], search the elements that are in a certain range eg:[10, 100]. 
solution: 用两次二分分别找first position of 10 and last position of 100. Then the elements between the two positions should be in range [10, 100]. <br>
- [0035.Search Insert Position](0035.Search_Insert_Position.java) (E) <br> 
- [1287.Element Appearing More Than 25% In Sorted Array](Solutions/1287.Element_Appearing_More_Than_25%_In_Sorted_Array.java)   (!!E) <br> 
想想如果我们需要求sorted arr 里 more than n//2 times的num, 只需要直接return arr[n//2]就可以了 同理我们可以求more than 25%的num. step 1: 找出 n//4, 2n//4, 3n//4 位置处的num, 因为答案只可能存在于这三个位置上 step 2: 对这三个num分别做binary search求出first_pos and last_pos, 如果last_pos - first_pos >= n//4 就找到了

### [第一境界：二分位置之ooxx]<br>
思想：严格找到左边都满足一个条件，右边不满足条件，或者倒过来！！！！

- [0278.First Bad Version](Solutions/0278.First_Bad_Version.java) (E) <br>
- [0702.Search in a Sorted Array of Unknown Size](Solutions/0702.Search_in_a_Sorted_Array_of_Unknown_Size.java) (M) <br>
  key point : Find end point using "double method" <br>
- [0074.Search a 2D_Matrix](Solutions/0074.Search_a_2D_Matrix.java) (M) <br>
- [0240.Search a 2D Matrix II](Solutions/0240.Search_a_2D_Matrix_II.java) (M) <br>
从左下角出发往右上角搜索, each comparism rule out a row (i-1=1) or rule out a col (j+=1). O(M+N). Comparing with 0074题目, we can see that in 74, the 2D matrix is strongly sorted, so the time is logM + logN
in 240, the 2D matrix is less strongly sorted, so the time is M + N
If the 2D matrix is not sorted at all, then the time is MN.
- [0852.Peak Index in a Mountain Array](Solutions/0852.Peak_Index_in_a_Mountain_Array.java) (E) <br>

### [第二境界：不能00xx, half-half]<br>
思想：找不到一个严格的分界点是左派还是右派，所以可以考虑是half-half<br>

- [0162.Find Peak Element](Solutions/0162.Find_Peak_Element.java) (M) <br>
  follow up: Find Peak Element II (by 算法强化班)   (TODO!!! hard)
- [0153.Find Minimum in Rotated Sorted Array](Solutions/0153.Find_Minimum_in_Rotated_Sorted_Array.java) (!!M)  <br>
  pay attention, compare with nums[n-1],not nums[0], 跟nums[0]比较，有可能全部递增的情况，会有问题
- [0154.Find Minimum in Rotated Sorted Array II](Solutions/0154.Find_Minimum_in_Rotated_Sorted_Array_II.java)  (!!H)   <br>
  与153类似，只是array里可能有duplicates，mid小于或者大于都不会影响程序，只有mid=right的情况不知道判断是向左走还是向右走？
  没法判断mid在左区间还是右区间，有个技巧是right - 1，丢掉right，因为right和mid相等，也不会影响最终答案，右区间一直压缩，直到mid和right不相等。
  采用153的解法三，唯一不同的是：nums[mid] == nums[end]: end -= 1, 注意不能drop掉一半，因为eg: nums= [2,2,2,2,2,1,2,2,2,2,2,2........], 由于不知道mid是1   前面的2还是1后面的2，所以无法确定是drop前面还是drop后面，只能保险地把end往前挪一位，所以154这题in extreme case, 时间复杂度是O(N). 这题用nums[end]与nums[mid]   比较能work的原因是end永远不可能出现在最小值的左边。<br>
- [0033.Search_in_Rotated_Sorted_Array](Solutions/0033.Search_in_Rotated_Sorted_Array.java) (M) <br>
  画个图分几个区间讨论就可以了, 分target在左边区间和target在右边区间讨论. <br>
- [0081.Search in Rotated Sorted Array II](Solutions/0081.Search_in_Rotated_Sorted_Array_II.java) (M) <br> 
  33题的follow up, 解法应该与154相似，传统二分不适合的情况，头等于尾巴，1，1，2，3，0，1，1，不知道向左走还是向右走？所以简单的方法就是去掉尾部和头部相同的元素.
  
### [第三境界：Binary Search on Result 二分答案]<br>
思想：往往没有给你一个数组让你二分 而且题目压根看不出来是个二分法可以做的题，同样是找到满足某个条件的最大或者最小值

- [0069.Sqrt(x)](Solutions/0069.Sqrt(x).java)(!!E)<br>
- [0367.Valid_Perfect_Square](Solutions/0367.Valid_Perfect_Square)(!!E)  注意越界问题<br>
- [0183.wood cut](Solutions/0183.wood_cut.java)(H Lintcode)<br>
  minimum/maximum to satisfy some condition 的问题: If we can cut into pieces with lens, then we can also cut into prices with len - 1, So this   is a OOOXXX problem, to find the last O.<br>
- [0437.Copy Books](Solutions/0437.Copy_Books.java)(!!M Lintcode) <br>
  minimum/maximum to satisfy some condition 的问题: OOOXXX problem, to find the first O. 二分法不难想，难想的是比较mid时的那个helper function, helper   function return if k people can finish all the pages in the midTime. Algorithm: greedy. 只有上一个人无法在mid时间内完成的情况下，我们才加一个人进来
- [0875.Koko Eating Bananas](Solutions/0875.Koko_Eating_Bananas.java)(M)<br>
  minimum/maximum to satisfy some condition 的问题: If Koko can finish eating all the bananas (within H hours) with an eating speed of K, she     can finish with a larger speed too. So it is a OOOXXX problem trying to find the first X. end is set to be max(piles). Every time find if it   posible to eat all the bananas with speed mid. if yes, then drop the right part, if no, then drop the left.

### [Related Questions]<br>
• Binary Search:
- [0248.Count of Smaller Number](Solutions/0248.Count_of_Smaller_Number.java)(M Lintcode) <br>
• Rotate Array 小视频， remember it.
- [0039.Recover Rotated Sorted Array](Solutions/0039.Recover_Rotated_Sorted_Array.java)(E Lintcode) <br>
- [0008.Rotate String](Solutions/0008.Rotate_String.java)(E Lintcode) <br>
三步翻转法: [4,5,1,2,3] → [5,4,1,2,3] → [5,4,3,2,1] → [1,2,3,4,5]

## [第二课：Binary_Tree & Divide Conquer 二叉树和分治法](/Data-Structure.py) 
思想：A divide-and-conquer algorithm works by recursively breaking down a problem into two or more sub-problems of the same or related type, until these become simple enough to be solved directly. 
The solutions to the sub-problems are then combined to give a solution to the original problem.

解法：<br>
1.Non-Recursion 
2.Recursion：Traverse 
3.Recursion：Divide & Conquer 
4.Recursion：Traverse + Divide & Conquer  <br>

写代码牢记：<br>
递归三要素：定义-拆解-结束条件 
1.definition: return revert binary tree
2.divide && conquer
3.exit

### [classic binary tree & divide conquer]() 
- [0226.Invert Binary Tree](Solutions/0226.Invert_Binary_Tree.java) (E)
- [0100.Same Tree](Solutions/0100.Same_Tree.java) (E)
- [0101.Symmetric_Tree](Solutions/0101.Symmetric_Tree.java) (E)
- [0617.Merge Two Binary Trees](Solutions/0617.Merge_Two_Binary_Trees.java) (E)
- [0597.Subtree with Maximum Average](Solutions/0597.Subtree_with_Maximum_Average.java) (E)
- [0655.Print Binary Tree](Solutions/0655.Print_Binary_Tree.java) (E)

time complexity training II <br>
O(n)的时间，把n的问题，变成了2个n/2的问题，复杂度是多少？  nlogn: merge sort//quick sort <br>
O(1)的时间，把n的问题，变成了1个n/2的问题，复杂度是多少？  logn <br>
O(1)的时间，把n的问题，变成了2个n/2的问题，复杂度是多少？  n （为什么）<br>

区别：全局变量和局部变量 <br>

### [二叉树前序-中序-后序算法]() 
前序-中序-后序算法要背诵 
解法：1.非递归算法 (recommend) 2.递归算法：分治法 3.递归算法：遍历法**  TODO:遍历法 <br>
- [0144.Binary Tree Preorder Traversal](Solutions/0144.Binary_Tree_Preorder_Traversal.java) (M) memorize the iterative version using stack<br>
分治法和遍历法的区别，遍历法用了全局变量 <br>
- [0094.Binary Tree Inorder Traversal.java](Solutions/0094.Binary_Tree_Inorder_Traversal.java)(M) memorize the iterative version using stack solution 2: in order traversal of BST (iteratively) - O(k+H) where H is height of tree. solution 1: trivial - in order traversal of BST - O(N), O(N). <br>
- [0145.Binary Tree Postorder Traversal](Solutions/0145.Binary_Tree_Postorder_Traversal.java) (M) memorize the iterative version using stack <br>
碰到二叉树的问题，就想想整棵树在该问题上的结果；和左右儿子在该问题上的结果之间的联系是什么

### [二叉树深度、路径、子树]() 
- [0104.Maximum Depth of Binary Tree.java](Solutions/0104.Maximum_Depth_of_Binary_Tree.java)(E) <br>
rootDepth = max(leftDepth, rightDepth) + 1 <br>
- [0480.Binary Tree paths](Solutions/0480.Binary_Tree_paths.java)(LintCode) <br>
- [0596.minimum subtree.java](Solutions/0596.minimum_subtree.java)(LintCode) <br>
Divide and Conquer的方法输出以root为根的subTree的subSum，然后每次与minSum打擂台进行比较，注意python中定义全局变量可以用self.minSum = float("inf"), self.minNode = None，在主函数中定义这两个变量就可以了. 这种题应该是送分题！<br>
- [0110.Balanced Binary Tree.java](Solutions/0110.Balanced_Binary_Tree.java)(E) <br>
helper function return (if the tree is balanced, maxDepth); rootIsBalan = leftIsBalan and rightIsBalan and abs(leftMaxDepth - rightMaxDepth) <= 1
- [1120.Maximum Average Subtree](Solutions/1120.Maximum_Average_Subtree)(E) <br>
- [0597.Subtree with Maximum Average](Solutions/0597.Subtree_with_Maximum_Average.java)(E) <br>
- [0114.Flatten Binary Tree to Linked List](Solutions/0114.Flatten_Binary_Tree_to_Linked_List.java)<br>

总结：二叉树的通用时间复杂度计算公式  =O(二叉树的节点个数N * 每个节点的处理时间)

### [最近公共祖先 Lowest Common Ancestor]() 
situation1: has parent note 
situation2: do not has parent note example:0236
situation3: a,b exist in binary tree?
situation4: binary search tree example:0235
- [0236.Lowest Common Ancestor of a Binary Tree.java](Solutions/0236.Lowest_Common_Ancestor_of_a_Binary_Tree.java)<br>
- [0235.Lowest Common Ancestor of a Binary Search Tree.java](Solutions/0235.Lowest_Common_Ancestor_of_a_Binary_Search_Tree)<br>
 follow up:LCA II & III
 
### [最长连续序列 Binary Tree Longest Consecutive Sequence]() 
situation1: 二叉树不可转弯 example:0298
situation2: 可转弯 example:0
situation3: 多叉树 所有子树最长递增和最长递减
总结：
在binary tree里求longest path问题，如果任何path都算数的话，那么我们在divide and conquer的时候要分成两种情况讨论：
case 1. path ended with root; 
case 2: path not ended with root
我们往往需要在helper函数中返回end_w和end_wo两种情况的值
有时候也可以将case 2细分为: I. path pass the root, and II. path without the root.

- [0687.Longest Univalue Path](Solutions/0687.Longest_Univalue_Path.java)()<br>
- [0298.Binary Tree Longest Consecutive Sequence](Solutions/0298.Binary_Tree_Longest_Consecutive_Sequence.java)(!!M)<br>
helper function returns (the LCS ended with root, without root)
- [0549.Binary Tree Longest Consecutive Sequence II](Solutions/0549.Binary_Tree_Longest_Consecutive_Sequence_II.java)(!!M)   (TODO) <br>
helper function returns (the LCS ended with root decreasing, increasing, without root, pass root)
follow up: BT LCS II & III
- [0687.Longest Univalue Path](Solutions/0687.Longest_Univalue_Path.java)(!!M)<br> 
- [0543.Diameter of Binary Tree](Solutions/0543.Diameter_of_Binary_Tree.java)(M)<br> 

### [路径相关的题目]() 
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
- [0257.Binary Tree Paths](Solutions/0257.Binary_Tree_Paths.java)(E)<br>
- [0655.Print Binary Tree](Solutions/0655.Print_Binary_Tree.java)(E)<br>

TODO:
1.https://leetcode.com/problems/path-sum-iii/ 
2.binary tree maximum path sum  还有一个相关的题  <br>

### [Balanced BinaryTree 平衡二叉树]() 
- [0110.Balanced_Binary_Tree.java](Solutions/0110.Balanced_Binary_Tree.java)(M)<br>
- [0543.Diameter of Binary Tree](Solutions/0543.Diameter_of_Binary_Tree.java)(M)<br>
- [0235.Lowest Common Ancestor of a Binary Search Tree](Solutions/0235.Lowest_Common_Ancestor_of_a_Binary_Search_Tree.java)(M)<br> 
- [0236.Lowest Common Ancestor of a Binary Search Tree II](Solutions/0236.Lowest_Common_Ancestor_of_a_Binary_Search_Tree_II.java)(M)<br> 
- [0250.Count_Univalue_Subtrees.java](Solution/0250.Count_Univalue_Subtrees.java)<br>
- [0563.Binary Tree Tilt](Solutions/0563.Binary_Tree_Tilt.java)(M)<br> 
- [1026.Maximum Difference Between Node and Ancestor](Solutions/1026.Maximum_Difference_Between_Node_and_Ancestor.java)(M)<br>

### [BST 二叉查找树]()
解决办法：二分查找的思想，递归实现
TODO:思考LCA建立在BST的基础之上
- [0700.Search in a Binary Search Tree](Solutions/0700.Search_in_a_Binary_Search_Tree.java)(E)<br>
- [0669.Trim a_Binary_Search_Tree.java](Solutions/0669.Trim_a_Binary_Search_Tree.java)(E)<br>
- [0938.Range_Sum_of_BST.java](Solutions/0938.Range_Sum_of_BST.java)(E).   解法同0669 <br>
- [270.Closest Binary Search Tree Value](Solutions/270.Closest_Binary_Search_Tree_Value.java)(E)<br>
- [0108.Convert_Sorted_Array_to_Binary_Search_Tree.java](Solutions/0108.Convert_Sorted_Array_to_Binary_Search_Tree.java)(E)<br>
- [0109.Convert_Sorted_List_to_Binary_Search_Tree.java](Solutions/0109.Convert_Sorted_List_to_Binary_Search_Tree.java)(E)<br>
- [0230.Kth_Smallest_Element_in_a_BST.java](Solutions/0230.Kth_Smallest_Element_in_a_BST.java)(E)<br>
- [0098.Validate_Binary_Search_Tree.java](Solutions/0098.Validate_Binary_Search_Tree.java)(E)<br>
- [0897.Increasing_Order_Search_Tree.java](Solutions/0897.Increasing_Order_Search_Tree.java)(E)<br>

注意判断条件不仅仅是left.val<root.val<right.val而是max of left < root < min of right; helper函数返回以root为根的树(是不是BST，max and min value in the tree); if (isLeftBST and isRightBST and maxLeft < root.val < minRight): return True

TODO:运行失败
convert binary search tree to doubly linked list:https://leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/ <br>

### [Related Questions]() 
 Binary Search Tree Iterator
• http://www.lintcode.com/problem/binary-search-tree-iterator
• http://www.jiuzhang.com/solutions/binary-search-tree-iterator

In-order Successor in Binary Search Tree
• http://www.lintcode.com/problem/inorder-successor-in-binary-search-tree/ 
• http://www.jiuzhang.com/solutions/inorder-successor-in-binary-search-tree/ 

Search Range in Binary Search Tree
• http://www.lintcode.com/problem/search-range-in-binary-search-tree/
• 
Insert Node in a Binary Search Tree
• http://www.lintcode.com/problem/insert-node-in-a-binary-search-tree/
• 
Remove Node in a Binary Search Tree
• http://www.lintcode.com/problem/remove-node-in-binary-search-tree/
• http://www.mathcs.emory.edu/~cheung/Courses/171/Syllabus/9-BinTree/BST-delete.html
 






 



  




 
 
 












