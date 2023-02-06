//Solution 1: brute force  time limit exceeded
class Solution {
    public int[] productExceptSelf(int[] nums) {
        int n = nums.length;
        int ans[] = new int[n];

        for (int i = 0; i < n; i++) {
            int pro = 1;
            for (int j = 0; j < n; j++) {
                if (i == j) continue;
                pro *= nums[j];
            }
            ans[i] = pro;
        }
        return ans;
    }
}

//Solution 2: using dividion operation. If there is 0 in the array, you can't use this method.
class Solution {
    public int[] productExceptSelf(int[] nums) {
        int n = nums.length;
        int[] res = new int[n];
        int pro = 1;
        for (int num : nums) {
            pro *= num;
        }

        for (int i = 0; i < n; i++) {
            res[i] = pro / nums[i];
        }

        return res;
    }
}

//Solution 3: Finding Prefix Product and Suffix Product, it is hard to make sure the index
class Solution {
    public int[] productExceptSelf(int[] nums) {
        int n = nums.length;
        int pre[] = new int[n];
        int suff[] = new int[n];
        int res[] = new int[n];

        pre[0] = 1;
        suff[n - 1] = 1;

        for (int i = 1; i < n; i++) {
            pre[i] = pre[i - 1] * nums[i - 1];
        }

        for (int i = n - 2; i >= 0; i--) {
            suff[i] = suff[i + 1] * nums[i + 1];
        }

        for (int i = 0; i < n; i++) {
            res[i] = pre[i] * suff[i];
        }

        return res;
    }
}



