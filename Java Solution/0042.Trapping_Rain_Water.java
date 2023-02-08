//Solution: Two Pointer
class Solution {
    public int trap(int[] height) {
        int water = 0;
        int l = 0, r = height.length - 1;
        int lmax = height[l], rmax = height[r];

        while (l <= r) {
            if (lmax < rmax) {
                lmax = Math.max(lmax, height[l]);
                water += lmax - height[l];
                l++;
            } else {
                rmax = Math.max(rmax, height[r]);
                water += rmax - height[r];
                r--;
            }
        }
        return water;
    }
}
