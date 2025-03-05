import os
import subprocess

def check_and_repair_file(filepath):
    if filepath.endswith('.py'):
        try:
            subprocess.check_call(['python', '-m', 'py_compile', filepath])
            print(f"The file {filepath} is valid.")
        except subprocess.CalledProcessError as e:
            print(f"Error with {filepath}: Syntax issue found.")
            with open(filepath, 'w') as file:
                file.write("")
            print(f"The file {filepath} has been repaired (reset).")
    else:
        print(f"File {filepath} is not a Python file and is not supported for repair.")

def repair_directory(directory_path):
    if not os.path.exists(directory_path):
        print("The specified folder does not exist.")
        return
    
    for filename in os.listdir(directory_path):
        filepath = os.path.join(directory_path, filename)
        if os.path.isfile(filepath):
            check_and_repair_file(filepath)

if __name__ == "__main__":
    directory = "PROGRAMS" 
    repair_directory(directory)
