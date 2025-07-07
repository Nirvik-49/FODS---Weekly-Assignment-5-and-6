import datetime
import os

def perform_calculations(numbers):
    """Perform addition, subtraction, multiplication, and division on a list of numbers"""
    
    if not numbers:
        return None, None, None, None
    
    # Calculation logic
    
    addition = sum(numbers)
    
    subtraction = numbers[0]
    for num in numbers[1:]:
        subtraction -= num
        
    multiplication = 1
    for num in numbers:
        multiplication *= num
        
    try:
        division = numbers[0]
        for num in numbers[1:]:
            division /= num
    except ZeroDivisionError:
        division = "Undefined (division by zero)"
        
    return addition, subtraction, multiplication, division

def write_to_file(results, filename="calculations_log.txt"):
    """Write results to file with timestamp"""
    
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    with open(filename, "a") as file:
        file.write(f"\n\n=== Calculation at {timestamp} ===\n")
        file.write(f"Numbers: {results['numbers']}\n")
        file.write(f"Addition: {results['addition']}\n")
        file.write(f"Subtraction: {results['subtraction']}\n")
        file.write(f"Multiplication: {results['multiplication']}\n")
        file.write(f"Division: {results['division']}\n")

def display_file_contents(filename="calculations_log.txt"):
    """Display file contents in a formatted way"""
    
    if not os.path.exists(filename):
        print("No calculations have been performed yet.")
        return
        
    print("\n=== Calculation History ===")
    with open(filename, "r") as file:
        print(file.read())

def main():
    print("Number Operations Calculator")
    print("Enter numbers separated by spaces")
    print("Enter 'q' to quit and view results\n")
    
    while True:
        try:
            user_input = input("Enter numbers: ")
            if user_input.lower() == 'q':
                break
                
            numbers = [float(num) for num in user_input.split()]
            
            addition, subtraction, multiplication, division = perform_calculations(numbers)
            
            if None in (addition, subtraction, multiplication, division):
                print("Error: Please enter at least one number")
                continue
                
            results = {
                "numbers": numbers,
                "addition": addition,
                "subtraction": subtraction,
                "multiplication": multiplication,
                "division": division
            }
            
            write_to_file(results)
            print("Calculations saved successfully!")
            
        except ValueError:
            print("Error: Please enter valid numbers separated by spaces")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
    
    display_file_contents()

if __name__ == "__main__":
    main()
