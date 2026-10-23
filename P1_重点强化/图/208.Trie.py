"""
题目：208. 实现 Trie (前缀树) (Trie)
难度：中等
分类：图
"""

from typing import List, Optional, Dict, Tuple

# ==================== 题目描述 ====================
"""
Trie（发音类似 "try"）或者说前缀树是一种树形数据结构，用于高效地存储和检索字符串数据集中的键。
请你实现 Trie 类：
- Trie() 初始化前缀树对象。
- void insert(String word) 向前缀树中插入字符串 word。
- boolean search(String word) 如果字符串 word 在前缀树中，返回 true；否则，返回 false。
- boolean startsWith(String prefix) 如果之前已经插入的字符串 word 的前缀之一为 prefix，返回 true；否则，返回 false。

示例 1：
输入：["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
输出：[null, null, true, false, true, null, true]
"""

# ==================== 解题思路 ====================
"""
根不存字符，路径即前缀，is_end 区分词与前缀。

**Trie 的正确模型：一棵 "路径即词" 的树**

- 每个**节点**存：一个字符的子节点字典 + 一个 "是否是某个词结尾" 的标记；
- **根节点不存字符**，是空起点；
- 从根到某节点的一条路径 = 一个前缀；到 `is_end=True` 的节点 = 一个完整词。

举个例子：依次插入 `"apple"` 和 `"app"`，树长这样（共享 `a-p-p` 前缀，这是 Trie 的精髓）：

```
root
 └─ a
    └─ p
       └─ p      ← 这里的 is_end = True（"app" 是完整词）
          └─ l
             └─ e  ← is_end = True（"apple" 是完整词）
```

**为什么 `is_end` 标记必须有？** 因为 `search("app")` 在只插过 `"apple"` 时要返回 **False**——"app" 只是前缀，不是完整词；而 `startsWith("app")` 返回 **True**。两者遍历方式几乎一样，**唯一区别就是最后一步**：search 检查 `is_end`，startsWith 不检查。
"""

# ==================== 代码实现 ====================
class TrieNode:
    def __init__(self):
        self.children = {}  # 字符 → 子节点
        self.is_end = False  # 是否是某词的结尾

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:   # 没有就建节点
                node.children[ch] = TrieNode()
            node = node.children[ch]      # 往下走
        node.is_end = True                # 走到词尾，打标记

    def search(self, word: str) -> bool:
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.is_end

    def startsWith(self, word: str) -> bool:
        node = self.root
        for ch in word:
            if ch in node.children:
                node = node.children[ch]
            else:
                return False
        return True

# ==================== 测试用例 ====================
def test_solution():
    trie = Trie()
    trie.insert("apple")
    assert trie.search("apple") is True
    assert trie.search("app") is False
    assert trie.startsWith("app") is True
    trie.insert("app")
    assert trie.search("app") is True
    assert trie.search("ap") is False
    assert trie.startsWith("ap") is True
    print('All test cases passed!')


if __name__ == "__main__":
    test_solution()
