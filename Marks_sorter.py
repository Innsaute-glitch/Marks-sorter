# Import time module for UX
import time

# Set up the variables needed
number = None # Define the number of students variable globally
marks = [] # Empty list for marks
continue1 = "New" # First loop
old_length = 0
interrupt = 0 # 0 means no Keyboard Interrupt here

while continue1 != "Stop" and interrupt == 0:
    number = None # Reset number
    while (type(number) is not int or number < 1) and interrupt == 0:
        try: # Error Handling for the cases + different statements for each use
            if continue1 == "New":
                number = int(input("How many students are there? ")) # First time
            else:
                number = int(input("How many more students should be added? "))
            if number >= 1: # 0 and (-)ve number of students should give error
                break
            else:
                print("This is not a valid number, please try again")
        except ValueError:
            print("Please input a valid number of students")
        except KeyboardInterrupt: # Handle keyboard Interrupt 1
            print("Alright mate- Stopping the script")
            interrupt = 1
            break
    if interrupt == 0:
        while (len(marks) - old_length) < number : # Use the loop only for new values
            try: # Error handling for marks
                marks.append(round(float(input("Please enter the marks: ")), 1)) # Using float for 1 point decimal
            except ValueError:
                print("Please input a valid number...:")
            except KeyboardInterrupt: # Handle keyboard Interrupt 2
                print("\nAlright mate- Stopping the script")
                interrupt = 1
                break
            time.sleep(0.1)
    else:
        break
    print("Max number of students reached") # Inform of limit
    continue1 = input("Add more? (y/N): ") # Ask for continuation
    if continue1.lower() == "n": # Feed the loop + more conditions
        continue1 = "Stop"
    else:
        continue1 = "Loop"
        old_length = int(len(marks)) # Set the old_length variable as current length

# Final results.. (The simple part)
if interrupt == 0:
    time.sleep(0.1)
    print(f"\nYour final list is: {marks}\n")
    print("Sorting in ascending order...")
    time.sleep(0.5)
    marks = sorted(marks)
    print(marks)
    print(f"Maximum marks are: {marks[-1]}")
    print(f"Minimum marks are: {marks[0]}")
    print("\nThank You for using this script :)\n")
else: # If Keyboard Interrupt detected
    time.sleep(0.1)
    print("And it's done! Thanks for using this script")
    print()
# Day 4 project end- To Do: Upload on GitHub later