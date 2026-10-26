"""
题目：146. LRU 缓存 (LRUCache)
难度：中等
分类：设计
"""
from collections import OrderedDict
from typing import List, Optional, Dict, Tuple

# ==================== 题目描述 ====================
"""
请你设计并实现一个满足 LRU (最近最少使用) 缓存约束的数据结构。
实现 LRUCache 类：
- LRUCache(int capacity) 以正整数作为容量 capacity 初始化 LRU 缓存
- int get(int key) 如果关键字 key 存在于缓存中，则返回关键字的值，否则返回 -1。
- void put(int key, int value) 如果关键字 key 已经存在，则变更其数据值 value；如果不存在，则向缓存中插入该组 key-value。如果插入操作导致关键字数量超过 capacity，则应该逐出最久未使用的关键字。
函数 get 和 put 必须以 O(1) 的平均时间复杂度运行。

示例 1：
输入：["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
输出：[null, null, null, 1, null, -1, null, -1, 3, 4]
"""


# ==================== 解题思路 ====================
# TODO: 在此填写解题思路
"""
"""

# ==================== 代码实现 ====================
from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if self.cache.get(key):
            self.cache.move_to_end(key)
            return self.cache.get(key)
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.pop(key)
        elif len(self.cache) == self.capacity:
            self.cache.popitem(last=False)
        self.cache[key] = value


# ==================== 测试用例 ====================
def test_solution():
    lru = LRUCache(2)
    lru.put(1, 1)
    lru.put(2, 2)
    assert lru.get(1) == 1
    lru.put(3, 3)
    assert lru.get(2) == -1
    lru.put(4, 4)
    assert lru.get(1) == -1
    assert lru.get(3) == 3
    assert lru.get(4) == 4
    # 容量1
    lru2 = LRUCache(1)
    lru2.put(1, 1)
    assert lru2.get(1) == 1
    lru2.put(2, 2)
    assert lru2.get(1) == -1
    assert lru2.get(2) == 2
    print('All test cases passed!')


if __name__ == "__main__":
    test_solution()
