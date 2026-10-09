from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        matching = {")": "(", "}": "{", "]": "["}
        for i in s:
            if i == "(" or i == "{" or i == "[":
                stack.append(i)
            elif i == ")" or i == "}" or i == ']':
                if not stack or stack.pop() != matching[i]:
                    return False
        return len(stack) == 0