Skip to content
Search or jump to…
Pull requests
Issues
Marketplace
Explore
 
@jim0607 
jim0607
/
Leetcode
Private template
Code
Issues
Pull requests
Actions
Projects
Security
Insights
Settings
Leetcode/Solutions/Google__Max_Absolute_Difference_of_Subarrays.py /
@jim0607
jim0607 Update Google__Max_Absolute_Difference_of_Subarrays.py
Latest commit a92d56a on Dec 1, 2020
 History
 1 contributor
156 lines (118 sloc)  3.76 KB
   
"""
Given an array of integers. 
Find two disjoint subarrays such that the absolute difference between the sum of the two subarrays is maximum 
Example: [-1 -2 1 -4 0 2 8] 
ans: (-1 -2 1 -4)  (2 8)  diff = 10 - (-6) = 16.
知识点：
Subarray就是连续的
Subsequence是不一定连续的
"""


解法：
step 1: 构造一个prefix_sum list和一个suffix_sum list.

step 2: 用这两个list计算出dp1 list, dp2 list, dp3 list, dp4 lsit. 
dp1[i] = the max subarray sum before i;
transition function 参考53. Maximum Subarray:
用一个辅助variable: min_presum
for i, presum in enumerate(pre_sums):
    dp1[i] = max(dp1[i-1], presum - min_presum)    # max(不以i结尾的max_subarry_sum, 以i结尾的max_subarry_sum)
    min_presum = min(min_presum, presum)

dp2[i] = the min subarray sum before i;
dp3[i] = the max subarray sum after i;
dp4[i] = the min subarray sum after i.

step 3: 从左到右遍历一遍，比较i左右两边的min 和 max, 更新max_abs_diff即可。
for i in range(len(nums)):
    res = max(res, abs(dp1[i] - dp4[i]), abs(dp2[i] - dp3[i]))

Time and space: O(N), O(N)





 
 


//  -6 -8 diff = 2 - 
// sum1 > 0 && sum2 > 0 || sum1 < 0 && sum2 < 0 

// min sum value of subarray dp O(n)
// max sum value of subarray dp O(n)
// [2 -1 -2 1 -4 2 -3 8] ((-1 -2 1 -4))
//  [-1, -2, 5 , -6]

// [-1, -2, 5, -6] 

// max
// [-1] -1
// [-1 -2] -1
// [-1 -2 5] 5
// [-1 -2 5 -6] 5 
// [-1 -2 5 -6 12] 12

// -1        -6 12
// [-1, -2,| 5, -6 12] 
// running maximum.
//. -1. -1  5  5  12
// maximum & minimum value for every index 
// we need left-> right
// we need right-> left
// [-1, -2,| 5, -6 12]
// [12] 12
// [12, -6] 12 right -> left
// left -> right [5, -6]
// [12, -6, 5]]


// [2 -1 -2 1 -4 2 8] 

// [2  2. 2 2. 2 2 10] maximum
// [2  -1 -3 -3 -6 -6 -6] minimum


// [8, 10, 10, 10, 10, 10, 10] maximum
// [8, 2, -4, -4, -5, -6, -6]  minimum
 
// two arrays
// [-1][-2,5,-6]
// -1, 3 * 2  min & max value
// min from 1  max from 2 
// max from 1  min from 2
// 
// n * breaking(O(n))
// 


// -1 -2 1 -4 2 -2

// 2 -2 8

//(  )
// 10 ^ 4  100 -> N^3 maybe N^4.
// 2<=arr.length<=10^5  => O(NlgN) O(N)  10^10 -> 3Ghz CPU runs for a couple of mins maybe 


//-1, -2, 5, -6, 12
// 0, -1, -3, 2, -4, 8
// sum[i - j] = preSum[j + 1] - preSum[i];
//d  0, 0, -1, -3, -3, -4
//
  
int maxAbsDiff(List<int> arr) {
  
  // calcaluate leftToRightRunningMax.
  // [2 -1 -2 1 -4 2 8] 
  // DP[I] using DP[X] X<I
  List<int> subSum = new ArrayList<>();
  int[] dp = new int[n];
  dp[0] = arr.get(0);
     // dp[i] 0 <  dp[i - 1] 
  // > 0 dp 
//   DP[i - 1] < 0 nums[i]
//   DP[i - 1] > 0 dp[i - 1] + nums[i]
  // 
  int max=INT_MIN;
  // -1, -2, 5, -6, 12
  // dp = [(float("-inf"),float("-inf")) for i in range(len(input_list)))], 
  // # first element is so far what is the maximum, second element is what is the maximum including current element
  //   -1, -1
  //   -1, -2
  //    5, 5
  //    5, -1
  //   12, 12
    // dp[i][1] = Math.max(dp[i - 1][1] + nums[i] , nums[i])
//   dp linear
  // subarray max sum stream
//   
  for (int i = 1; i < n; i++) {
    dp[i] = Math.max(arr[i], arr[i]+dp[i-1]);// i + 1
    max=Math.max(max, dp[i]);
    subSum[i]=max;
  }
  
  List<Integer> leftToRightRunningMax, leftToRightRunningMin, rightToLeftRunningMin, rightToLeftRunningMax;
  // in the right part we choose the element from right to left 
  int rs = 0; // bottom here is zero.
  for (int i = 1; i < arr.size(); i++) {
    int leftMax = leftToRightRunningMax[i];
    int leftMin = leftToRightRunningMin[i];
    int rightMax = rightToLeftRunningMax[arr.size() - i];
    int rightMin = rightToLeftRunningMin[arr.size() - i];
    // 8  6
    int sum1 = Math.abs(rightMax - leftMin);// if leftMin < 0;
    int sum2 = Math.abs(leftMax - rightMin);
    
    rs = Math.max(Math.max(sum1, sum2), rs);
  }
  
  return rs;
}

