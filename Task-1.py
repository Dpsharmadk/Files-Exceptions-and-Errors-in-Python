# Task 1: Read a File and Handle Errors

try:
    # Try to open the file in read mode
    with open("sample.txt", "r") as file:
        print("Reading file content:\n")
        
        # Read file line by line
        for line in file:
            print(line.strip())

except FileNotFoundError:
    # Handle error if file does not exist
    print("Error: The file 'sample.txt' does not exist.")

except Exception as e:
    # Handle any other unexpected errors
    print("An unexpected error occurred:", e)
    