/*
描述
给定n本书，第i本书有[i]页。有k个人来抄这些书。

这些书排成一行，每个人都可以索取连续一段的书。例如，一个复印机可以连续地将书从第i册复制到第j册，但是他不能复制第1册、第2册和第4册（没有第3册）。

他们在同一时间开始抄书，每抄一页书都要花1分钟。为了让最慢的复印机能在最早的时间完成书的分配，最好的策略是什么？

请返回最慢复印机花费的最短时间。

书籍页数总和小于等于2147483647

样例
样例 1:

输入: pages = [3, 2, 4], k = 2
输出: 5
解释: 第一个人复印前两本书, 耗时 5 分钟. 第二个人复印第三本书, 耗时 4 分钟.
样例 2:

输入: pages = [3, 2, 4], k = 3
输出: 4
解释: 三个人各复印一本书.
挑战
时间复杂度 O(nk)
*/

//version 1: 二分答案 python version
class Solution:
    """
    @param pages: an array of integers
    @param k: An integer
    @return: an integer
    """
    def copy_books(self, pages: List[int], k: int) -> int:
        # write your code here
        if not pages:
            return 0

        start, end = max(pages), sum(pages)
        while start + 1 < end:
            mid = start + (end - start) // 2
            if self.is_possible(pages, mid, k):
                end = mid
            else:
                start = mid
        return start if self.is_possible(pages, start, k) else end

    def is_possible(self, pages, threshold, k):
        people_needed = 1
        curr_time = 0
        for page in pages:
            if curr_time + page > threshold:
                people_needed += 1
                curr_time = 0
            curr_time += page
        return people_needed <= k

"""需要找到一种分段方式，使得所有段的数字之和的最大值最小
f[k][i]=前k个(不包括k)抄写员最多需要多长时间抄完前i本书(不包括i)
f[k][j]=min(max(f[k-1][i], i~j所需时间)) for 0<i <j
初始条件：f[k][0]=0; f[0][0]=0; f[0][i] = inf for i > 0
O(N^2*K), O(N*K)"""
class Solution:
    """
    @param pages: an array of integers
    @param k: An integer
    @return: an integer
    """
    def copyBooks(self, pages, k):
        lens = len(pages)
        dp = [[float("inf")] * (lens + 1) for _ in range(k + 1)]
        
        for m in range(k + 1):
            dp[m][0] = 0
            for j in range(1, lens + 1):
                dp[0][j] = float("inf")
                
        for m in range(1, k + 1):
            for j in range(1, lens + 1):
                for i in range(j):
                    tempMax = max(dp[m - 1][i], sum(pages[i:j]))
                    dp[m][j] = min(dp[m][j], tempMax)
                    
        return dp[k][lens]


//version 1: 二分答案 java version
public class Solution {
    /**
     * @param pages: an array of integers
     * @param k: An integer
     * @return: an integer
     */
    public int copyBooks(int[] pages, int k) {
        // write your code here

        if (pages ==  null || pages.length == 0) {
            return 0;
        }

        if (k == 0) {
            return -1;
        }

        int total = 0;

        int max = pages[0]; 
        for (int i = 0; i < pages.length; i++) {
            total += pages[i];
            if(pages[i] > max){
                max = pages[i];
            }
        }

        int start = max, end = total;
        while (start + 1 < end) {
            int mid = start + (end - start) / 2;
            if (canFinish(pages, mid) > k) {
                start = mid;
            } else {
                end = mid;
            } 
        }

        if (canFinish(pages, start) <= k){
            return start;
        }
        return end;
    }

    // return how many people we need to finish all pages in time 
    private int canFinish(int pages[], int time) {
        if (pages == null) {
            return 0; 
        }

        int peopleNeeded = 1;

        int remainTime = time;
        for(int i = 0; i < pages.length; i++) {
            if(remainTime >= pages[i]) {
                remainTime = remainTime - pages[i];
            } else {
                peopleNeeded += 1;
                remainTime = time - pages[i];
            }
        }
        return peopleNeeded;
    }
}

//version 2: 划分性动态规划

需要找到一种分段方式，是的所有短的数字之和的最大值最小
f[k][i] =前K个（不包含k）抄写员最多需要多长时间抄完前i本书（不包括i）








