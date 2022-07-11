"""
You are given two integer arrays persons and times. In an election, the ith vote was cast for persons[i] at time times[i].

For each query at a time t, find the person that was leading the election at time t. Votes cast at time t will count towards our query. In the case of a tie, the most recent vote (among tied candidates) wins.

Implement the TopVotedCandidate class:

TopVotedCandidate(int[] persons, int[] times) Initializes the object with the persons and times arrays.
int q(int t) Returns the number of the person that was leading the election at time t according to the mentioned rules.
 

Example 1:

Input
["TopVotedCandidate", "q", "q", "q", "q", "q", "q"]
[[[0, 1, 1, 0, 0, 1, 0], [0, 5, 10, 15, 20, 25, 30]], [3], [12], [25], [15], [24], [8]]
Output
[null, 0, 1, 1, 0, 0, 1]

Explanation
TopVotedCandidate topVotedCandidate = new TopVotedCandidate([0, 1, 1, 0, 0, 1, 0], [0, 5, 10, 15, 20, 25, 30]);
topVotedCandidate.q(3); // return 0, At time 3, the votes are [0], and 0 is leading.
topVotedCandidate.q(12); // return 1, At time 12, the votes are [0,1,1], and 1 is leading.
topVotedCandidate.q(25); // return 1, At time 25, the votes are [0,1,1,0,0,1], and 1 is leading (as ties go to the most recent vote.)
topVotedCandidate.q(15); // return 0
topVotedCandidate.q(24); // return 0
topVotedCandidate.q(8); // return 1

 

Constraints:

1 <= persons.length <= 5000
times.length == persons.length
0 <= persons[i] < persons.length
0 <= times[i] <= 109
times is sorted in a strictly increasing order.
times[0] <= t <= 109
At most 104 calls will be made to q.
"""

"""
refer:https://www.youtube.com/watch?v=_HDRtskOT_U
Precomputed Answer + Binary Search.
Constructor: O(N). each query: O(logN)
"""
class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        p_to_cnt = defaultdict(int)
        max_cnt = 0
        self.winners = []
        for p, t in zip(persons, times):
            p_to_cnt[p] += 1
            if p_to_cnt[p] >= max_cnt:
                self.winners.append((t, p))
                max_cnt = p_to_cnt[p]
            else:
                self.winners.append((t, self.winners[-1][1]))

    def q(self, t: int) -> int:
        if t >= self.winners[-1][0]:
            return self.winners[-1][1]
        start, end = 0, len(self.winners) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if self.winners[mid][0] >= t:
                end = mid
            else:
                start = mid
        if self.winners[end][0] <= t:
            return self.winners[end][1]
        else:
            return self.winners[start][1]


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)

