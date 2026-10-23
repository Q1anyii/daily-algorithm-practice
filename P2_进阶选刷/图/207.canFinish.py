"""
题目：207. 课程表 (canFinish)
难度：中等
分类：图
"""

from typing import List, Optional, Dict, Tuple

# ==================== 题目描述 ====================
"""
你这个学期必须选修 numCourses 门课程，记为 0 到 numCourses - 1。
在选修某些课程之前需要一些先修课程。先修课程按数组 prerequisites 给出，其中 prerequisites[i] = [ai, bi]，表示如果要学习课程 ai 则必须先学习课程 bi。
请你判断是否可能完成所有课程的学习？

示例 1：
输入：numCourses = 2, prerequisites = [[1,0]]
输出：true
解释：总共有 2 门课程。学习课程 1 之前，你需要完成课程 0。这是可能的。
"""


# ==================== 解题思路 ====================
# TODO: 在此填写解题思路
"""
"""

# ==================== 代码实现 ====================
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # TODO: 实现该方法
        pass


# ==================== 测试用例 ====================
def test_solution():
    sol = Solution()
    assert sol.canFinish(2, [[1, 0]]) is True
    assert sol.canFinish(2, [[1, 0], [0, 1]]) is False
    assert sol.canFinish(3, [[1, 0], [2, 1]]) is True
    assert sol.canFinish(1, []) is True
    assert sol.canFinish(4, [[1, 0], [2, 0], [3, 1], [3, 2]]) is True
    print('All test cases passed!')


if __name__ == "__main__":
    test_solution()
