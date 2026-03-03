# Task 2: Write and Append Data to a File

# Take user input
user_input = input("Enter some data to write into the file: ")

# Write data to file (overwrites if file exists)
with open("output.txt", "w") as file:
    file.write("User entered: " + user_input + "\n")

print("Data written successfully.")

# Append additional data
additional_data = input("Enter additional data to append: ")

with open("output.txt", "a") as file:
    file.write("Appended data: " + additional_data + "\n")

print("Data appended successfully.\n")

# Read and display final content
print("Final content of the file:\n")

with open("output.txt", "r") as file:
    content = file.read()
    print(content)