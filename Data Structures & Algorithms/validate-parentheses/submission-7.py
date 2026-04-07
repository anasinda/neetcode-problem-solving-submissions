class Solution:
    def isValid(self, s: str) -> bool:
        brackets_duct = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        seen_brackets_open = []
        size_open = 0
        for bracket in s:
            if bracket not in brackets_duct.keys():
                seen_brackets_open.append(bracket)
                size_open += 1
            elif size_open > 0 and seen_brackets_open[-1] == brackets_duct[bracket]:
                    del seen_brackets_open[-1]
                    size_open -= 1
            else:
                return False
        if size_open == 0:
            return True
        return False