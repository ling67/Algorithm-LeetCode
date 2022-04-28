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
        self.vectors = [v1, v2]
        self.queue = deque()
        for index, vector in enumerate(self.vectors):
            if len(vector) > 0:
                self.queue.append((index, 0))

    def next(self) -> int:
        if self.queue:
            vec_index, elem_index = self.queue.popleft()
            next_elem_index = elem_index + 1
            if next_elem_index < len(self.vectors[vec_index]):
            # append the pointer for the next round
            # if there are some elements left
                self.queue.append((vec_index, next_elem_index))
        return self.vectors[vec_index][elem_index]

    def hasNext(self) -> bool:
        return len(self.queue) > 0

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())
