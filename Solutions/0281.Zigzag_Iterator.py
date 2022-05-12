Given two vectors of integers v1 and v2, implement an iterator to return their elements alternately.

Implement the ZigzagIterator class:

ZigzagIterator(List<int> v1, List<int> v2) initializes the object with the two vectors v1 and v2.
boolean hasNext() returns true if the iterator still has elements, and false otherwise.
int next() returns the current element of the iterator and moves the iterator to the next element.
 

Example 1:

Input: v1 = [1,2], v2 = [3,4,5,6]
Output: [1,3,2,4,5,6]
Explanation: By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,3,2,4,5,6].
Example 2:

Input: v1 = [1], v2 = []
Output: [1]
Example 3:

Input: v1 = [], v2 = [1]
Output: [1]
 

Constraints:

0 <= v1.length, v2.length <= 1000
1 <= v1.length + v2.length <= 2000
-231 <= v1[i], v2[i] <= 231 - 1

#1.two point
#2.Queue
class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.idx1 = 0
        self.idx2 = 0
        self.flag = True   #flag = True means take from v1
        self.v1 = v1
        self.v2 = v2

    def next(self) -> int:
        if self.hasNext():
            if self.idx2 >= len(self.v2) or (self.flag and self.idx1 < len(self.v1)):
                res = self.v1[self.idx1]
                self.idx1 += 1
                self.flag = not self.flag
            elif self.idx1 >= len(self.v1) or (not self.flag and self.idx2 < len(self.v2)):
                res = self.v2[self.idx2]
                self.idx2 += 1
                self.flag = not self.flag
            return res

    def hasNext(self) -> bool:
        if self.idx1 >= len(self.v1) and self.idx2 >= len(self.v2):
            return False
        return True

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())
