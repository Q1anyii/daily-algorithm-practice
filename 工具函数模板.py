# -*- coding: utf-8 -*-
"""
模板
------------------------------------------------------------
"区间和 / 查询"→ 前缀和；
"区间整体加减"→ 差分；
"坐标巨大"→ 离散化；
"最大连续子数组 / 最优增量"→ Kadane；
"最大值最小"→ 二分答案；
"连通 / 合并集合"→ DSU；
"合并重叠区间"→ merge_intervals；
"最长 / 最短满足条件"→ 滑动窗口；
"下一个更大 / 更小"→ 单调栈。
【0. 固定开场三行 —— 每题都写】
"""
import sys

input = sys.stdin.readline          # 比内置 input() 快 5~10 倍，大数据必用
sys.setrecursionlimit(10 ** 7)      # 递归题必加，否则深递归直接 RE


def solve():
    pass


if __name__ == '__main__':
    solve()


# ============================================================
# 1. 快读：一次性读完所有 token（10万+ 数据时最稳）
# ============================================================
def read_all_ints():
    return list(map(int, sys.stdin.read().split()))


def read_lines():
    return sys.stdin.read().splitlines()


# ============================================================
# 2. 前缀和（一维）
# pre[i] = a[0]+...+a[i-1]；区间和 [l, r] = pre[r+1] - pre[l]
# ============================================================
def prefix_sum(a):
    pre = []
    for x in a:
        pre.append(pre[-1] + x)
    return pre


# ============================================================
# 3. 差分（区间整体加/减，O(1) 修改）—— 去哪儿两次考到
# 对 [l, r] 都加 v：diff[l] += v; diff[r+1] -= v （下标从0开始）
# ============================================================
def diff_add(n, ops):
    """ops = [(l, r, v), ...] 闭区间，0-indexed"""
    d = [0] * (n + 2)
    for l, r, v in ops:
        d[l] += v
        d[r + 1] -= v
    res = []
    cur = 0
    for i in range(n):
        cur += d[i]
        res.append(cur)
    return res


# ============================================================
# 4. 离散化 + 二分（坐标很大但数量不多时必用）
# 返回：排序去重后的坐标数组 xs，以及把原坐标映射到下标的函数
# ============================================================
from bisect import bisect_left


def discretize(coords):
    xs = sorted(set(coords))
    return xs, lambda x: bisect_left(xs, x)


# ============================================================
# 5. Kadane：最大连续子数组和（笔试真题核心解法）
# ============================================================
def max_subarray_sum(a):
    best = cur = a[0]
    for x in a[1:]:
        cur = max(x, cur + x)
        best = max(best, cur)
    return best


def min_subarray_sum(a):
    best = cur = a[0]
    for x in a[1:]:
        cur = min(x, cur + x)
        best = min(best, cur)
    return best


# ============================================================
# 6. 双指针 / 滑动窗口（最长/最短满足条件的连续段）
# ============================================================
def longest_window(a, check):
    """check(cur_state) -> bool，返回满足条件的最长窗口长度"""
    from collections import defaultdict
    cnt = defaultdict(int)
    l, ans = 0, 0
    for r, x in enumerate(a):
        cnt[x] += 1
        while not check(cnt):
            cnt[a[l]] -= 1
            l += 1
        ans = max(ans, r - l + 1)
    return ans


# ============================================================
# 7. 单调栈（下一个更大/更小元素，直方图最大矩形）
# ============================================================
def next_smaller(a):
    n = len(a)
    st, res = [], [-1] * n
    for i in range(n):
        while st and a[st[-1]] > a[i]:
            res[st.pop()] = i
        st.append(i)
    return res


# ============================================================
# 8. 二分答案（"最大值最小" / "最小值最大" 类）
# ============================================================
def binary_search_answer(lo, hi, feasible):
    """hi 可行，lo 不可行，返回最小的可行值"""
    while lo < hi:
        mid = (lo + hi) // 2
        if feasible(mid):
            hi = mid
        else:
            lo = mid + 1
    return lo


# ============================================================
# 9. 并查集（连通性、区间合并）
# ============================================================
class DSU:
    def __init__(self, n):
        self.p = list(range(n))

    def find(self, x):
        while self.p[x] != x:
            self.p[x] = self.p[self.p[x]]
            x = self.p[x]
        return x

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra != rb:
            self.p[ra] = rb


# ============================================================
# 10. 区间合并（排序后线性扫）
# ============================================================
def merge_intervals(intervals):
    intervals.sort()
    res = []
    for l, r in intervals:
        if res and l <= res[-1][1]:
            res[-1][1] = max(res[-1][1], r)
        else:
            res.append([l, r])
    return res



# ==========================================================================
#                        临 场 注 意 事 项
# ==========================================================================
# 1. 赛码网 Python：用 input()/sys.stdin.readline 都行，但【不要】用
#    readline() 这种赛码专有函数（那是它家 C/JS 模板里的）。
# 2. 输出统一用 print 或 sys.stdout.write，注意多组用例每组一行。
# 3. 不要写 package、不要写 class Main（那是 Java 的要求），Python 直接脚本。
# 4. 遇到超时：先换 sys.stdin.read() 一次读完；再检查有没有 O(n^2) 以上的循环。
# 5. 除法用 //，浮点误差题优先转整数运算（比如金额用分、汇率乘10000取整）。
# 6. 递归题一定要 sys.setrecursionlimit，否则直接 RE 而不是 TLE。
