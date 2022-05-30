"""
The deletion distance of two strings is the minimum number of characters you need to delete in the two strings in order to get the same string. For instance, the deletion distance between "heat" and "hit" is 3:

By deleting 'e' and 'a' in "heat", and 'i' in "hit", we get the string "ht" in both cases.
We cannot get the same string from both strings by deleting 2 letters or fewer.
Given the strings str1 and str2, write an efficient function deletionDistance that returns the deletion distance between them. Explain how your function works, and analyze its time and space complexities.

Examples:

input:  str1 = "dog", str2 = "frog"
output: 3

input:  str1 = "some", str2 = "some"
output: 0

input:  str1 = "some", str2 = "thing"
output: 9

input:  str1 = "", str2 = ""
output: 0
Constraints:

[input] string str1
[input] string str2
[output] integer

"""

"""
step1: get max number of same string in this two string: lens
step2: len(str1) + len(str2) -  2 * lens
str1 = dog str2 = frog
bruth force method, fixed str1, 
compare the character in str2 to str1
d str2 frog campare, 0
o str2 frog campare o == o so, move str1, str2 g == g len = 2
time complexity is O(m*n) m is len str1 n is len str2
Dynamic programming method
define state dp[i][j] repersent the max same cha in both str1[0:i] and str2[0:j]
what result? dp[len(str1)][len(str2)] 
initialize dp[0][0] = 0
recurtion function: dp[i][j] = if str1[i-1] == str2[j-1] dp[i-1][j-1] but if str1[i-1] != str2[j-1]
max(dp[i][j-1] or dp[i-1][j])

"""
def deletion_distance(str1, str2):
  m = len(str1)
  n = len(str2)
  
  dp = [[0] * (n+1) for _ in range(m+1)]
  
  for i in range(1, m+1):
    for j in range(1, n+1):
      if str1[i-1] == str2[j-1]:
        dp[i][j] = dp[i-1][j-1] + 1
      else:
        dp[i][j] = max(dp[i-1][j], dp[i][j-1])
  
  res = m + n - 2*dp[m][n]
  return res
