class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 建立一個 Dictionary，Key 是特徵，Value 是裝著字串的 List
        res_dict = {} 
        
        for s in strs:
            # 1. 找到特徵 (例如：排序後的字串)
            key = "".join(sorted(s))
            
            # 2. 根據特徵分類
            if key not in res_dict:
                res_dict[key] = []
            res_dict[key].append(s)
            
        # 3. 回傳所有的 Value 即可
        return list(res_dict.values())