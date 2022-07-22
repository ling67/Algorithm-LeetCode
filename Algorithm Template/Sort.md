## quick sort

```python
O(nlogn) O(1)
def partitionArray(self, nums, k):
        # write your code here
        lens = len(nums)
        if lens == 0:
            return 0

        l, r = 0, lens - 1
        while l <= r:                        #易错点1:统一写成l<=r
            while l <= r and nums[l] < k:    #易错点2:统一写成l<=r
                l += 1
            while l <= r and nums[r] >= k:   #易错点3:统一写成l<=r
                r -= 1
            if l <= r:                       #易错点4:统一写成l<=r
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
        
        return l     #l一定是大于r的
```

## quick select

快速选择原理如下，选择第k大的数字：
* 我们在快速选择的时候，也同样用了划分的思想，随机选择一个中轴，双指针i, j，指针i从左往右扫描，指针j从右往左扫描，如果i < j 则进行交换，并且继续循环，直到遇到中轴，这时候我们的i和j均为中轴（理由：因为i，j相等），如果数字在中轴的左边，则向左递归，如果数字在中轴的右边则向右递归。
* 分析复杂度分析，刚开始的一个循环找中轴，用掉了n次，第二次循环只能找左边的中轴或者右边的中轴，用了n/2次，无限循环下去，直到极限，表达式如下:
* 𝑛+𝑛/2+𝑛/4+𝑛/8...令𝑆𝑛=𝑛+𝑛/2+𝑛/4+𝑛/8...则1/2∗𝑆𝑛=𝑛/2+𝑛/4+𝑛/8...上述两式子相减得到1/2∗𝑆𝑛=𝑛,则𝑆𝑛=2𝑛 时间复杂度推导出T(2n)，结果为O(n)的复杂度。

```python
# 求第k大的数：先partition，再比较
    def quickSelect(self, nums, start, end, k):
        if start == end:
            return nums[start]
        
        left, right = start, end
        pivot = nums[(left + right) // 2]
        
        while left <= right:
            while left <= right and nums[left] > pivot:
                left += 1
            while left <= right and nums[right] < pivot:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
                
        if k <= right:
            return self.quickSelect(nums, start, right, k)
        elif left <= k:
            return self.quickSelect(nums, left, end, k);
        else:
            return nums[k];
```

## merge sort

```python
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        index = len(nums1) - 1
        m -= 1
        n -= 1
        
        while m >= 0 and n >= 0:
            if nums1[m] > nums2[n]:
                nums1[index] = nums1[m]
                m -= 1
                index -= 1

            else:
                nums1[index] = nums2[n]
                n -= 1
                index -= 1
        
        while m >= 0:
            nums1[index] = nums1[m]
            m -= 1
            index -= 1
            
        while n >= 0:
            nums1[index] = nums2[n]
            n -= 1
            index -= 1
```

## bucket sort - use freq/dist/num as idx

```python
1.先用hashmap统计 freq/num
2.再将freq作为数组下标，下标相同的放在同一个bucket中
3.根据bucket链上结果
4.以空间换时间
```

## cycle sort

```python
求重复的数，求缺失的数 要求在O(n) time space O(1) memery space 
把数当坐标用
We use the sign of the index as the indicator. If one number never occur, 
we know the number corresponding to the idx will never be negative.
```
