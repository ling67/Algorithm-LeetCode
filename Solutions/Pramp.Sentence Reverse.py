"""
You are given an array of characters arr that consists of sequences of characters separated by space characters. Each space-delimited sequence of characters defines a word.

Implement a function reverseWords that reverses the order of the words in the array in the most efficient manner.

Explain your solution and analyze its time and space complexities.

Example:

input:  arr = [ 'p', 'e', 'r', 'f', 'e', 'c', 't', '  ',
                'm', 'a', 'k', 'e', 's', '  ',
                'p', 'r', 'a', 'c', 't', 'i', 'c', 'e' ]

output: [ 'p', 'r', 'a', 'c', 't', 'i', 'c', 'e', '  ',
          'm', 'a', 'k', 'e', 's', '  ',
          'p', 'e', 'r', 'f', 'e', 'c', 't' ]
Constraints:

[time limit] 5000ms

[input] array.character arr

0 ≤ arr.length ≤ 100
[output] array.character
"""

"""
One possible solution is doing a linear iteration on arr while pushing a copy of every word to a stack and then pulling them in reverse order while copying the words back into arr. Another approach is initializing a new array at the same length, iterating over arr from right to left and copying any sequence of characters to the new array from left to right. Both approaches take O(N) time and at least O(N) space.

A more elegant and efficient approach is to reverse all the characters in arr and then reverse the characters in each word separately. While the first reverse gives us the words in the reverse order as we wanted, it also reverses the characters of each word. To fix that, we do the second reverse, which reverses each word separately.

Reversing items in an array is done by a ‘mirror’ function, that swaps the items of every 2 indices with the same distance from the middle.
"""



def reverse_helper(arr, start, end):
    while start < end:
      arr[start], arr[end] = arr[end], arr[start]
      start += 1
      end -= 1

def reverse_words(arr):
  #reverse all characters 
  n = len(arr)
  reverse_helper(arr, 0, n - 1)

  word_start = 0  
  for i in range(n + 1):
    if i == n or arr[i] == " ":   
      reverse_helper(arr, word_start, i - 1)
      word_start = i + 1
      
  return arr
