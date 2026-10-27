"""
题目：45. 跳跃游戏 II (jump)
难度：中等
分类：贪心
"""

from typing import List, Optional, Dict, Tuple

# ==================== 题目描述 ====================
"""
给定一个长度为 n 的 0 索引整数数组 nums。初始位置为 nums[0]。
每个元素 nums[i] 表示从索引 i 向前跳转的最大长度。换句话说，如果你在 nums[i]，你可以跳转到任意 nums[i + j] 处。
返回到达 nums[n - 1] 的最小跳跃次数。

示例 1：
输入: nums = [2,3,1,1,4]
输出: 2
解释: 跳到最后一个位置的最小跳跃数是 2。从下标为 0 跳到下标为 1，跳 1 步，然后跳 3 步到达数组的最后一个位置。
"""


# ==================== 解题思路 ====================
"""
和canJump题型类似，不过这次是算次数而非能否跳到最后
"""

# ==================== 代码实现 ====================
class Solution:
    def jump(self, nums: List[int]) -> int:
        p = len(nums) - 1
        step = 0

        while p > 0:
            for i in range(p):
                # 从后往前找，先找到能跳到p的位置，然后再把p换成那个位置，再继续往前找
                if i + nums[i] >= p:
                    p = i
                    step += 1
                    break

        return step

# ==================== 测试用例 ====================
def test_solution():
    sol = Solution()
    assert sol.jump([2, 3, 1, 1, 4]) == 2
    assert sol.jump([2, 3, 0, 1, 4]) == 2
    assert sol.jump([0]) == 0
    assert sol.jump([1]) == 0
    assert sol.jump([1, 2]) == 1
    assert sol.jump([2, 1]) == 1
    print('All test cases passed!')


if __name__ == "__main__":
    test_solution()
