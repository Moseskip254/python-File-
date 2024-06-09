try:
    # File Creation
    with open("my_file.txt", 'w') as file:
        file.write("This is line 1\n")
        file.write("12345\n")
        file.write("Another line with some text and numbers 789\n")
    print("File 'my_file.txt' created successfully.")

    # File Reading and Display
    with open("my_file.txt", 'r') as file:
        print("Contents of 'my_file.txt':")
        for line in file:
            print(line.strip())

    # File Appending
    with open("my_file.txt", 'a') as file:
        file.write("Additional line 1\n")
        file.write("Another line appended\n")
        file.write("123456789\n")
    print("Data appended to 'my_file.txt'.")

except FileNotFoundError:
    print("Error: The file 'my_file.txt' was not found.")
except PermissionError:
    print("Error: Permission denied to access 'my_file.txt'.")
except Exception as e:
    print("An error occurred:", e)

finally:
    print("Script execution complete.")
