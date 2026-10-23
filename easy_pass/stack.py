class Solution:
    # 括号匹配
    def is_valid(self, s):
        stack = []
        pairs = {')': '(', ']': '[', '}': '{'}
        for c in s:
            if c in pairs:
                if not stack or stack[-1] != pairs[c]:
                    return False
                stack.pop()
            else:
                stack.append(c)
        return not stack

if __name__ == "__main__":
    sol = Solution()
    print(sol.is_valid("()(()}"))
    print(sol.is_valid("()()[]{}"))
    print(sol.is_valid("{()[]}"))
