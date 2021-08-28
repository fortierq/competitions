#  https://leetcode.com/problems/peeking-iterator/

# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.it = iterator
        self.it_next = None

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if not self.it_next:
            self.it_next = self.it.next()
        return self.it_next
        
        
    def next(self):
        """
        :rtype: int
        """
        res = self.it_next
        if not res:
            res = self.it.next()
        self.it_next = None
        return res
    
    
    def hasNext(self):
        """
        :rtype: bool
        """
        return (self.it_next is not None) or self.it.hasNext()
            

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].