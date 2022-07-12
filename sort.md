## Merge sort vs Quick sort
- [0912.Sort an Array](Solutions/0912.Sort_an_Array.py) （M） <br>
  Solution: bubble sort, quick sort，merge sort.
- [0148.Sort_List](Solutions/0148.Sort_List.py) (!!M)  <br>
  Solution: merge sort算法, 不能用quick sort，因为quick sort交换在list中很麻烦, 注意找中点的时候，slow, fast = head, head.next。如果写成slow, fast = head, head会陷入死循环 
- [0969.Pancake_Sorting.py](Solutions/0969.Pancake_Sorting.py) （M Pramp） <br>
Solution: for i in range(lens-1, -1, -1 ): Find maxIndex -> flip max to top -> flip max to bottom of the whole arr -> repeat
- [0451.Sort_Characters_By_Frequency.py](Solutions/0451.Sort_Characters_By_Frequency.py) （M） <br>
Solution: buckets sort.  
- [0143.Reorder_List](Solutions/0143.Reorder_List.py) （M） <br>
Solution: step 1: cut the list into two halves; step 2: reverse the 2nd half; step 3: connect the 1st and 2nd half
- [0061.Rotate_List.py](Solutions/0061.Rotate_List.py) （M） <br>
Solution:先求出长度，在根据lens - k % lens得到第几个元素是新的head
- [0561.Array_Partition_I.py](Solutions/0561.Array_Partition_I.py) （E） <br>


## Quick select


## partition
