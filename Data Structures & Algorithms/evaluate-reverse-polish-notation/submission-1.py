class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands = ["+", "-", "*", "/"]
        stack = []
        for token in tokens:
            if token in operands:
                # pop twice
                if len(stack) < 2:
                    return None
                v2 = stack.pop()
                v1 = stack.pop()
                if token == "+":
                    new_val = v1 + v2
                elif token == "-":
                    new_val = v1 - v2
                elif token == "*":
                    new_val = v1 * v2
                elif token == "/":
                    is_negative = False
                    if v1 < 0 or v2 < 0:
                        is_negative = True
                        v1 *= -1
                    new_val = v1 // v2
                    if is_negative:
                        new_val = -new_val
                stack.append(new_val)
            else:
                new_val = int(token)
                stack.append(new_val)
        return stack[-1]
