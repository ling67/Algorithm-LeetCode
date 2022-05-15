/*
Design a data structure that accepts a stream of integers and checks if it has a pair of integers that sum up to a particular value.

Implement the TwoSum class:

TwoSum() Initializes the TwoSum object, with an empty array initially.
void add(int number) Adds number to the data structure.
boolean find(int value) Returns true if there exists any pair of numbers whose sum is equal to value, otherwise, it returns false.
 

Example 1:

Input
["TwoSum", "add", "add", "add", "find", "find"]
[[], [1], [3], [5], [4], [7]]
Output
[null, null, null, null, true, false]

Explanation
TwoSum twoSum = new TwoSum();
twoSum.add(1);   // [] --> [1]
twoSum.add(3);   // [1] --> [1,3]
twoSum.add(5);   // [1,3] --> [1,3,5]
twoSum.find(4);  // 1 + 3 = 4, return true
twoSum.find(7);  // No two integers sum up to 7, return false
*/

#python version
class TwoSum(object):
    
    def __init__(self):
        self.nums = []

    def add(self, number):
        """
        :type number: int
        :rtype: None
        """
        self.nums.append(number)

    def find(self, value):
        """
        :type value: int
        :rtype: bool
        """
        num_set = set()
        for i, num in enumerate(self.nums):
            if value - num in num_set:
                return True
            num_set.add(num)
        return False
        


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)


class TwoSum {
    HashMap<Integer, Integer> num_cnts;
    
    public TwoSum() {
        this.num_cnts = new HashMap<Integer, Integer>();
    }
    
    public void add(int number) {
        if (this.num_cnts.containsKey(number)) {
            this.num_cnts.replace(number, this.num_cnts.get(number) + 1);
        } else {
            this.num_cnts.put(number, 1);
        }
    }
    
    public boolean find(int value) {
        for (Map.Entry<Integer, Integer> entry : this.num_cnts.entrySet()) {  //map的遍历记住
            int key = entry.getKey();
            if (this.num_cnts.containsKey(value - key)) {
                if (value - key != key) {
                    return true;
                } 
                if (entry.getValue() > 1) {
                    return true;
                }
            } 
        }
        return false;
    }
}

/**
 * Your TwoSum object will be instantiated and called as such:
 * TwoSum obj = new TwoSum();
 * obj.add(number);
 * boolean param_2 = obj.find(value);
 */
