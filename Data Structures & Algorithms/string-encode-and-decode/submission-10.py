class Solution:

    def encode(self, strs: List[str]) -> str:
        enc = ""
        for s in strs:
            enc = enc + str(len(s)) + "#" + s
        return enc

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1

            length = int(s[i:j])
            dec_s = s[j+1 : j+1+length]

            result.append(dec_s)
            i = j + 1 + length
        return  result

