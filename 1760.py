"""Very classic binary search problem.

Suppose there exist a threshold X where X = argmax/argmin f(X)

1. The time complexity for verify X is a solution need O(n or nlogn) -> Use the idea of NP problem
2. f(X) should be strictly increased/decreased with X

We could use binary search to solve this kind problem

Very Similar to find out solution of x^2 = 2

Similar problems:

774. Minimize Max Distance to Gas Station

"""

class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:

        def min_cut(x, p):
            if x <= p:
                return 0
            if not x % p:
                return x // p - 1
            return x // p

        def get_min_cut_count(nums, p):
            return sum([min_cut(num, p) for num in nums])

        _min, _max = 1, max(nums)
        while _min < _max:
            mid = (_min + _max) // 2
            cut_count = get_min_cut_count(nums, mid)
            if mid == _min:
                if cut_count <= maxOperations:
                    return _min
                return _min + 1
            if cut_count <= maxOperations:
                _max = mid
            else:
                _min = mid
        return _min

