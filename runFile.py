import os
import subprocess

def py_file(filename):
    # Get the current directory
    current_directory = os.path.dirname(os.path.abspath(__file__))
    
    # Construct the full path to the file
    file_path = os.path.join(current_directory, filename)
    
    # Check if the file exists
    if os.path.exists(file_path) and file_path.endswith(".py"):
        # Run the .py file using subprocess
        result = subprocess.run(["python", file_path], capture_output=True, text=True)
