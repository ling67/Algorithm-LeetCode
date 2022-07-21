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
        if A is None or len(A) <= 1:
            return

        # Assume A does not contain 0
        l, r = 0, len(A) - 1
        while l <= r:
            while l <= r and A[l] < 0:
                l += 1
            while l <= r and A[r] > 0:
                r -= 1    
            if l <= r:
                A[l], A[r] = A[r], A[l]
                l += 1
                r -= 1

        neg_count = l
        pos_count = len(A) - l

        # the amount of pos and neg number should at most diff by one
        if abs(neg_count - pos_count) > 1:
            return

        l = 1 if neg_count >= pos_count else 0
        r = len(A) - 2 if pos_count >= neg_count else len(A) - 1

        while l < r:
            A[l], A[r] = A[r], A[l]
            l += 2
            r -= 2
