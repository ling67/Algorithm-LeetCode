/*
Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).

Implement the MyStack class:

void push(int x) Pushes element x to the top of the stack.
int pop() Removes the element on the top of the stack and returns it.
int top() Returns the element on the top of the stack.
boolean empty() Returns true if the stack is empty, false otherwise.
Notes:

You must use only standard operations of a queue, which means that only push to back, peek/pop from front, size and is empty operations are valid.
Depending on your language, the queue may not be supported natively. You may simulate a queue using a list or deque (double-ended queue) as long as you use only a queue's standard operations.
 

Example 1:

Input
["MyStack", "push", "push", "top", "pop", "empty"]
[[], [1], [2], [], [], []]
Output
[null, null, null, 2, 2, false]

Explanation
MyStack myStack = new MyStack();
myStack.push(1);
myStack.push(2);
myStack.top(); // return 2
myStack.pop(); // return 2
myStack.empty(); // return False
*/

class MyStack {
    
    private Queue<Integer> queue1;
    private Queue<Integer> queue2;

    public MyStack() {
        queue1 = new LinkedList<Integer>();
        queue2 = new LinkedList<Integer>();
    }
    
    public void push(int x) {
        queue1.add(x);
    }
    
    public int pop() {
        //如果queue1未空，代表栈顶在queue2，交换
        if (queue1.isEmpty()) {
            Queue temp = queue1;
            queue1 = queue2;
            queue2 = temp;
        }
        
        //将queue1前n-1个放入queue2，获得最后的元素
        while (queue1.size() > 1) {
            queue2.add(queue1.poll());
        }
        return queue1.poll();
    }
    
    public int top() {
        //如果queue1未空，代表栈顶在queue2，交换
        if (queue1.isEmpty()) {
            Queue temp = queue1;
            queue1 = queue2;
            queue2 = temp;
        }
        
        //将queue1前n-1个放入queue2，获得最后的元素
        while (queue1.size() > 1) {
            queue2.add(queue1.poll());
        }
        return queue1.peek();
    }
    
    public boolean empty() {
        return queue1.isEmpty() && queue2.isEmpty();
    }
}

/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack obj = new MyStack();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.top();
 * boolean param_4 = obj.empty();
 */


class MyStack:

    def __init__(self):
        self.q1 = collections.deque()    #store element
        self.q2 = collections.deque()    #help space

    def push(self, x: int) -> None:
        while self.q1:
            self.q2.append(self.q1.popleft())
        self.q1.append(x)
        while self.q2:
            self.q1.append(self.q2.popleft())

    def pop(self) -> int:
        if len(self.q1) == 0:
            raise IndexError("The stack is empty")
        return self.q1.popleft()

    def top(self) -> int:
        if len(self.q1) == 0:
            raise IndexError("The stack is empty")
        return self.q1[0]
        
    def empty(self) -> bool:
        return len(self.q1) == 0
        
# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()


