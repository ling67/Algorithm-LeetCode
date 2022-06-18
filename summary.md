## [LeetCode Patterns](/Data-Structure.py) 

If input array is sorted then    
* Binary search    
* Two pointers     

If asked for all permutations/subsets then  
* Backtracking Algorithm  

If given a tree then  
* DFS  
* BFS  

If given a graph then  
* DFS 
* BFS  

If given a linked list then  
* Two pointers  

If recursion is banned then 
* Stack 

If must solve in-place then 
* Swap corresponding values  
* Store one or more different values in the same pointer  

If asked for maximum/minimum subarray/subset/options then  
* Dynamic programming  

If asked for top/least K items then  
* Heap  

If asked for common strings then  
* Map 
* Trie 

Else 
* Map/Set for O(1) time & O(n) space
* Sort input for O(nlogn) time and O(1) space

## [Data structure](/Data-Structure.py) 

> 不可变数据（3 个）：Number（数字）、String（字符串）、Tuple（元组）；
> 可变数据（3 个）：List（列表）、Dictionary（字典）、Set（集合）。

> data structures and their operations:

* Arrays:
```python
lst.reverse() directly modifies the original list // lst[::-1]: a new copy list. 
list.sort(reverse=True|False, key=myFunc) ascending 不返回任何东西, modifies the order of elements in the list.
self.position.sort(key = lambda x:(x[1], x[0], x[2]))
b = sorted(arr) 排序，但是不改变原有数组
```

* Maps  
 
* Set: 
```python
arr = [111, 222, 333]
arr = set()
arr.add(444)
person.remove(111)
```
 
* Linked Lists 

* Queues:  
```python
collections.deque()  
q.append() 
q.popleft() pop first element 
q.pop() pop last element 
q[0] get first element 
```
 
* Stacks:  
```python
stack = [] 
stack.append()//stack.put() 
stack.pop()栈顶弹出 
stack.peek()//stack[-1] 取栈顶元素
```

* Heaps:   
```python
heapq.heapify(arr)小顶堆  
heapq.heappush(arr, 4)  
heapq.heappop(li)
```

* 
* Trees  <br>
* 
* Graphs  <br>
    
> common algorithms such as: 
* Recursion
* Binary search
* Breadth-first search
* Depth-first search 

## [binary tree 解题思路](/Data-Structure.py) 

遇到tree的题没有想法怎么办   <br>
1.直接分治，看能不能解决问题，可以跟其他的相互转换   <br>
2.helper: 使用辅助函数helper(), 直接返回的结果//self.res(全局变量打擂台)   <br>
3.dfs访问每一个节点，访问的同时处理数据  跟helper差不多     <br>
4.preorder, inorder访问每个节点，访问的同时处理数据（在中序part处理）     <br>

binary search tree: 同样解题思路，要注意怎么运用它的特点      <br>
q: deque(), append(), popleft() 头部元素        <br> 
array.pop(0) first element array.pop() last element      <br>


## [0.小视频]()
1.SubsetII  done
2.字符串查找之Rabin Karp算法

3.Algorithm-search a 2DMatrix II    Done
related search a 2DMatrix (Binary search) 
4.三步翻转法  时间复杂度O(n)是下线    Done
[4 5 1 2 3]
[4,5]翻转[5,4]
[1 2 3]翻转[3 2 1]
最后再翻转一下[1,2,3,4,5]
5.Merge sort   done
6.Quick Sort  done
7.Quick Sort vs Merge sort   done
8.Quick Select   done
9.Heap done  所有父亲节点比儿子节点来得小，儿子节点之间没有关系

参考第8次课程
10.Subarray子数组问题

11.Merge K Sorted Lists   0023 done
解法：
1.堆priorityQueue, 很有可能不让使用priorityQueue   时间复杂度：NlogK
2.暴力法：第一个跟第二个合并，结果在跟第三个合并，直到最后   时间复杂度：NK 
3.分治算法：从上到下 k分为k/2, k/2分为k/4, 时间复杂度：NlogK
4.归并算法：从下到上 第一个跟第二个合并，第三个跟第四个合并，第五个跟第六个合并
