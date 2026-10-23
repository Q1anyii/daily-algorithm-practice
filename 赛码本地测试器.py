# -*- coding: utf-8 -*-
"""
赛码网本地测试器
============================================
用法：
1. 先在「赛码ACM答题模板.py」里把 solve() 写完；
2. 把题目的示例输入 / 自己造的边界用例填进 CASES（(输入文本, 期望输出)）；
3. 运行本文件，逐条断言，PASS/FAIL 一目了然；
4. 全 PASS 后，把模板内容粘贴到赛码编辑器提交。

务必额外造边界用例：最小输入（1 个元素）、空输入、最大数、装不下/达不到 等情况。
"""

import 赛码ACM答题模板 as sol


# 用例格式：(stdin 文本, 期望 stdout 文本)
# 示例用 360 第一题占位——替换成你明天遇到的题
CASES = [
    # 示例用例（示例输入 / 期望输出）
    ("3 4\n5 2 7\n3 6 8 4\n", "17\n"),
    # 边界用例：装不下 → -1
    ("1 1\n5\n3\n", "-1\n"),
    # 边界用例：最小输入（只有 1 个元素时下标/循环别崩）
    ("1 0\n1\n\n", "0\n"),
]


def main():
    all_pass = True
    for i, (inp, expected) in enumerate(CASES, 1):
        got = sol.solve(inp.split())
        exp = expected.strip()
        ok = (got.strip() == exp)
        all_pass &= ok
        mark = "PASS" if ok else "FAIL"
        print(f"[{mark}] 用例 {i}: 期望={exp!r}  实际={got!r}")
    print("-" * 40)
    print("全部通过，可以提交" if all_pass else "存在失败用例，检查 solve()")


if __name__ == "__main__":
    main()
