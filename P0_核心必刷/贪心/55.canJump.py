"""
题目：55. 跳跃游戏 (canJump)
难度：中等
分类：贪心
"""

from typing import List, Optional, Dict, Tuple

# ==================== 题目描述 ====================
"""
给你一个非负整数数组 nums，你最初位于数组的第一个下标。数组中的每个元素代表你在该位置可以跳跃的最大长度。
判断你是否能够到达最后一个下标。

示例 1：
输入：nums = [2,3,1,1,4]
输出：true
解释：可以先跳 1 步，从下标 0 到达下标 1, 然后再从下标 1 跳 3 步到达最后一个下标。

示例 2：
输入：nums = [3,2,1,0,4]
输出：false
"""


# ==================== 解题思路 ====================
"""
假设最远步数为0，获取nums.length表示目标位置
判断最远步数是否大于等于当前位置，如果是，则更新最远步数
当前位置+当前位置值>nums.length，即表示可到达目标位置
"""

# ==================== 代码实现 ====================
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        k = 0
        for i in range(len(nums)):
            if i > k: return False # k无法到达i目标位置，那么返回false
            k = max(k, i + nums[i]) #当前位置+当前位置步数
        return True


# ==================== 测试用例 ====================
def test_solution():
    sol = Solution()
    assert sol.canJump([2, 3, 1, 1, 4]) is True
    assert sol.canJump([3, 2, 1, 0, 4]) is False
    assert sol.canJump([0]) is True
    assert sol.canJump([2, 0, 0]) is True
    assert sol.canJump([1, 0, 2]) is False
    print('All test cases passed!')


if __name__ == "__main__":
    test_solution()
