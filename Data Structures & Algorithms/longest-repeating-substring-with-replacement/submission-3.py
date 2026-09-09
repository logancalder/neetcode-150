class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq_map = defaultdict(int)
        most_seen, maxf, longest = None, 0, 0

        l = r = 0

        while r < len(s):
            letter = s[r]
            freq_map[letter] += 1

            if freq_map[letter] > maxf:
                maxf = freq_map[letter]
                most_seen = letter

            window = r - l + 1

            while most_seen and window - maxf > k:
                freq_map[s[l]] -= 1
                l += 1
                window = r - l + 1

            longest = max(window, longest)

            r += 1
        
        return longest