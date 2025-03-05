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
