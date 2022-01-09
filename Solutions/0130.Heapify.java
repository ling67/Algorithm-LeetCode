/*
escription
Given an integer array, heapify it into a min-heap array.

For a heap array A, A[0] is the root of heap, and for each A[i], A[i * 2 + 1] is the left child of A[i] and A[i * 2 + 2] is the right child of A[i].

What is heap? What is heapify? What if there is a lot of solutions?

Heap is a data structure, which usually have three methods: push, pop and top. where "push" add a new element the heap, "pop" delete the minimum/maximum element in the heap, "top" return the minimum/maximum element.
Convert an unordered integer array into a heap array. If it is min-heap, for each element A[i], we will get A[i * 2 + 1] >= A[i] and A[i * 2 + 2] >= A[i].
Return any of them.
*/

//区别是向上调还是向下调，跟孩子比较就是向下调，跟父亲比较就是向上调，就决定了时间复杂度

//version 1 siftup nlogn
public class Solution {
    /*
     * @param A: Given an integer array
     * @return: nothing
     */
    public void heapify(int[] A) {
        // write your code here
        for (int i = 0; i < A.length; i++) {
            siftup(A, i);
        }
    }

    private void siftup(int[] A, int n) {
        while (n != 0) {
            int father = (n - 1) / 2;
            if (A[n] > A[father]) {
                break;
            }
            int temp = A[n];
            A[n] = A[father];
            A[father] = temp;
            n = father;
        }
    }
}
 
//version 2. siftdown n
public class Solution {
    /*
     * @param A: Given an integer array
     * @return: nothing
     */
    public void heapify(int[] A) {
        // write your code here
        for (int i = A.length / 2; i >= 0; i--) {
            siftdown(A, i);
        }
    }

    private void siftdown(int[] A, int k) {
        while (k < A.length) {
            int smallest = k;
            if (k * 2 + 1 < A.length && A[k * 2 + 1] < A[smallest]) {
                smallest = k * 2 + 1;
            }
            if (k * 2 + 2 < A.length && A[k * 2 + 2] < A[smallest]) {
                smallest = k * 2 + 2;
            }
            if (smallest == k) {
                break;
            }
            int temp = A[smallest];
            A[smallest] = A[k];
            A[k] = temp;
            k = smallest;
        }
    }
}





