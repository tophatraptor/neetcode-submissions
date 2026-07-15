class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        values = []
        operators = ["+", "-", "*", "/"]
        for x in tokens:
            if x in operators:
                v2 = values.pop()
                v1 = values.pop()
                if x == '+':
                    values.append(v1 + v2)
                elif x == '-':
                    values.append(v1 - v2)
                elif x == '*':
                    values.append(v1 * v2)
                elif x == '/':
                    # We need to do floor division
                    if (v1 < 0 or v2 < 0) and not (v1 < 0 and v2 < 0):
                        sign = -1
                    else:
                        sign = 1
                    values.append(int(v1 / v2))
            else:
                x = int(x)
                values.append(x)
        return values[0]
                    