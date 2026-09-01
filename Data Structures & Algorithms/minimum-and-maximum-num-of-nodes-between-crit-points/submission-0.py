# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        prev, head = head, head.next
        i, indexes = 0, []

        while head.next:
            if prev.val < head.val and head.val > head.next.val:
                indexes.append(i)
            elif prev.val > head.val and head.val < head.next.val:
                indexes.append(i)

            prev = head
            head = head.next

            i += 1

        if len(indexes) <= 1:
            return [-1, -1]

        minimum = indexes[1] - indexes[0]

        for i in range(len(indexes) - 1):
            minimum = min(minimum, indexes[i + 1] - indexes[i])

        return [minimum, indexes[-1] - indexes[0]]
