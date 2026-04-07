class Solution:
    def isValid(self, s: str) -> bool:
        brackets_duct = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
        opening_brackets = ["(", "[", "{"]
        seen_brackets_open = []
        for bracket in s:
            if bracket in opening_brackets:
                seen_brackets_open.append(bracket)
            elif len(seen_brackets_open) > 0:
                if brackets_duct[bracket] == seen_brackets_open[-1]:
                    del seen_brackets_open[-1]
                else:
                    return False
            else:
                return False
        if len(seen_brackets_open) == 0:
            return True
        return False