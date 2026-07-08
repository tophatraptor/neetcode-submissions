class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        self.combinationSumRec([], candidates, 0, target, res)
        return res

    def combinationSumRec(self, cur_candidates: List[int], candidates, i, target, res):
        if target < 0:
            return
        if target == 0:
            res.append(cur_candidates[:])
            return
        if i >= len(candidates):
            return
        for j in range(i, len(candidates)):
            if j > i and candidates[j] == candidates[j-1]:
                continue
            cur_candidates.append(candidates[j])
            self.combinationSumRec(cur_candidates, candidates, j + 1, target - candidates[j], res)
            cur_candidates.pop()