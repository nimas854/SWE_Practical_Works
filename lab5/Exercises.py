class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        print(" -> ".join(map(str, elements)))

    def insert(self, data, position):
        new_node = Node(data)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        for _ in range(position - 1):
            if current is None:
                raise IndexError("Position out of range")
            current = current.next
        new_node.next = current.next
        current.next = new_node

    def delete(self, data):
        if not self.head:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

    def search(self, data):
        current = self.head
        position = 0
        while current:
            if current.data == data:
                return position
            current = current.next
            position += 1
        return -1

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev


    def find_middle(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.data if slow else None


    def has_cycle(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False


    def remove_duplicates(self):
        if not self.head:
            return
        current = self.head
        seen = set([current.data])
        while current.next:
            if current.next.data in seen:
                current.next = current.next.next
            else:
                seen.add(current.next.data)
                current = current.next

    @staticmethod
    def merge_sorted(list1, list2):
        dummy = Node(0)
        tail = dummy
        a, b = list1.head, list2.head

        while a and b:
            if a.data < b.data:
                tail.next = a
                a = a.next
            else:
                tail.next = b
                b = b.next
            tail = tail.next

        tail.next = a if a else b
        merged_list = LinkedList()
        merged_list.head = dummy.next
        return merged_list


ll1 = LinkedList()
ll1.append(1)
ll1.append(2)
ll1.append(3)
ll1.append(4)
ll1.append(5)


print("Middle element:", ll1.find_middle())


print("Has cycle:", ll1.has_cycle())

ll2 = LinkedList()
ll2.append(1)
ll2.append(2)
ll2.append(2)
ll2.append(3)
ll2.append(3)
ll2.append(4)
ll2.remove_duplicates()
print("After removing duplicates:")
ll2.display()


ll3 = LinkedList()
ll3.append(1)
ll3.append(3)
ll3.append(5)

ll4 = LinkedList()
ll4.append(2)
ll4.append(4)
ll4.append(6)

merged_ll = LinkedList.merge_sorted(ll3, ll4)
print("Merged sorted linked list:")
merged_ll.display()
