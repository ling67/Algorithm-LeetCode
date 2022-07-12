/*
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.

 

Example 1:

Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4
*/


#Solution 1: use a queue to store the time-linear data and dictionary to store the cache number, very straighr forward.
"""
1. 使用queue去存储最近访问过的key
2. cache去存储key, value
3. get后要更新q
4. put时如果capacity已经不足，要删除最近最久没使用的值
"""

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.q = collections.deque()   #保存key,最recenty used放在最后面，最least used放在最前面
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            self.q.remove(key)        #O(n)
            self.q.append(key)
            return self.cache[key]
        
    def put(self, key: int, value: int) -> None:
        if key not in self.cache:    # if key not in cache, put it in cache and q, and slao check the size of q
            self.cache[key] = value
            self.q.append(key)
            if len(self.q) > self.capacity:
                leastUsedKey = self.q.popleft()
                del self.cache[leastUsedKey]
        else:                       # if key is in cache, then renew it is corresponding value 
            self.cache[key] = value
            self.q.remove(key)     #O(N)
            self.q.append(key)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


#Solution 2: OrderedDict解法
"""
OrderedDict:有顺序的dict, 先加进来的在前面，后加进来的在后面，按照加的顺序来排的。
popitem(last=True)   True的话会把字典的最后返回删除， False的话会把字典的第一个元素返回删除
move_to_end(key, last=True)  True移动到队尾，False移动到队首
"""
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dict = collections.OrderedDict()
        self.size = 0
        
    def get(self, key: int) -> int:
        if key in self.dict:
            self.dict.move_to_end(key)
            return self.dict[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            self.dict[key] = value
            self.dict.move_to_end(key)   #移动到队尾
        else:
            if self.size < self.capacity:
                self.dict[key] = value     #orderedDict一定要放在队尾
                self.size += 1
            else:
                self.dict.popitem(False)   #pop队首的元素，
                self.dict[key] = value
                

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
 

/*
approach1 extends LinkedHashMap
approach2 use list and node
*/
class LRUCache {
    
    class Node {
        Node prev;
        Node next;
        int key;
        int value;
        
        public Node(int key, int value) {
            this.key = key;
            this.value = value;
            this.prev = null;
            this.next = null;
        }
    }
    
    private int capacity;
    private HashMap<Integer, Node> hs = new HashMap<Integer, Node>();
    private Node head = new Node(-1, -1);
    private Node tail = new Node(-1, -1);

    public LRUCache(int capacity) {
        this.capacity = capacity;
        tail.prev = head;
        head.next = tail;
    }
    
    public int get(int key) {
        if (!hs.containsKey(key)) {
            return -1;
        }
        
        // remove current
        Node current = hs.get(key);
        current.prev.next = current.next;
        current.next.prev = current.prev;
        
        //move current to tail
        moveToTail(current);
        
        return hs.get(key).value;
    }
    
    private void moveToTail (Node current) {
        current.prev = tail.prev;
        tail.prev = current;
        current.prev.next = current;
        current.next = tail;
    }
    
    public void put(int key, int value) {
        // get这个方法会把key挪到最末端，因此，不需要再调用moveToTail
        if(get(key) != -1) {
            hs.get(key).value = value;
            return;
        }
        
        if (hs.size() == capacity) {
            hs.remove(head.next.key);
            head.next = head.next.next;
            head.next.prev = head;
        }
        
        Node insert = new Node(key, value);
        hs.put(key, insert);
        moveToTail(insert);
    }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */


