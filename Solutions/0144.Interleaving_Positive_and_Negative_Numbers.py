"""
Description
Given an array with positive and negative integers. Re-range it to interleaving with positive and negative integers.

Wechat reply 【144】 get the latest requent Interview questions . (wechat id : jiuzhang15)

You are not necessary to keep the original order of positive integers or negative integers.

Example
Example 1

Input : [-1, -2, -3, 4, 5, 6]
Outout : [-1, 5, -2, 4, -3, 6]
Explanation :  any other reasonable answer.
Challenge
Do it in-place and without extra memory.
"""

class Solution:
    """
    @param: A: An integer array.
    @return: nothing
    先把正负数 partition 开，然后再相向双指针进行交换。
    """
    def rerange(self, A):
        # write your code here
        pos, neg = 0, 0
        for num in A:
            if num > 0:
                pos += 1
            else:
                neg += 1
        self.partition(A, pos > neg)
        self.interleave(A, pos == neg)

    def partition(self, A, start_positive):
        flag = 1 if start_positive else -1
        left, right = 0, len(A) - 1
        while left < right:
            while left < right and A[left] * flag > 0:
                left += 1
            while left < right and A[right] * flag < 0:
                right -= 1
            if left < right:
                A[left], A[right] = A[right], A[left]
                left += 1
                right -= 1

    def interleave(self, A, has_same_length):
        left, right = 1, len(A) - 1
        if has_same_length:
            right = len(A) - 2
        while left < right:
            A[left], A[right] = A[right], A[left]
            left, right = left + 2, right - 2


