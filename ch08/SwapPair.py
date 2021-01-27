class ListNode:
    def __init__(self, data=0, next=None):
        self.val = data
        self.next = None

    def _print_all(self):
        while self:
            print(self.val, end=' ')
            self = self.next

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        root = prev = ListNode(None)
        print("head: ", head)
        prev.next = head
        while head and head.next:
            print("head in while: ", head)
            # b가 a(head)를 가리키도록 할당
            b = head.next
            head.next = b.next
            b.next = head
            
            #prev가 b를 가리키도록 할당
            prev.next = b
            
            #다음번 비교를 위해 이동
            head = head.next
            prev = prev.next.next# next가 None이면? next.next접근에 에러는 없는가?
            
        return root.next
            
        # python에서 꼭 필요한 작업인가? 가독성을 위한 행동인가?

test = Solution()
head = LinkedList()
head.append(1)
head.append(2)
head.append(3)
head.append(4)
#ListNode{val: 1, next: ListNode{val: 2, next: ListNode{val: 3, next: ListNode{val: 4, next: None}}}}

print("head: ", head.)
#test.swapPairs(head)