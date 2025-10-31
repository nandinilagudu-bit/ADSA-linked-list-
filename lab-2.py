# Convert The Patient List to A Circular Linked List for a Round-Robin Check-Up System. Implement Insertion and Deletion.
class Node:
    def __init__(self, name):
        self.name = name
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None  

    
    def insert(self, name):
        new_node = Node(name)

        if self.head is None:
            
            self.head = new_node
            new_node.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head
        print(f"Inserted: {name}")


    def delete(self, name):
        if self.head is None:
            print("List is empty!")
            return

        curr = self.head
        prev = None
        if curr.name == name:
            
            if curr.next == self.head:
                self.head = None
                print(f"Deleted: {name}")
                return

            
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = curr.next
            self.head = curr.next
            print(f"Deleted: {name}")
            return

        
        while curr.next != self.head:
            prev = curr
            curr = curr.next
            if curr.name == name:
                prev.next = curr.next
                print(f"Deleted: {name}")
                return

        print("Patient not found!")


    def display(self):
        if self.head is None:
            print("No patients in the list.")
            return

        temp = self.head
        print("\nCurrent Patient List (Circular):")
        while True:
            print(temp.name, end=" -> ")
            temp = temp.next
            if temp == self.head:
                break
        print(f"(back to {self.head.name})")


patient_list = CircularLinkedList()

patient_list.insert("Ram")
patient_list.insert("Sita")
patient_list.insert("Ramesh")
patient_list.display()

patient_list.delete("ram")
patient_list.display()

patient_list.insert("ganesh")
patient_list.display()