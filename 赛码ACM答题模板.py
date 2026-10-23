# -*- coding: utf-8 -*-
"""
赛码网 / acmcoder ACM 模式答题模板
============================================
提交版：直接复制本文件内容到赛码编辑器即可（自包含，无外部依赖）。
调试版：配合同目录「赛码本地测试器.py」使用——测试器 import 本文件的 solve()，
       喂多组输入用例本地断言验证，全 PASS 后再粘贴提交。

提交前自查清单（写完逐条核对）：
1. 分支完整性：每个 if 有没有 else / 兜底？循环跑完不 break 会怎样？
2. 空输入 / 空集合：min([]) / max([]) / data[0] / len==0 会崩吗？
3. 消耗品 / 重复值：dict 去重丢信息吗？用过的元素要标记吗？
4. 边界：0、负数、最大值；>= 还是 ==；1-based 还是 0-based？
5. 复杂度：10^5 数据 O(n^2) 会超时吗？要不要排序 / 二分 / 前缀和？
"""

import sys, bisect
def solve(data):
    """data: sys.stdin.read().split() 切好的全部 token（字符串列表）"""
    # ---------- 解析（按题意改，常见三种读法） ----------
    # n = int(data[0])                          # 只有一个参数
    # n, m = map(int, data[:2])                 # 两个参数
    # arr = list(map(int, data[2:2 + n]))       # 后面跟 n 个数
    # n, m = map(int, data[:2])
    # arr = list(map(int, data[2:2 + n]))

    # ---------- 核心逻辑（TODO: 在这里写算法） ----------



if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    print(solve(data))
