from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        groups = defaultdict(list)
        for s in strs:
            key = ''.join(sorted(s))        # 方向 A 或 B，結果必須 hashable
            groups[key].append(s)
        return list(groups.values())           # dict 的哪個方法可以取出所有 value？
