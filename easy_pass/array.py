from typing import List, Tuple, Any

class Solution:
    # 去重（保持顺序）
    def dedup(self, nums: List[int]) -> List[int]:
        seen, res = set(), []
        for num in nums:
            if num not in seen:
                seen.add(num)
                res.append(num)
        return res

    # 最大/次大值（一次遍历）
    def max_two(self, nums: List[int]) -> tuple[float | int | Any, float | int | Any]:
        m1 = m2 = float("-inf")
        for n in nums:
            if n > m1:
                m1, m2 = m2, n
            elif n > m2:
                m2 = n
        return m1, m2

    # 两数之和
    def two_sum(self, nums: List[int], target: int):
        dict_ = {}
        for i, x in enumerate(nums):
            diff = target - x
            if diff in dict_:
                return [dict_[diff], i]
            dict_[x] = i
        return []

    # 合并数组
    def merge(self, nums1, m, nums2, n):
        i, j, k = m - 1, n - 1, m + n - 1
        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
        return nums1

if __name__ == "__main__":
    sol = Solution()
    print(sol.dedup([1,2,3,3,4,2,4,1,2]))
    print(sol.max_two([1,2,4,5,2,4,6]))
    print(sol.two_sum([1, 2, 4, 5, 2, 4, 6], 7))
    print(sol.merge(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3))