```
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prv = None
        cur = head
        nxt = cur.next if cur != None else None
        while cur != None:
            cur.next = prv
            prv = cur
            cur = nxt
            nxt = cur.next if cur != None else None
        return prv

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                return True
        return False
```
