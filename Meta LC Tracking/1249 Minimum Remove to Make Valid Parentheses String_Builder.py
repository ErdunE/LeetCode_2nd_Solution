class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        def helper(s:str,left_p:str,right_p:str) -> str:
            string_builder = []
            banlance = 0

            for c in s:
                if c == left_p:
                    banlance += 1
                elif c == right_p:
                    if banlance == 0:
                        continue
                    banlance -= 1
                string_builder.append(c)

            return ''.join(string_builder)


        first_pass = helper(s, '(', ')')

        second_pass = helper(first_pass[::-1] , ')', '(')

        return second_pass[::-1]