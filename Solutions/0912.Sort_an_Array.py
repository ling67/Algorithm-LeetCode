/*
Given an array of integers nums, sort the array in ascending order.

Example 1:

Input: nums = [5,2,3,1]
Output: [1,2,3,5]
Example 2:

Input: nums = [5,1,1,2,0,0]
Output: [0,0,1,1,2,5]

*/

#归并排序：NlogN
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        
        # ste p1: divide - 由于每次都是稳定取中间进行divide
        # 所以recursion tree的深度可以稳定在log(N)
        mid = len(nums) // 2
        leftArr = self.sortArray(nums[:mid])
        rightArr = self.sortArray(nums[mid:])
        
        #step2: conquer
        i, j, k = 0, 0, 0
        while i < len(leftArr) and j < len(rightArr):
            if leftArr[i] < rightArr[j]:
                nums[k] = leftArr[i]
                i += 1
                k += 1
            else:
                nums[k] = rightArr[j]
                j += 1
                k += 1
        while i < len(leftArr):
                nums[k] = leftArr[i]
                i += 1
                k += 1
        while j < len(rightArr):
                nums[k] = rightArr[j]
                j += 1
                k += 1      
        return nums
 
#快速排序 NlogN
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.quickSort(nums, 0, len(nums) - 1)
        return nums
    
    def quickSort(self, nums, start, end):
        if start >= end:    # the outlet of the recursion is start >= end
            return 
        
        # 先整体有序
        # 注意这里选取pivot原因不能保证recursion tree深度稳定在log(N)，最坏的情况是深度为N.
        pivot = nums[(start + end) // 2]   # key point 1: pivot is the value, not the index，一定要在while循环外面取值  
        left, right = start, end
        while left <= right:
            while left <= right and nums[left] < pivot:   # 注意点nums[left] < pivot，一定要使用pivot，而不是nums[mid]，因为当nums[i] nums[j]交换之后，数组变了，所以nums[mid]也可能变了
                left += 1
            while left <= right and nums[right] > pivot:  # 注意点nums[left] > pivot 可以将pivot均匀分到两边。
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        
        # 再局部有序, 注意出while循环之后right在左边，所以这里是right
        self.quickSort(nums, start, right) # no return for the quickSort function!
        self.quickSort(nums, left, end)

        
# 冒泡排序 O(n^2)
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n):   #优化1:i代表需要排序的轮数,其实只需要n-1轮就可以
            id_made_swap = False  ## 设置标志位，若本身已经有序，则直接break
            for j in range(n - i - 1):  #j+1为每次能确定的位置 from n - i - 1 = n - 1
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
                    is_made_swap = True    #交换过就设置为true
            if not is_made_swap:
                break
        return nums
    
/******************************************jave version***************************************/
        
//归并排序
class Solution {
    public int[] sortArray(int[] nums) {
        if (nums == null || nums.length == 0) {
            return null;
        }
        int[] temp = new int[nums.length];
        mergeSort(nums, 0, nums.length - 1, temp);
        return nums;
    }
    
    private void mergeSort(int[] nums, int start, int end, int[] temp) {
        if (start >= end) {
            return;
        }
        int left = start, right = end;
        int mid = (start + end) / 2;
        
        //先划分成左右两边的归并排序
        mergeSort(nums, start, mid, temp);
        mergeSort(nums, mid + 1, end, temp);
        merge(nums, start, end, temp);
    }
    
    //将两个排好序的数组合并成一个
    private void merge(int[] nums, int start, int end, int[] temp) {
        int middle = (start + end) / 2;
        int leftStart = start;
        int rightStart = middle + 1;
        int index = leftStart;
        
        while (leftStart <= middle && rightStart <= end) {
            if (nums[leftStart] < nums[rightStart]) {
                temp[index++] = nums[leftStart++];
                
            } else {
                temp[index++] = nums[rightStart++];
            }
        }
        
        while (leftStart <= middle) {
            temp[index++] = nums[leftStart++];
        }
        
        while (rightStart <= end) {
            temp[index++] = nums[rightStart++];
        }
        
        for (int i = start; i <= end; i++) {
            nums[i] = temp[i];
        }
    }
}

//快速排序
class Solution {
    public int[] sortArray(int[] nums) {
        if (nums == null || nums.length <= 1) {
            return nums;
        }
        quickSort(nums, 0, nums.length - 1);
        return nums;
    }
    
    private void quickSort(int[] nums, int start, int end) {
        if (start >= end) {
            return;
        }
        int left = start, right = end;
        
        //1.pivot, A[start], A[end]
        //get value not index
        int pivot = nums[(start + end) / 2]; 
        
        //2.left <= right not left < right
        while (left <= right) {
            //3.A[left] < pivot not <=
            while ((left <= right) && (nums[left] < pivot)) {
                left++;
            }
            while ((left <= right) && (nums[right] > pivot)) {
                right--;
            }
            //这里的判断别忘记了，因为left有可能>right
            if (left <= right) {
                int temp = nums[left];
                nums[left] = nums[right];
                nums[right] = temp;
                left++;
                right--;
            } 
        }
        quickSort(nums, start, right);
        quickSort(nums, left, end);
    }
}
