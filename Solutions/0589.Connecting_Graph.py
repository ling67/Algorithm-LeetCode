"""
Description
Given n nodes in a graph labeled from 1 to n. There is no edges in the graph at beginning.

You need to support the following method:

connect(a, b), add an edge to connect node a and node b`.
query(a, b), check if two nodes are connected
Contact me on wechat to get Amazon、Google requent Interview questions . (wechat id : jiuzhang15)


Example
Example 1:

Input:
ConnectingGraph(5)
query(1, 2)
connect(1, 2)
query(1, 3) 
connect(2, 4)
query(1, 4) 
Output:
[false,false,true]
Example 2:

Input:
ConnectingGraph(6)
query(1, 2)
query(2, 3)
query(1, 3)
query(5, 6)
query(1, 4)

Output:
[false,false,false,false,false]
"""

class ConnectingGraph:
    """
    @param: n: An integer
    """
    def __init__(self, n):
        # do intialization if necessary
        self.father = collections.defaultdict(int)
        for i in range(1, n + 1):
            self.father[i] = i
    
    def find(self, x):
        if self.father[x] == x:
            return x
        self.father[x] = self.find(self.father[x])
        return self.father[x]
    """
    @param: a: An integer
    @param: b: An integer
    @return: nothing
    """
    def connect(self, a, b):
        # write your code here
        root_a, root_b = self.find(a), self.find(b)
        if root_a != root_b:
            self.father[root_a] = root_b

    """
    @param: a: An integer
    @param: b: An integer
    @return: A boolean
    """
    def query(self, a, b):
        # write your code here
        return self.find(a) == self.find(b)

