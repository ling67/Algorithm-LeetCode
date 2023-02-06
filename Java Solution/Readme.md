## [Array]()

```python
模板(背诵)：
```
- [0001.Two_Sum.java](0001.Two_Sum.java) (E) <br>  
Brute force, Hashmap, Two Point(can't use)
- [0015.3Sum.java](0015.3Sum.java) (M) <br> 
two point then use set to remove repeat array. (more easy)
- [0121.Best_Time_to_Buy_and_Sell_Stock.java](0121.Best_Time_to_Buy_and_Sell_Stock.java) (E) <br> 
Traverse the array and record the max profit
- [0169.Majority_Element.java](0169.Majority_Element.java) (E) <br>  
method 1: sort then return the middle element
method 2: hashmap record the feq of the element
- [0217.Contains_Duplicate.java](0217.Contains_Duplicate.java) (E) <br>  
compare the size of hashmap and length of array
- [0057.Insert_Interval.java](0057.Insert_Interval.java) (M) <br>  
for loop to traverse the array. there are 3 situation. 1.when I can directly to add interval. 2.when I can directly to add newInterval.3.when I need combin interval and newInterval.
- [0238.Product_of_Array_Except_Self.java](0238.Product_of_Array_Except_Self.java) (M) <br>  
Solution 1: brute force  time limit exceeded
Solution 2: using dividion operation. If there is 0 in the array, you can't use this method.
Solution 3: Finding Prefix Product and Suffix Product, it is hard to make sure the index.
- [0039.Combination_Sum.java](0039.Combination_Sum.java) (M) <br>  
Backtrack!


