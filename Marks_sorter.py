# Import time module for UX
import time

# Set up the variables needed
marks = [] # Empty list for marks

def get_typed_input(prompt, to_convert_type):
    while True:
        try:
            return to_convert_type(input(prompt))
        except ValueError:
            print("\t⚠️ This is not a valid input. Please try again!")
            continue

def marks_type_check():
    while True:
        marks_type = get_typed_input("Are the marks containing decimal points? (Y/N): ", str)
        if marks_type.lower() == "y":
            return float
        elif marks_type.lower() == "n":
            return int
        else:
            print("Please input either Y or N")

def main():
    attempts = 0
    while True:
        number = get_typed_input("How many students are there? ", int)
        if number <= 0:
            print("⚠️ Please input a number greater than 0. Your current input is:", number)
        else:
            break
    marks_definition = marks_type_check()
    while attempts < number:
        marks.append(get_typed_input("Please enter the marks: ", marks_definition))
        attempts += 1
    print("Max number of students reached")

def final_sorting():
    print(f"\nYour final list is: {marks}\n")
    print("Sorting in ascending order...")
    time.sleep(0.1)
    marks.sort()
    print(marks)
    print(f"Maximum marks are: {marks[-1]}")
    print(f"Minimum marks are: {marks[0]}")
    print("\nThank You for using this script :)\n")
    time.sleep(0.1)
    print("And it's done! Thanks for using this script")
    print()

running = True
while running:
    try:
        main()
        while True:
            try_again = input("Do you want to add more? (y/n): ")
            if try_again.lower() == "y":
                running = True
                break
            elif try_again.lower() == "n":
                print("Getting the final data sorted...")
                final_sorting()
                running = False
                break
            else:
                print("⚠️ Please input either 'y' or 'n'...")
    except KeyboardInterrupt:
        print()
        print("⚠️ KeyboardInterrupt Detected.. Exiting the script successfully...")
        break
    except EOFError:
        print()
        print("⚠️ EOF Error Detected.. Exiting the script successfully...")
        break
