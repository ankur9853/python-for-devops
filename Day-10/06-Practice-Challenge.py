#Level 3 — Challenge (1 hour)
#Task 5 — File Reader with Exception Handling:

#Read a text file containing server names (one per line)
#Store them in a list
#Handle: FileNotFoundError, PermissionError, empty file
#Where is file located: C:\Users\prakabh\Python for devops\python-for-devops-1\Day-10\server_names.txt
# Why to use os module: The os module provides a way to interact with the operating system, allowing you to construct file paths in a way that is compatible across different platforms (Windows, macOS, Linux). By using os.path.join and os.path.dirname, you can ensure that your code will work regardless of where it is run, making it more portable and robust.
# Why 2 functions used here? : Using functions helps to organize the code, making it more modular and easier to read. 
# The read_server_names function is responsible for reading the file and handling exceptions, 
# while the main function serves as the entry point of the program, 
# managing the overall flow and calling the necessary functions. 
# This separation of concerns enhances code maintainability and readability.


import os

def read_server_names(file_path):
    try:
        with open(file_path, 'r') as file:
            # Read lines, strip whitespace, and ignore comments/empty lines
            server_names = [line.strip() for line in file if line.strip() and not line.strip().startswith('#')]
            
            if not server_names: # this will check if the list is empty. If it is, it will raise a ValueError.
                raise ValueError("The file is empty or contains no valid server names.")
            return server_names
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except PermissionError:
        print(f"Error: You do not have permission to read the file '{file_path}'.")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    return None

def main():
    # Dynamically find the file path relative to this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(script_dir, "server_names.txt")
    
    print(f"Starting file reader task for: {path}")
    servers = read_server_names(path)
    
    if servers:
        print("Server list stored successfully:", servers)
    else:
        print("No servers were loaded.")

if __name__ == "__main__":
    main()