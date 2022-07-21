```python
Quick select 模板：（quick sort也套用这个模板！！！）
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
