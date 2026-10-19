class ListNode:
    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next = next_node

class LinkedList:
    def __init__(self):
        # Dummy node banate hain empty list wale edge cases se bachne ke liye
        self.head = ListNode(-1)
        self.tail = self.head

    def get(self, index: int) -> int:
        curr = self.head.next
        i = 0
        
        # List mein aage badhte jayenge jab tak required index na mil jaye
        while curr:
            if i == index:
                return curr.val
            i += 1
            curr = curr.next
            
        # Agar index out of bounds hai
        return -1

    def insertHead(self, val: int) -> None:
        new_node = ListNode(val)
        new_node.next = self.head.next
        self.head.next = new_node
        
        # Agar list pehle empty thi, toh naya node hi head aur tail dono hoga
        if not new_node.next:
            self.tail = new_node

    def insertTail(self, val: int) -> None:
        # Tail pointer hone ki wajah se poori list traverse nahi karni padegi
        self.tail.next = ListNode(val)
        self.tail = self.tail.next

    def remove(self, index: int) -> bool:
        i = 0
        curr = self.head
        
        # Humein us node se ek qadam pehle (previous node) rukna hai
        while i < index and curr:
            i += 1
            curr = curr.next
            
        # Agar current node exist karta hai aur delete karne ke liye uske aage bhi node hai
        if curr and curr.next:
            # Agar delete hone wala node hi aakhri (tail) node tha, 
            # toh tail ko ek step peeche shift karenge.
            if curr.next == self.tail:
                self.tail = curr
                
            # Node ko delete karna (pointer bypass karenge)
            curr.next = curr.next.next
            return True
            
        return False

    def getValues(self) -> list[int]:
        curr = self.head.next
        res = []
        while curr:
            res.append(curr.val)
            curr = curr.next
        return res