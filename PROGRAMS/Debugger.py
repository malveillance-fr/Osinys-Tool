# ============================================
# LICENCE D'UTILISATION
# ============================================
# Ce code est protégé par des droits d'auteur et est destiné à un usage personnel uniquement. 
# Vous n'êtes pas autorisé à le modifier, le distribuer, le vendre, ou à en faire des copies à des fins commerciales sans l'autorisation explicite de l'auteur.
# Toute tentative de modification, de revente, ou de redistribution du code sans permission constitue une violation de cette licence et pourra entraîner des poursuites judiciaires.
# 
# Propriétaire du code : Malveillance
# Version : 3.2
# Copyright © 2025
# ============================================



# ============================================
# USAGE LICENSE
# ============================================
# This code is copyrighted and intended for personal use only. 
# You are not allowed to modify, distribute, sell, or make copies of it for commercial purposes without explicit permission from the author.
# Any attempt to modify, resell, or redistribute the code without permission constitutes a breach of this license and may result in legal action.
# 
# Code Owner: Malveillance
# Version: 3.2
# Copyright © 2025
# ============================================






#Ce code est a but éducatif, tout usage malveillant ne sera en aucun cas de la faute de l'auteur
#This code is for educational purposes, any malicious use will in no way be the fault of the author.




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
