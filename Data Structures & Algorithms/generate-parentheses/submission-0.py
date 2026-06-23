class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        results = []
        cur_n = n
        open_parens = 0
        paren_stack = []

        def traverse(paren_stack, cur_n, open_parens):
            # Base case: cur_n = 0, open_parens = 0
            if cur_n == 0 and open_parens == 0 and len(paren_stack) > 0:
                results.append(''.join(paren_stack))
                return
            # Case 1: cur_n > 0
            # Expansion 1: add open parentheses then recurse, then backtrack
            if cur_n > 0:
                paren_stack.append('(')
                traverse(paren_stack, cur_n - 1, open_parens + 1)
                paren_stack.pop()
            # Expansion 2: add closed parentheses, recurse, and backtrack
            if open_parens > 0:
                paren_stack.append(')')
                traverse(paren_stack, cur_n, open_parens - 1)
                paren_stack.pop()
        
        traverse(paren_stack, cur_n, open_parens)
        return results