## DFS template

```python
模板1：dfs 可以直接写成内部函数，方便，不用传递太多参数
def dfs(curr):
  visited.add(curr)   （树不用visited, we never visit same node in a tree）
  for next in neighbors(curr):
    if next not in visited:
      dfs(next)
      
解题步骤：
能不能套模板？
需不需要返回参数？
```

## Backtrack template

1. 最本质的法宝是“画图”，千万不能偷懒，拿纸和笔“画图”能帮助我们更好地分析递归结构，这个“递归结构”一般是“树形结构”，而符合题意的解正是在这个“树形结构”上进行一次“深度优先遍历”，这个过程有一个形象的名字，叫“搜索”；我们写代码也几乎是“看图写代码”，所以“画树形图”很重要。
2. 然后使用一个状态变量，一般我习惯命名为 path、pre ，在这个“树形结构”上使用“深度优先遍历”，根据题目需要在适当的时候把符合条件的“状态”的值加入结果集；这个“状态”可能在叶子结点，也可能在中间的结点，也可能是到某一个结点所走过的路径。
3. 在某一个结点有多个路径可以走的时候，使用循环结构。当程序递归到底返回到原来执行的结点时，“状态”以及与“状态”相关的变量需要“重置”成第 1 次走到这个结点的状态，这个操作有个形象的名字，叫“回溯”，“回溯”有“恢复现场”的意思：意即“回到当时的场景，已经走过了一条路，尝试走下一条路”。第 2 点中提到的状态通常是一个列表结构，因为一层一层递归下去，需要在列表的末尾追加，而返回到上一层递归结构，需要“状态重置”，因此要把列表的末尾的元素移除，符合这个性质的列表结构就是“栈”（只在一头操作）。
4. 当我们明确知道一条路走不通的时候，例如通过一些逻辑计算可以推测某一个分支不能搜索到符合题意的结果，可以在循环中 continue 掉，这一步操作叫“剪枝”。“剪枝”的意义在于让程序尽量不要执行到更深的递归结构中，而又不遗漏符合题意的解。因为搜索的时间复杂度很高，“剪枝”操作得好的话，能大大提高程序的执行效率。“剪枝”通常需要对待搜索的对象做一些预处理，例如第 47 题、第 39 题、第 40 题、第 90 题需要对数组排序。“剪枝”操作也是这一类问题很难的地方，有一定技巧性。总结一下：“回溯” = “深度优先遍历” + “状态重置” + “剪枝”，写好“回溯”的前提是“画图”。因此，非要写一个模板，我想它可能长这个样子：

```Python

一般回溯的问题有两种：
1. 打印/输出所有路径的问题一定是回溯。如果要求输出所有最短路径则需要DFS+BFS. 
2. 打印或输出所有组合/排列的问题：combination/permutation （eg: subsets/permutations 问题）

def backtrack(candidate):    # 递归的定义很重要    
   if find_solution(candidate):   
      output(candidate)    # normally a deep copy for list  
      return    
   for next_candidate in list_of_candidates:    # iterate all possible next candidates.  
      if is_not_valid(next_candidate):    # In the above example: “N” != “I”  
       continue  
   place(next_candidate)        # try this partial candidate solution        
   backtrack(next_candidate)    # given the candidate, explore further.      
   remove(next_candidate)       # backtrack      
   
套用模板:  <br>
如果允许一个数取多次：则next candidate从 i 开始.   <br>
如果不允许一个数取多次：则next candidate从 i+1 开始 (subsets).    <br>
如果不允许一个数取多次且输入有重复元素题目要求去重：则分两步，第一步sort, 第二步去重判断，且next candidate从 i+1 开始.  <br>
如果(1, 3)和(3, 1)认为是不同答案(premutation)：则不需要start_idx, for loop每次都从零开始就可以了，但是每个数只能取一次，所以需要一个visited set做标记.  <br>

在写代码之前一定要先写下三点：  <br>
什么是backtrack的结束条件   <br>
next_candidate有哪些constraint    <br>
将什么传入backtrack函数   <br>

```
