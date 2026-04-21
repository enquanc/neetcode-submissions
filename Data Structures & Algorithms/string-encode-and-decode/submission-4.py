class Solution:

    def encode(self, strs: List[str]) -> str:
        enc = ""
        for s in strs:
            enc = enc + s
            enc = enc + "一"
        enc = enc + "end"
        return enc

    def decode(self, s: str) -> List[str]:
        str_list = s.split("一")[:-1]
        return str_list

