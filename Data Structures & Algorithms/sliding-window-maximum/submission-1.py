from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque()
        res = []
        for i in range(len(nums)):
            if len(queue) == 0:
                queue.append((i, nums[i]))
            else:
                first_idx, first_val = queue.popleft()
                if first_idx > i - k:
                    queue.appendleft((first_idx, first_val))
                while len(queue) > 0:
                    last_idx, last_val = queue.pop()
                    if last_val > nums[i]:
                        queue.append((last_idx, last_val))
                        break
                queue.append((i, nums[i]))
            if i >= k-1:
                first_idx, first_val = queue.popleft()
                res.append(first_val)
                queue.appendleft((first_idx, first_val))
        return res


"""
Naive solution: iterate over the window each time, O(n * k), O(1) space

Optimized solution: We can use a heap, which will be O(n log n) in the worst case,
since we only perform lazy deletion if the maximum element falls outside of our window.

Mostest optimal solution: monotonic queue:
- Add first element
- Append to queue if the next element is less than, so we can be aware of what the next smallest element is
- If we encounter a bigger element: Nothing we've seen before in the queue matters, so pop all of the bigger elements
"""