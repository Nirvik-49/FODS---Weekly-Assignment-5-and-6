import csv

def add_student_record():

    # Take input from user
    
    name = input("Enter student name: ").strip()
    student_id = input("Enter student ID: ").strip()
    course = input("Enter course: ").strip()
    level = input("Enter level (Undergraduate/Graduate): ").strip()
    section = input("Enter section: ").strip().upper()

    # Prepare the new record
    new_record = {
        'name': name,
        'id': student_id,
        'course': course,
        'level': level,
        'section': section
    }

    # Append to the CSV file
    try:
        with open('students.csv', mode='a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['name', 'id', 'course', 'level', 'section'])
            
            # Check if file is empty to write header
            if file.tell() == 0:
                writer.writeheader()
            
            writer.writerow(new_record)
        print("Student record added successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")

# Run the function
add_student_record()

