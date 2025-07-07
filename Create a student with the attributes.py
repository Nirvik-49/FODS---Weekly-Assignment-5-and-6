class Student:
    def __init__(self, id, name, address, admission_year, level, section):
        """Initialize a Student object with provided attributes"""
        self.id = id
        self.name = name
        self.address = address
        self.admission_year = admission_year
        self.level = level
        self.section = section
    
    def display_info(self):
        """Display all student information in a formatted way"""
        print("\nStudent Information:")
        print(f"ID: {self.id}")
        print(f"Name: {self.name}")
        print(f"Address: {self.address}")
        print(f"Admission Year: {self.admission_year}")
        print(f"Level: {self.level}")
        print(f"Section: {self.section}")

def create_student():
    """Create and return a Student object with user input"""
    
    print("Enter Student Details:")
    id = input("ID: ")
    name = input("Name: ")
    address = input("Address: ")
    admission_year = input("Admission Year: ")
    level = input("Level (e.g., Undergraduate/Graduate): ")
    section = input("Section: ")
    
    return Student(id, name, address, admission_year, level, section)

# Main program

if __name__ == "__main__":
    
    # Create a student object with user input
    student = create_student()
    
    # Display the student information
    student.display_info()
