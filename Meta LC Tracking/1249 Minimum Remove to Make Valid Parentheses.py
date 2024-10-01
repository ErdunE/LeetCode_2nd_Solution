class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        left = 0
        right = s.count(')')
        res = ''

        for c in s:
            if c == "(":
                if right > 0:
                    res += c
                    left += 1
                    right -= 1
            elif c == ")":
                if left > 0:
                    res += c
                    left -= 1
                else:
                    right -= 1
            else:
                res += c

        return res
