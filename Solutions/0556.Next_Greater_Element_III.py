"""
Given a positive integer n, find the smallest integer which has exactly the same digits existing in the integer n and is greater in value than n. If no such positive integer exists, return -1.

Note that the returned integer should fit in 32-bit integer, if there is a valid answer but it does not fit in 32-bit integer, return -1.

 

Example 1:

Input: n = 12
Output: 21
Example 2:

Input: n = 21
Output: -1
 

Constraints:

1 <= n <= 231 - 1
"""

"""
2 4 3 2 1
step1:从末尾向前找到第一个升序：2
step2:从后向前找到第一个比它大的数：3
step3:交换2， 3 ： 34221
step4:让后面的4221排序形成1224
"""

class Solution:
    def nextGreaterElement(self, n: int) -> int:
        s = list(str(n))
        l = len(s)
        i = l - 2
        
        #step1:
        while i >= 0:
            if s[i] < s[i + 1]:
                break
            i -= 1
        if i < 0:   #means all number decrease
            return -1 
    
        #step2:
        for j in range(l - 1, i, -1):
            if s[j] > s[i]:
                s[i], s[j] = s[j], s[i]   #step 3
                break
        
        #step3: 倒序
        s[i + 1:] = s[i + 1:][::-1]
        res = ''.join(s)
        return res if int(res) <= 2 ** 31 - 1 else -1

class Solution:
    def nextGreaterElement(self, n: int) -> int:
        BOUND =  2147483647
        arr = []
        
        #将整数转成数组
        while n // 10 != 0:
            arr.append(n % 10)
            n //= 10
        arr.append(n % 10)
        
        i, j = 0, len(arr)-1
        while i < j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
        
        #从右向左转找到第一个递减的点，记录为left_pos
        for i in range(len(arr) - 1, 0, -1):
            if arr[i-1] < arr[i]:
                break

        left_pos = i-1
        
        #从left_pos出发从左向右找到最后一个将将递增的pos
        dis = float('inf')
        right_pos = left_pos
        for j in range(i, len(arr)):
            if arr[j] > arr[left_pos] and arr[j] - arr[left_pos] <= dis:
                right_pos = j
                dis = arr[j] - arr[left_pos]
        
        #交换两个位置
        if right_pos != left_pos:
            arr[left_pos], arr[right_pos] = arr[right_pos], arr[left_pos]
            #交换后要将left_pos右边的数变成单调递增，才能保证是最小的值。交换后是单调递减的，所以交换变成递增的。
            i, j = left_pos + 1, len(arr) - 1
            while i < j:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j -= 1
                
            #
            res = 0
            for num in arr:
                if 10*res + num <= BOUND:
                    res = 10 * res + num
                else:
                    return -1
            return res
        
        else:
            return -1
            
