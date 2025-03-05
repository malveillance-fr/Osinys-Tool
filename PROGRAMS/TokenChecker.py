import customtkinter as ctk
import requests

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

class TokenCheckerApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Osinys - Token Checker")
        self.geometry("700x600")
        self.configure(bg="black")

        self.token_entry = ctk.CTkEntry(self, placeholder_text="Enter Discord Token", width=500)
        self.token_entry.pack(pady=10)

        self.user_info_var = ctk.BooleanVar()
        self.friends_list_var = ctk.BooleanVar()
        self.server_join_var = ctk.BooleanVar()
        self.external_connection_var = ctk.BooleanVar()
        
        self.checkboxes = [
            ("User Info", self.user_info_var),
            ("Friends List", self.friends_list_var),
            ("Server Join", self.server_join_var),
            ("External Connection", self.external_connection_var)
        ]

        for text, var in self.checkboxes:
            ctk.CTkCheckBox(self, text=text, variable=var, fg_color="red", text_color="white").pack(anchor="w", padx=20)

        self.check_button = ctk.CTkButton(self, text="Check", command=self.display_info, fg_color="red")
        self.check_button.pack(pady=10)

        self.info_frame = ctk.CTkFrame(self, width=600, height=300, fg_color="gray", border_width=2, border_color="red")
        self.info_frame.pack(pady=10)

        self.info_textbox = ctk.CTkTextbox(self.info_frame, width=580, height=280, fg_color="gray", text_color="white")
        self.info_textbox.pack()

        

    def display_info(self):
        token = self.token_entry.get()
        headers = {"Authorization": token, "Content-Type": "application/json"}
        
        selected_info = []
        
        if self.user_info_var.get():
            response = requests.get("https://discord.com/api/v9/users/@me", headers=headers)
            if response.status_code == 200:
                data = response.json()
                selected_info.append("[$] Username: {}#{}".format(data.get('username'), data.get('discriminator')))
                selected_info.append("[$] Nitro: {}".format("Yes" if data.get('premium_type') else "No"))
                selected_info.append("[$] Email: {}".format(data.get('email', 'Not Available')))
                selected_info.append("[$] Phone: {}".format(data.get('phone', 'Not Available')))
                selected_info.append("[$] Displayname: {}".format(data.get('global_name', 'Not Set')))
                selected_info.append("[$] Token: {}".format(token))
                selected_info.append("[$] ID: {}".format(data.get('id')))
                selected_info.append("[$] Badges: {}".format(data.get('flags')))
            else:
                selected_info.append("[$] Invalid Token")
        
        if self.friends_list_var.get():
            response = requests.get("https://discord.com/api/v9/users/@me/relationships", headers=headers)
            if response.status_code == 200:
                friends = response.json()
                selected_info.append("[$] Friends List:")
                for friend in friends:
                    selected_info.append(f"  - {friend['user']['username']}#{friend['user']['discriminator']} (ID: {friend['id']})")
            else:
                selected_info.append("[$] Unable to fetch Friends List")
        
        if self.server_join_var.get():
            response = requests.get("https://discord.com/api/v9/users/@me/guilds", headers=headers)
            if response.status_code == 200:
                guilds = response.json()
                selected_info.append("[$] Servers Joined:")
                for guild in guilds:
                    owner_tag = " [OWNER]" if guild.get('owner') else ""
                    selected_info.append(f"  - {guild['name']}{owner_tag}")
            else:
                selected_info.append("[$] Unable to fetch Server List")
        
        if self.external_connection_var.get():
            response = requests.get("https://discord.com/api/v9/users/@me/connections", headers=headers)
            if response.status_code == 200:
                connections = response.json()
                selected_info.append("[$] External Connections:")
                for conn in connections:
                    selected_info.append(f"  - {conn['name']}")
            else:
                selected_info.append("[$] Unable to fetch External Connections")
        
        self.info_textbox.delete("1.0", "end")
        self.info_textbox.insert("end", "\n".join(selected_info))



if __name__ == "__main__":
    app = TokenCheckerApp()
    app.mainloop()
