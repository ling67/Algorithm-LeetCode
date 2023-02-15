# [String]()
- [0242.Valid_Anagram.java](0242.Valid_Anagram.java) (E) <br>
Character method or array to record the frequency of each char.
- [0125.Valid_Palindrome.java](0125.Valid_Palindrome.java) (E) <br>
Two Pointer.
- [0409.Longest_Palindrome.java](0409.Longest_Palindrome.java) (E) <br>
Hashmap
- [0005.Longest_Palindromic_Substring.java](0005.Longest_Palindromic_Substring.java) (M) <br>
1.Brute Force. 2.Expand Around Center. 3.Dynamic Programming
- [0003.Longest_Substring_Without_Repeating_Characters.java](0003.Longest_Substring_Without_Repeating_Characters.java) (M) <br>
Sliding Window. We need consider when we need move i.
- [0438.Find_All_Anagrams_in_a_String.java](0438.Find_All_Anagrams_in_a_String.java) (M) <br>
Sliding Window. with a hashmap(fix window) or sliding window with a array
- [0076.Minimum_Window_Substring.java](0076.Minimum_Window_Substring.java) (M) <br>
Sliding Window. 
- [0008.String_to_Integer_(atoi).java](0008.String_to_Integer_(atoi).java) (M) <br>
不会，好难

# [Array]()

```python
模板(背诵)：
```
- [0001.Two_Sum.java](0001.Two_Sum.java) (E) <br>
Brute force, Hashmap, Two Point(can't use)
- [0015.3Sum.java](0015.3Sum.java) (M) <br>
Two Pointer. then use set to remove repeat array. (more easy)
- [0011.Container_With_Most_Water.java](0011.Container_With_Most_Water.java) (M) <br>
Two Pointer
- [0075.Sort_Colors.java](0075.Sort_Colors.java) (M) <br>
Three Pointer.
- [0169.Majority_Element.java](0169.Majority_Element.java) (E) <br>
method 1: sort then return the middle element
method 2: Hashmap record the feq of the element
- [0217.Contains_Duplicate.java](0217.Contains_Duplicate.java) (E) <br>
Hashmap: compare the size of hashmap and length of array
- [0121.Best_Time_to_Buy_and_Sell_Stock.java](0121.Best_Time_to_Buy_and_Sell_Stock.java) (E) <br> 
Traverse the array and record the max profit
- [0057.Insert_Interval.java](0057.Insert_Interval.java) (M) <br>
For loop to traverse the array. There are 3 situation. 1.when I can directly to add interval. 2.when I can directly to add newInterval.3.when I need combin interval and newInterval.
- [0056.Merge_Intervals.java](0056.Merge_Intervals.java) (M) <br>
For loop to traverse the array. The same solution with the 57.
- [0238.Product_of_Array_Except_Self.java](0238.Product_of_Array_Except_Self.java) (M) <br>
Solution 1: brute force  time limit exceeded.
Solution 2: using dividion operation. If there is 0 in the array, you can't use this method.
Solution 3: Finding Prefix Product and Suffix Product, it is hard to make sure the index.
- [0039.Combination_Sum.java](0039.Combination_Sum.java) (M) <br>
Backtrack!

# [Linked List]()
- [0021.Merge_Two_Sorted_Lists.java](0021.Merge_Two_Sorted_Lists.java) (E) <br>
Two Pointer
- [0141.Linked_List_Cycle.java](0141.Linked_List_Cycle.java) (E) <br>
Two Pointer. slow and fast point.
- [0876.Middle_of_the_Linked_List.java](0876.Middle_of_the_Linked_List.java) (E) <br>
Two Pointer. slow and fast point.
- [0206.Reverse_Linked_List.java](0206.Reverse_Linked_List.java) (E) <br>
Recursion.
- [0146.LRU_Cache.java](0146.LRU_Cache.java) (M) <br>
Approach 1: LinkedHashMap. https://www.jianshu.com/p/8f4f58b4b8ab
Approach 2: Hashmap + DoubleLinkedList

# [Stack]()
- [0020.Valid_Parentheses.java](0020.Valid_Parentheses.java) (E) <br>
Stack. 
- [0150.Evaluate_Reverse_Polish_Notation.java](0150.Evaluate_Reverse_Polish_Notation.java) (M) <br>
- [0232.Implement_Queue_using_Stacks.java](0232.Implement_Queue_using_Stacks.java) (E) <br>
Two Stack.
- [0155.Min_Stack.java](0155.Min_Stack.java) (M) <br>
Two Stack.
- [0224.Basic_Calculator.java](0224.Basic_Calculator.java) (H) <br>
Two Stack.太难了
- [0042.Trapping_Rain_Water.java](0042.Trapping_Rain_Water.java) (M) <br>
Two Pointer
TODO[84]太难了
2.栈解法：固定h，向左右扩散，向左边如果高度大于等于当前h，就加入这个面积，如果高度小于当前的高度就不加入，那此时的面积就是h*(j-i).
向左/右寻找第一个比自己小的位置可以用两次单调栈实现，我们可以把向左和向右第一个比自己小的位置存到起来，然后再来计算面积。

# [Heap]()
- [0973.K_Closest_Points_to_Origin.java]( 0973.K_Closest_Points_to_Origin.java) (M) <br>
1.Brute Force. 2.PriorityQueue
- [0621.Task_Scheduler.java](0621.Task_Scheduler.java) (M) <br>
1.Brute Force. 2.PriorityQueue

# [Binary]()
- [0067.Add_Binary.java](0067.Add_Binary.java) (E) <br>
Two Pointer, 以前考过

# [Binary Search]()
- [0704.Binary_Search.java](0704.Binary_Search.java) (E) <br>
- [0278.First_Bad_Version.java](0278.First_Bad_Version.java) (E) <br>
- [0033.Search_in_Rotated_Sorted_Array.java](0033.Search_in_Rotated_Sorted_Array.java) (M) <br>

# [Binary Tree]()
- [0226.Invert_Binary_Tree.java](0226.Invert_Binary_Tree.java) (E) <br>
Recursion three point: end condition, divide, conquer
- [0110.Balanced_Binary_Tree.java](0110.Balanced_Binary_Tree.java) (E) <br>
Recursion three point: end condition, divide, conquer
- [0236.Lowest_Common_Ancestor_of_a_Binary_Tree.java](0236.Lowest_Common_Ancestor_of_a_Binary_Tree.java) (M) <br>
Recursion three point: end condition, divide, conquer
- [0235.Lowest_Common_Ancestor_of_a_Binary_Search_Tree.java](0235.Lowest_Common_Ancestor_of_a_Binary_Search_Tree.java) (E) <br>
Recursion three point: end condition, divide, conquer
- [0104.Maximum_Depth_of_Binary_Tree.java](0104.Maximum_Depth_of_Binary_Tree.java) (E) <br>
Length of Tree
- [0543.Diameter_of_Binary_Tree.java](0543.Diameter_of_Binary_Tree.java) (E) <br>
Length of Tree
- [0102.Binary_Tree_Level_Order_Traversal.java](0102.Binary_Tree_Level_Order_Traversal.java) (M) <br>
BFS，Queue
- [0199.Binary_Tree_Right_Side_View.java](0199.Binary_Tree_Right_Side_View.java) (M) <br>
BFS，Queue
- [0098.Validate_Binary_Search_Tree.java](0098.Validate_Binary_Search_Tree.java) (M) <br>
Binary Search Tree
- [0230.Kth_Smallest_Element_in_a_BST.java](0230.Kth_Smallest_Element_in_a_BST.java) (M) <br>
Binary Search Tree + inorder

# [Graph]()
- [0733.Flood_Fill.java](0733.Flood_Fill.java) (E) <br>
DFS
- [0200.Number_of_Islands.java](0200.Number_of_Islands.java) (M) <br>
DFS
- [0079.Word_Search.java](0079.Word_Search.java) (M) <br>
DFS-Backtrack
- [0542.01_Matrix.java](0542.01_Matrix.java) (M) <br>
BFS-Matrix-with layer
- [0994.Rotting_Oranges.java](0994.Rotting_Oranges.java) (M) <br>
BFS-Matrix-with layer
- [0207.Course_Schedule.java](0207.Course_Schedule.java) (M) <br>
BFS-Topological Sort 

# [Recursion]()
- [0046.Permutations.java](0046.Permutations.java) (M) <br>
DFS-Backtrack
- [0078.Subsets.java](0078.Subsets.java) (M) <br>
DFS-Backtrack
- [0017.Letter_Combinations_of_a_Phone_Number.java](0017.Letter_Combinations_of_a_Phone_Number.java) (M) <br>
DFS-Backtrack
- [0133.Clone_Graph.java](0133.Clone_Graph.java) (M) <br>
DFS-Backtrack

# [Dynamic Programming]()
- [0070.Climbing_Stairs.java](0070.Climbing_Stairs.java) (E) <br>
DP

























