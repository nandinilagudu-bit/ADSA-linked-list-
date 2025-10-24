# 2.	Convert The Patient List to A Circular Linked List for a Round-Robin Check-Up System. Implement Insertion and Deletion.
class Node:
    def __init__(self, name, age, patient_id):
        self.name = name
        self.age = age
        self.patient_id = patient_id
        self.next = None  


class CircularPatientList:
    def __init__(self):
        self.head = None


    def insert_patient(self, name, age, patient_id):
        new_node = Node(name, age, patient_id)

        if self.head is None:
            self.head = new_node
            self.head.next = self.head  
            print(f"Patient {name} added as first patient.")
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head  
            print(f"Patient {name} added to the list.")


    def delete_patient(self, patient_id):
        if self.head is None:
            print("No patients to delete.")
            return

        current = self.head
        prev = None

  
        if current.next == self.head and current.patient_id == patient_id:
            self.head = None
            print(f"Patient with ID {patient_id} deleted.")
            return

        
        while True:
            if current.patient_id == patient_id:
                if prev is not None:
                    prev.next = current.next
                else:
                
                    temp = self.head
                    while temp.next != self.head:
                        temp = temp.next
                    temp.next = self.head.next
                    self.head = self.head.next
                print(f"Patient with ID {patient_id} deleted.")
                return
            prev = current
            current = current.next
            if current == self.head:
                break

        print(f"Patient with ID {patient_id} not found.")

    def display_patients(self):
        if self.head is None:
            print("No patients in the list.")
            return

        temp = self.head
        print("\nCurrent Patient Round-Robin List:")
        while True:
            print(f"Name: {temp.name}, Age: {temp.age}, ID: {temp.patient_id}")
            temp = temp.next
            if temp == self.head:
                break

if __name__ == "__main__":
    patients = CircularPatientList()
    patients.insert_patient("Jinnie", 30, 101)
    patients.insert_patient("Alekya", 25, 102)
    patients.insert_patient("Bobbie", 40, 103)

    patients.display_patients()
    

    patients.delete_patient(102)
    patients.display_patients()
