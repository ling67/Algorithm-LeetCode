//



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

//Version 1: divide
public class Solution {
    /**
     * @param root: the root of the binary tree
     * @return: all root-to-leaf paths
     */

    //先判断我们要的接口和他给的接口是不是一样的，是一样的就不需要再写一个方法调用了

    //1.return all root-to-leaf paths 
    public List<String> binaryTreePaths(TreeNode root) {
        // write your code here
        List<String> paths = new ArrayList<>();

        //3.exit null + leaf 出口想清楚是null还是null+leaf
        if (root == null) {
            return paths;
        }

        //leaf
        if (root.left == null && root.right == null) {
            paths.add("" + root.val);
            return paths;
        }

        //2. split
        List<String> left = binaryTreePaths(root.left);
        List<String> right = binaryTreePaths(root.right);
        for (String path : left){
            paths.add(root.val + "->" + path);
        }
        for (String path : right){
            paths.add(root.val + "->" + path);
        }

        return paths;
    }
  
  
  //Version 2: revise
  
  

