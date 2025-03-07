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
from PIL import Image, ImageTk
import pyperclip

def copy_to_clipboard():
    pyperclip.copy("bc1q2634fmjpasyknfymhuje2a5cqh34cr84hvk6wz")
    status_label.configure(text="Copied successfully!", text_color="green")

root = ctk.CTk()
root.title("Osinys - Donate Center")
root.geometry("500x300")
root.configure(bg='dark')

title_label = ctk.CTkLabel(root, text="Welcome to Donate Center!", font=("Arial", 18), text_color="white")
title_label.pack(pady=20)

frame = ctk.CTkFrame(root, width=400, height=60, corner_radius=10, fg_color='white')
frame.pack(pady=10)

btc_label = ctk.CTkLabel(frame, text="bc1q2634fmjpasyknfymhuje2a5cqh34cr84hvk6wz", font=("Arial", 12), text_color='black', fg_color='white')
btc_label.pack(side="left", padx=10)

btc_image = Image.open("bitcoin.png")
btc_image = btc_image.resize((30, 30))  
btc_logo = ctk.CTkImage(dark_image=btc_image, size=(30, 30))

btc_logo_label = ctk.CTkLabel(frame, image=btc_logo, fg_color='white')
btc_logo_label.pack(side="right", padx=10)

copy_button = ctk.CTkButton(root, text="Copy", command=copy_to_clipboard)
copy_button.pack(pady=20)

status_label = ctk.CTkLabel(root, text="", font=("Arial", 12), text_color="green")
status_label.pack(pady=5)

root.mainloop()
