from collections import defaultdict, deque

"""

Problem written and solved by Logan J Calder on August 8, 2026.

Problem Description:

You are given two strings s1 and s2 of the same length, where s2 is an anagram
of s1 (i.e., s2 can be formed by rearranging the characters of s1).

A pivot is an operation where you swap two adjacent characters in s2.

Return the minimum number of pivots required to transform s2 into s1.

-----------------------

Example 1:

Input: s1 = "abcdefg", s2 = "acdbegf"
Output: 3

Example 2:

Input: s1 = "abcdefg", s2 = "acbedfg"
Output: 2

Example 3:
Input: s1 = "aab", s2= "aab"
Output: 0

-----------------------

Constraints:
1 <= s1.length == s2.length <= 10^5
s1 and s2 consist of lowercase English letters
s2 is guaranteed to be an anagram of s1

"""


class Solution:
    def minPivots(self, s1, s2) -> int:

        def build_perm(arr1, arr2):
            imap = defaultdict(deque)
            for i, char in enumerate(arr1):
                imap[char].append(i)

            perm = []
            for char in arr2:
                perm.append(imap[char].popleft())
            return perm

        def merge(arr1, arr2):
            l = r = 0
            result = []
            inversions = 0
            while l < len(arr1) and r < len(arr2):
                if arr1[l] < arr2[r]:
                    result.append(arr1[l])
                    l += 1
                else:
                    result.append(arr2[r])
                    inversions += len(arr1[l:])
                    r += 1

            result += arr1[l:]
            result += arr2[r:]

            return (result, inversions)

        def mergeSort(arr):
            if len(arr) <= 1:
                return arr, 0
            m = len(arr) // 2
            left, invl = mergeSort(arr[:m])
            right, invr = mergeSort(arr[m:])
            merged, invm = merge(left, right)
            return (merged, invl + invr + invm)

        perm = build_perm(s1, s2)

        return mergeSort(perm)[1]
