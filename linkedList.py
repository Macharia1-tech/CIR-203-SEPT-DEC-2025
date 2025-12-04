
class Node:
    def __init__(self, name, admission_no, grades):
        self.data = {
            "name": name,
            "admission_no": admission_no,
            "grades": grades    
        }
        self.next = None



class StudentLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, name, admission_no, grades):
        new_node = Node(name, admission_no, grades)

        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node


    def display(self):
        current = self.head
        if current is None:
            print("The list is empty.")
            return

        while current:
            print("Name:", current.data["name"])
            print("Admission No:", current.data["admission_no"])
            print("Grades:", current.data["grades"])
            print("-----")
            current = current.next


students = StudentLinkedList()

students.insert("Mike Smith", "CIM/0035/024", [80, 74, 96])
students.insert("Mercy Atieno", "CIT/0973/024", [68, 90, 82])
students.insert("Julius Peters", "CIS/2472/024", [78, 86, 88])

print("All Students:")
students.display()

