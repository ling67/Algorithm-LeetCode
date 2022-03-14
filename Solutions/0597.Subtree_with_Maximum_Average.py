/*
Description
Given a binary tree, find the subtree with maximum average. Return the root of the subtree.

Contact me on wechat to get more FLAMG requent Interview questions . (wechat id : jiuzhang15)

LintCode will print the subtree which root is your return node.
It's guaranteed that there is only one subtree with maximum average.

Example
Example 1

Input：
{1,-5,11,1,2,4,-2}
Output：11
Explanation:
The tree is look like this:
     1
   /   \
 -5     11
 / \   /  \
1   2 4    -2 
The average of subtree of 11 is 4.3333, is the maximun.
Example 2

Input：
{1,-5,11}
Output：11
Explanation:
     1
   /   \
 -5     11
The average of subtree of 1,-5,11 is 2.333,-5,11. So the subtree of 11 is the maximun.
*/


/**
 * Definition of TreeNode:
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left, right;
 *     public TreeNode(int val) {
 *         this.val = val;
 *         this.left = this.right = null;
 *     }
 * }
 */


from lintcode import (
    TreeNode,
)

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root of binary tree
    @return: the root of the maximum average of subtree
    """
    def find_subtree2(self, root: TreeNode) -> TreeNode:
        # write your code here
        if not root:
            return root
        self.max_avg = float("-inf")
        self.max_root = root
        self.help(root)

        return self.max_root

    #return sum and num
    def help(self, root: TreeNode):
        if not root:
            return 0, 0

        #divide
        left_cnt, left_sum = self.help(root.left)
        right_cnt, right_sum = self.help(root.right)

        #conquer
        cnt = left_cnt + right_cnt + 1
        sum = left_sum + right_sum + root.val
        avg = sum / cnt
        
        #traverse to compare
        if avg > self.max_avg:
            self.max_avg = avg
            self.max_root = root
        
        return cnt, sum



public class Solution {
    /**
     * @param root: the root of binary tree
     * @return: the root of the maximum average of subtree
     */
    class ResultType {
        public int sum, num;
        public ResultType(int sum, int num) {
           this.sum = sum;
           this.num = num;
       }
    }

    private ResultType maxAvg = null;
    private TreeNode maxNode = null;

    public TreeNode findSubtree2(TreeNode root) {
        // write your code here
        if (root == null) {
            return null;
        }
        help(root);
        return maxNode;
    }

    //1.return sum and count
    public ResultType help(TreeNode root) {
        //4.exit
        if (root == null) {
            return new ResultType(0, 0);
        }
        //2.divide
        ResultType left = help(root.left);
        ResultType right = help(root.right);
        //3.conquer
        int sum = left.sum + right.sum + root.val;
        int num = left.num + right.num + 1;
        ResultType rootResult = new ResultType(sum, num);

        if (maxAvg == null || sum * maxAvg.num > num * maxAvg.sum) {
            maxAvg = rootResult;
            maxNode = root;
        }
        
        return rootResult;
    }
}

