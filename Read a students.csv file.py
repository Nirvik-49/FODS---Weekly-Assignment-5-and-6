import csv

def read_students_file(filename):
    try:
        with open(filename, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                name = row['name']
                student_id = row['id']
                course = row['course']
                level = row['level']
                section = row['section']
                print(f"Name: {name}, ID: {student_id}, Course: {course}, Level: {level}, Section: {section}")
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Specify the CSV file name
csv_file = 'students.csv'

# Call the function to read and print the student data
read_students_file(csv_file)


