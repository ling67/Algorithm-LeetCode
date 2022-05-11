/*
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
 

Example 1:

Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2

*/


/*
there are two method to solve this problem
approch 1: we can use stack store the min value, each time we push number to stack, we store the min value in stack as well
approch 2: we use two stack, one can be use to store value, the other one can be use to store min value.
*/
class MinStack:

    def __init__(self):
        self.st = []

    def push(self, val: int) -> None:
        self.st.append(val)

    def pop(self) -> None:
        if len(self.st) == 0:
            raise IndexError("The stack is empty!")
        return self.st.pop()

    def top(self) -> int:
        if len(self.st) == 0:
            raise IndexError("The stack is empty!")
        return self.st[-1]
        
    def getMin(self) -> int:   #注意没有说删除最小值
        if len(self.st) == 0:
            raise IndexError("The stack is empty!")
        minValue = min(self.st)
        return minValue
        
            
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
 
