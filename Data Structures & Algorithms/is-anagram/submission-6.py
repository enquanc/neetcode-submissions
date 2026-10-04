class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        def find(strings):
            dict_s = {}

            for str_s in strings:
                if str_s in dict_s:
                    dict_s[str_s] += 1
                else:
                    dict_s[str_s] = 1
            return dict_s

        dict_1 = find(s)
        dict_2 = find(t)
        if dict_1 == dict_2:
            return True
        return False