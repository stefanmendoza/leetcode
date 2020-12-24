import heapq


class Solution:

    # T(n) = O(n + n lg(n) + O(1)) = O(n lg(n))
    #
    # Runtime: 56 ms, faster than 95.30% of Python3 online submissions for Kth Largest Element in an Array.
    # Memory Usage: 15 MB, less than 49.62% of Python3 online submissions for Kth Largest Element in an Array.
    def solution_1(self, nums: List[int], k: int) -> int:
        # O(n)
        heapq.heapify(nums)

        # O(n lg n)
        ascending = sorted(nums)

        # O(1)
        return ascending[k * -1]

    # Instead, you make a smaller, size-n max-heap with the first n items, then do repeated pushpop operations on it
    # with the remaining items from the sequence. Once you're done, you pop the items from the heap and return them in
    # reversed order.
    #
    # This process take O(N log(n)) time (note the small n) and of course only O(n) space. If n is much less than N,
    # it's much more efficient than sorting and slicing.
    #
    # Source: https://stackoverflow.com/questions/33069490/nlargest-and-nsmallest-heapq-python
    #
    # Runtime: 60 ms, faster than 86.34% of Python3 online submissions for Kth Largest Element in an Array.
    # Memory Usage: 15.3 MB, less than 17.28% of Python3 online submissions for Kth Largest Element in an Array.
    def solution_2(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k, nums)[-1]
