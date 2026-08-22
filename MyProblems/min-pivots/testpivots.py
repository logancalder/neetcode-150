"""
Test bench for Solution.minPivots(s1, s2).

Drop this file in the same folder as your solution.py (which should define
`class Solution` with a `minPivots(self, s1, s2) -> int` method), then run:

    python test_min_pivots.py

It checks your solution against a brute-force O(n^2) reference on 50 cases:
hand-picked edge cases + randomly generated ones (including duplicate letters).
"""

import random
import string
from collections import defaultdict, deque

# --- import your solution ---
# Adjust this import to match your actual file/class name.
from solution import Solution


def build_perm(s1, s2):
    """perm[i] = index in s1 of the i-th character of s2 (leftmost-first for dupes)."""
    char_indices = defaultdict(deque)
    for i, ch in enumerate(s1):
        char_indices[ch].append(i)

    perm = []
    for ch in s2:
        perm.append(char_indices[ch].popleft())
    return perm


def brute_force_inversions(s1, s2) -> int:
    """O(n^2) reference: build perm, count inversions by brute force pairwise check."""
    perm = build_perm(s1, s2)
    n = len(perm)
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            if perm[i] > perm[j]:
                count += 1
    return count


def random_anagram_pair(n, alphabet_size):
    """Generate s1 (random string) and s2 (a random permutation of s1's chars)."""
    alphabet = string.ascii_lowercase[:max(1, alphabet_size)]
    s1 = ''.join(random.choice(alphabet) for _ in range(n))
    chars = list(s1)
    random.shuffle(chars)
    s2 = ''.join(chars)
    return s1, s2


def build_test_cases():
    cases = []

    # --- hand-picked edge cases ---
    cases.append(("", ""))                          # empty strings
    cases.append(("a", "a"))                         # single char
    cases.append(("ab", "ab"))                       # already equal, len 2
    cases.append(("ab", "ba"))                       # 1 swap needed
    cases.append(("abc", "abc"))                     # already sorted/equal
    cases.append(("abc", "cba"))                     # fully reversed
    # from the original discussion (unrestricted-swap answer 3)
    cases.append(("abcdefg", "acdbegf"))
    # two independent 2-cycles
    cases.append(("abcdefg", "acbedfg"))
    cases.append(("abcdefg", "aecdbfg"))              # single displaced jump
    cases.append(("aab", "aba"))                      # duplicate letters
    # duplicate letters, more shuffled
    cases.append(("aab", "baa"))
    cases.append(("aaaa", "aaaa"))                    # all identical chars
    # duplicates, reversed blocks
    cases.append(("aabbcc", "ccbbaa"))
    cases.append(("aabbcc", "abcabc"))                # duplicates, interleaved
    cases.append(("xyz", "zyx"))                      # 3 distinct, reversed
    cases.append(("mississippi", "mississippi"))       # long word, equal
    # placeholder, fixed below
    cases.append(("mississippi", "ppissississim"[:len("mississippi")]))

    # fix the mississippi shuffled case properly (must be an anagram)
    base = "mississippi"
    chars = list(base)
    random.seed(42)
    random.shuffle(chars)
    cases[-1] = (base, ''.join(chars))

    # --- randomly generated cases ---
    random.seed(1234)  # reproducible
    remaining = 50 - len(cases)
    for _ in range(remaining):
        n = random.randint(1, 30)
        alphabet_size = random.choice(
            [1, 2, 3, 5, 8, 15])  # varies duplicate density
        s1, s2 = random_anagram_pair(n, alphabet_size)
        cases.append((s1, s2))

    return cases[:50]


def run_tests():
    sol = Solution()
    cases = build_test_cases()

    passed = 0
    failed = []

    for idx, (s1, s2) in enumerate(cases, 1):
        expected = brute_force_inversions(s1, s2)
        try:
            actual = sol.minPivots(s1, s2)
        except Exception as e:
            failed.append((idx, s1, s2, expected, f"EXCEPTION: {e}"))
            continue

        if actual == expected:
            passed += 1
        else:
            failed.append((idx, s1, s2, expected, actual))

    print(f"\n{passed}/{len(cases)} test cases passed.\n")

    if failed:
        print("Failures:")
        for idx, s1, s2, expected, actual in failed:
            s1_disp = s1 if len(s1) <= 40 else s1[:37] + "..."
            s2_disp = s2 if len(s2) <= 40 else s2[:37] + "..."
            print(
                f"  #{idx}: s1={s1_disp!r} s2={s2_disp!r} expected={expected} got={actual}")
    else:
        print("All test cases passed!")


if __name__ == "__main__":
    run_tests()
