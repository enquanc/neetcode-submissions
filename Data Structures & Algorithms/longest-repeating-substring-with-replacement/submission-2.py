class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        max_len = 0
        char = {}
        max_f = 0
        for right in range(len(s)):
            if s[right] not in char:
                char[s[right]] = 1
            else:
                char[s[right]] += 1

            max_f = max(max_f, char[s[right]])

            while (right - left + 1) - max_f > k:
                char[s[left]] -= 1
                left += 1
                max_f = max(max_f, char[s[right]])
            
            if (right - left + 1) > max_len:
                max_len = right - left + 1

        return max_len
        
            
                    
