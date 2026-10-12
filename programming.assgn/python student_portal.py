# ==========================================
# Domain: Education (Student Learning Portal)
# DPG Standards: Open-source, Privacy-respecting, Modular
# ==========================================

class Student:
    # Class attribute shared across all instances (DPG institutional context)
    institution = "Digital Public Learning Portal - Open Access"

    def __init__(self, student_id, name, program):
        self.student_id = student_id  # Unique identifier
        self.name = name              # Public name
        self.program = program        # Enrolled program
        self.grades = []              # List data structure for academic results

    # Task 3: Instance Method to display info
    def display_info(self):
        print(f"----------------------------------------")
        print(f"Student ID : {self.student_id}")
        print(f"Name       : {self.name}")
        print(f"Program    : {self.program}")
        print(f"Grades     : {self.grades if self.grades else 'No grades recorded'}")
        print(f"----------------------------------------")

    # Task 3: Instance Method to update student record
    def update_record(self, new_program=None, new_grade=None):
        if new_program:
            self.program = new_program
        if new_grade is not None:
            self.grades.append(new_grade)
        print(f"[Success] Record updated for student ID: {self.student_id}")

    # Task 3: Class Method (@classmethod)
    @classmethod
    def get_portal_info(cls):
        return f"Portal System: {cls.institution} | Designed under DPG Standards"


# Task 2: Python Data Structure (Dictionary storing objects with unique ID as key)
student_database = {}

# Task 2: Function to add records
def add_student_record(student_id, name, program):
    if student_id in student_database:
        print(f"[Error] Student ID {student_id} already exists.")
    else:
        new_student = Student(student_id, name, program)
        student_database[student_id] = new_student
        print(f"[Success] Added student: {name}")

# Task 2: Function to display records from the dictionary
def display_all_records():
    if not student_database:
        print("No records found in the portal.")
        return
    
    print("\n=== All Student Portal Records ===")
    print(Student.get_portal_info())
    for s_id, student_obj in student_database.items():
        student_obj.display_info()


# ==========================================
# Sample Execution / Interaction Testing
# ==========================================
if __name__ == "__main__":
    # 1. Adding students (Task 2)
    add_student_record("S101", "Aminata Conteh", "Information Technology")
    add_student_record("S102", "Mohamed Sesay", "Software Engineering")

    # 2. Displaying all initial records (Task 2 & 3)
    display_all_records()

    # 3. Interacting with objects & updating records (Task 1 & 3)
    print("\n-- Performing Record Update --")
    student_database["S101"].update_record(new_program="Cybersecurity", new_grade=88)
    student_database["S102"].update_record(new_grade=92)

    # 4. Displaying updated records
    display_all_records()