// for loop to traverse the array. there are 3 situation
// when I can directly to add interval
// when I can directly to add newInterval
// when I need combin interval and newInterval

class Solution {
    public int[][] insert(int[][] intervals, int[] newInterval) {
        List<int[]> res = new ArrayList<>();
        int[] toAdd = newInterval;
        for (int i = 0; i < intervals.length; i++) {
            if (intervals[i][1] < toAdd[0]) {
                res.add(intervals[i]);
            } else if (toAdd[1] < intervals[i][0]) {
                res.add(toAdd);
                toAdd = intervals[i];
            } else {
                toAdd = new int[] {Math.min(intervals[i][0], toAdd[0]), Math.max(intervals[i][1], toAdd[1])};
            }
        }
        res.add(toAdd);
        return res.toArray(new int[res.size()][2]);
    }
}
