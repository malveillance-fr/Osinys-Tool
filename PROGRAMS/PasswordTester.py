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








import customtkinter as ctk
import time

def calculate_crack_time():
    password = entry_password.get()
    brute_force_rate = int(entry_rate.get())
    
    length = len(password)
    if length < 5:
        force = "low"
    elif length < 10:
        force = "medium"
    else:
        force = "hard"
    
    total_attempts = 95 ** length
    seconds_to_crack = total_attempts / brute_force_rate
    
    if seconds_to_crack > 31536000:
        time_to_crack = f"{seconds_to_crack // 31536000} years"
    elif seconds_to_crack > 86400:
        time_to_crack = f"{seconds_to_crack // 86400} days"
    elif seconds_to_crack > 3600:
        time_to_crack = f"{seconds_to_crack // 3600} hours"
    elif seconds_to_crack > 60:
        time_to_crack = f"{seconds_to_crack // 60} minutes"
    else:
        time_to_crack = f"{seconds_to_crack} seconds"
    
    result = f"[+] Password Force: {force}\n[+] Time to crack: {time_to_crack}"
    result_text.delete(1.0, "end")  
    result_text.insert("end", result)  

root = ctk.CTk()

root.title("Osinys - Password Tester")
root.geometry("400x400")

frame = ctk.CTkFrame(root, corner_radius=15)
frame.pack(pady=30, padx=40, fill="both", expand=True)

label_rate = ctk.CTkLabel(frame, text="Brute Force Rate (attempts/sec):", text_color="white")
label_rate.pack(pady=10)
entry_rate = ctk.CTkEntry(frame)
entry_rate.pack(pady=5)

label_password = ctk.CTkLabel(frame, text="Password:", text_color="white")
label_password.pack(pady=10)
entry_password = ctk.CTkEntry(frame, show="*")
entry_password.pack(pady=5)

calculate_button = ctk.CTkButton(frame, text="Calculate", command=calculate_crack_time)
calculate_button.pack(pady=15)

result_text = ctk.CTkTextbox(root, height=4, width=40, corner_radius=10, state="normal", bg_color="gray")
result_text.pack(pady=15, padx=40, fill="both", expand=True)

root.mainloop()
