"""
Given n nodes in a graph labeled from 1 to n. There is no edges in the graph at beginning.

You need to support the following method:

connect(a, b), an edge to connect node a and node b
query(a), Returns the number of connected component nodes which include node a.
Contact me on wechat to get Amazon、Google requent Interview questions . (wechat id : jiuzhang15)


Example
Example 1:

Input:
ConnectingGraph2(5)
query(1)
connect(1, 2)
query(1)
connect(2, 4)
query(1)
connect(1, 4)
query(1)
Output:[1,2,3,3]
Example 2:

Input:
ConnectingGraph2(6)
query(1)
query(2)
query(1)
query(5)
query(1)

Output:
[1,1,1,1,1]
"""

class ConnectingGraph2:
    """
    @param: n: An integer
    """
    def __init__(self, n):
        # do intialization if necessary
        self.father = collections.defaultdict()
        self.size = collections.defaultdict()
        for i in range(n+1):
            self.father[i] = i
            self.size[i] = 1

    def find(self, x):
        if self.father[x] == x:
            return x
        self.father[x] = self.find(self.father[x])  #压缩路径
        return self.father[x]
    """
    @param: a: An integer
    @param: b: An integer
    @return: nothing
    """
    def connect(self, a, b):
        # write your code here
        father_a = self.find(a)
        father_b = self.find(b)
        if father_a != father_b:
            self.father[father_a] = father_b
            #记录root快的点数
            self.size[father_b] += self.size[father_a]
        
    """
    @param: a: An integer
    @return: An integer
    """
    def query(self, a):
        # write your code here
        return self.size[self.find(a)]
