"""
The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value and the median is the mean of the two middle values.

For example, for arr = [2,3,4], the median is 3.
For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
Implement the MedianFinder class:

MedianFinder() initializes the MedianFinder object.
void addNum(int num) adds the integer num from the data stream to the data structure.
double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.
 

Example 1:

Input
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]
Output
[null, null, null, 1.5, null, 2.0]

Explanation
MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(1);    // arr = [1]
medianFinder.addNum(2);    // arr = [1, 2]
medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
medianFinder.addNum(3);    // arr[1, 2, 3]
medianFinder.findMedian(); // return 2.0
 

Constraints:

-105 <= num <= 105
There will be at least one element in the data structure before calling findMedian.
At most 5 * 104 calls will be made to addNum and findMedian.
"""

"""
Maintain left_hq as a max heap, right_hq as a min heap
每次新增一个数的时候，先根据比 maxheap 中最后一个数 大还是小丢到对应的 heap 里。
丢完以后，再处理左右两边的平衡性:
如果左边太少了，就从右边拿出一个最小的丢到左边。
如果右边太少了，从左边拿出一个最大的丢到右边。
"""
class MedianFinder:

    def __init__(self):
        self.left_hq = [] #max heap
        self.right_hq = [] #min heap

    def addNum(self, num: int) -> None:
        if len(self.left_hq) == 0 or num <= -self.left_hq[0]:
            heappush(self.left_hq, -num)
        else:
            heappush(self.right_hq, num)
            
        # we want to maintain the lens of leftHq equal or slightly larger to rightHq
        if len(self.left_hq) < len(self.right_hq):
            heappush(self.left_hq, -heappop(self.right_hq))
        elif len(self.right_hq) < len(self.left_hq) - 1:
            heappush(self.right_hq, -heappop(self.left_hq))
            
    def findMedian(self) -> float:
        if len(self.left_hq) == len(self.right_hq):
            return (-self.left_hq[0] + self.right_hq[0]) / 2
        else:
            return -self.left_hq[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
