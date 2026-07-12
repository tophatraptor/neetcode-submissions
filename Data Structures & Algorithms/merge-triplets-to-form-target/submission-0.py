class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        cur_triplet = None
        for i, x in enumerate(triplets):
            is_valid = True
            for j in range(3):
                if x[j] > target[j]:
                    is_valid = False
                    break
            if is_valid:
                if cur_triplet is None:
                    cur_triplet = x
                else:
                    cur_triplet = self.mergeTwoTriplets(cur_triplet, x)
        if cur_triplet is None:
            return False
        for j in range(3):
            if cur_triplet[j] != target[j]:
                return False
        return True

    def mergeTwoTriplets(self, a: List[int], b: List[int]) -> List[int]:
        return [max(a[i], b[i]) for i in range(len(a))]
        
"""
Thinking this through - I was actually wondering if ordering mattered, but I realized ordering doesn't actually matter. We can merge with any triplet, as long as all three
values of that triplet *do not* exceed the target.
"""