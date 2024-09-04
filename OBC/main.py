import time
import discord
import colorama
from colorama import Fore
from discord.ext import commands
import sys
import urllib.request
import asyncio
import warnings
import requests
from database import version, versionHash

colorama.init(autoreset=True)

# FİLTER
warnings.filterwarnings("ignore")

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
bot = commands.Bot(command_prefix='!', intents=intents)

# VERSİON CONTROL
async def check_version():
    global update
    try:
        url = "https://raw.githubusercontent.com/berhatpasha/OBC/main/OBC/versionControl/version"
        response = requests.get(url)
        response.raise_for_status()
        content = response.text.strip()

        print(f"{Fore.CYAN}Last version: {content}")
        print(f"{Fore.CYAN}Used version: {versionHash}")
        if versionHash == content:
            print(f"{Fore.GREEN}OBC is up to date ✓")
            await asyncio.sleep(3)
        else:
            print(f"\n{Fore.YELLOW}Update available!")
            print(f"{Fore.YELLOW}Use: git clone https://github.com/berhatpasha/OBC.git")
            update = True
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")

async def initial_sleep():
    if update:
        print(f"{Fore.YELLOW}It will resume in 20 seconds.")
        await asyncio.sleep(20)
    else:
        await asyncio.sleep(5)

# BANNER
def print_banner():
    print("\n" * 50)
    time.sleep(1)
    print(f'''{Fore.LIGHTBLUE_EX}
       "$$$$bo.
         "$$$$$$$$booocS$$$    ..    ,.
     ".    "*$$$$SP{Fore.LIGHTRED_EX}*****{Fore.LIGHTBLUE_EX}V$o..o$$. .$$$b             ░█████╗░██████╗░░█████╗░
      "$$o. .$$$$$o{Fore.LIGHTRED_EX}*****{Fore.LIGHTBLUE_EX}A$$$$$$$$$$$$$$b            ██╔══██╗██╔══██╗██╔══██╗
""bo.   "*$$$$$$$$$$$$$$$$$$$$P*$$$$$$$$:           ██║░░██║██████╦╝██║░░╚═╝
    "$$.    V$$$$$$$$$$$P""**""*"'   VP  * "l          ██║░░██║██╔══██╗██║░░██╗
     "$$$o.4$$$$$$$$X                               ╚█████╔╝██████╦╝╚█████╔╝
     "*$$$$$$$$$$$$$$P""     {Fore.LIGHTRED_EX}""*oo,,     ,$P{Fore.LIGHTBLUE_EX}   {Fore.CYAN}o⃨p⃨e⃨n⃨ b⃨o⃨t⃨ c⃨o⃨n⃨s⃨o⃨l⃨e⃨ {Fore.LIGHTYELLOW_EX}{version}{Fore.LIGHTBLUE_EX}
           $$P""V$$$$$$$:    .        {Fore.LIGHTRED_EX}""*****"{Fore.LIGHTBLUE_EX}  {Fore.CYAN} Github :{Fore.LIGHTYELLOW_EX} https://bit.ly/4h2u{Fore.LIGHTBLUE_EX} 
          .*"    A$$$$$$$$o.4;      .
               .oP""   "$$$$$$b.  .$;
                         A$$$$$$$$$$P
                         "  "$$$$$P"
                             $$P*"
                            .$"
                            "
''')

async def emergency_mode():
    for guild in bot.guilds:
        print(f'Sending warning message to {guild.name} server')
        for channel in guild.text_channels:
            try:
                await channel.send('Attention! Bot manager launches emergency protocol!')
                print(f'{Fore.WHITE}{channel.name}{Fore.GREEN} ✓')
            except Exception as e:
                print(f'{Fore.WHITE}{channel.name}{Fore.RED} x{Fore.YELLOW} [{e}]')
        try:
            await guild.leave()
            print(f'Left server: {guild.name} {Fore.GREEN} ✓')
        except Exception as e:
            print(f'Failed to leave server: {guild.name} {Fore.RED} x [{e}]')
    try:
        await bot.close()
        print(f"{Fore.WHITE}Bot shutdown successfully{Fore.GREEN} ✓")
    except Exception as e:
        print(f"{Fore.WHITE}Failed to shutdown bot{Fore.RED} x [{e}]")
    sys.exit()

def get_public_ip():
    try:
        response = requests.get('https://api.ipify.org?format=json')
        ip_info = response.json()
        return ip_info['ip']
    except Exception:
        return "error"

def check_connection(url="http://www.google.com"):
    try:
        urllib.request.urlopen(url, timeout=5)
        return True
    except urllib.error.URLError:
        return False

def invisible_mode():
    print("")
    print(f"{Fore.CYAN}You've turned on invisible mode!")
    print(f"{Fore.GREEN}!send command lost ✓")
    print(f"{Fore.GREEN}!changeStatus command is lost ✓")
    print(f"{Fore.GREEN}Bot status invisible ✓")

async def read_user_input():
    print(f"{Fore.GREEN}Interaction complete! For help, try this: {Fore.CYAN}!help")
    while True:
        temp_input = await asyncio.get_event_loop().run_in_executor(None, input, f"{Fore.LIGHTGREEN_EX}")
        if temp_input == "!help":
            print(f"{Fore.CYAN}!send {Fore.LIGHTCYAN_EX}<channelId> {Fore.BLUE}<message>")
            print(f"{Fore.CYAN}!monitoringMode {Fore.LIGHTMAGENTA_EX}(does not take arguments)")
            print(f"{Fore.CYAN}!emergencyMode {Fore.LIGHTMAGENTA_EX}(does not take arguments)")
            print(f"{Fore.CYAN}!ban {Fore.LIGHTCYAN_EX}<userID>")
            print(f"{Fore.CYAN}!kick {Fore.LIGHTCYAN_EX}<userID>")
            print(f"{Fore.CYAN}!mute {Fore.LIGHTCYAN_EX}<userID> {Fore.BLUE}<duration (in minutes)>")
            print(f"{Fore.CYAN}!rootInfo {Fore.LIGHTMAGENTA_EX}(does not take arguments)")
            print(f"{Fore.CYAN}!clear {Fore.LIGHTCYAN_EX}<channelId> {Fore.BLUE}<count>")
            print(f"{Fore.CYAN}!changeStatus {Fore.LIGHTCYAN_EX}<type> {Fore.BLUE}<name>")  # type = game(discord.Game)
            print(f"{Fore.CYAN}!spam {Fore.LIGHTCYAN_EX}<channelId> {Fore.BLUE}<count> {Fore.LIGHTMAGENTA_EX}<message>")
            print(f"{Fore.CYAN}!invisibleMode {Fore.LIGHTMAGENTA_EX}(does not take arguments)")
            print(f"{Fore.CYAN}!role {Fore.LIGHTCYAN_EX}<+/-> {Fore.BLUE}<role ID> {Fore.LIGHTMAGENTA_EX}<user ID>")
        elif temp_input.startswith("!send"):
            try:
                channel_id = int(temp_input.split()[1])
                channel = bot.get_channel(channel_id)
                if channel:
                    await channel.send(f"{' '.join(temp_input.split()[2:])}")
                    print(f"{Fore.LIGHTGREEN_EX}Your message has been sent ✓")
                else:
                    print(f"{Fore.LIGHTYELLOW_EX}Channel with ID {channel_id} not found")
                    print(f"{Fore.LIGHTRED_EX}Send operation failed x")
            except Exception as e:
                print(f"{Fore.LIGHTRED_EX}Error: {e}")
        elif temp_input == "!monitoringMode":
            print(f"{Fore.CYAN}Monitoring mode enabled")
            while True:
                if not check_connection():
                    print(f"{Fore.RED}No internet connection. Reconnecting...")
                    await asyncio.sleep(5)
                await asyncio.sleep(1)
        elif temp_input == "!emergencyMode":
            print(f"{Fore.RED}Emergency mode activated")
            await emergency_mode()
        elif temp_input.startswith("!ban"):
            try:
                user_id = int(temp_input.split()[1])
                for guild in bot.guilds:
                    user = guild.get_member(user_id)
                    if user:
                        await user.ban(reason="Banned by bot command")
                        print(f"{Fore.LIGHTGREEN_EX}User {user_id} has been banned ✓")
                    else:
                        print(f"{Fore.LIGHTYELLOW_EX}User with ID {user_id} not found in guild")
            except Exception as e:
                print(f"{Fore.LIGHTRED_EX}Error: {e}")
        elif temp_input.startswith("!kick"):
            try:
                user_id = int(temp_input.split()[1])
                for guild in bot.guilds:
                    user = guild.get_member(user_id)
                    if user:
                        await user.kick(reason="Kicked by bot command")
                        print(f"{Fore.LIGHTGREEN_EX}User {user_id} has been kicked ✓")
                    else:
                        print(f"{Fore.LIGHTYELLOW_EX}User with ID {user_id} not found in guild")
            except Exception as e:
                print(f"{Fore.LIGHTRED_EX}Error: {e}")
        elif temp_input.startswith("!mute"):
            try:
                user_id = int(temp_input.split()[1])
                duration = int(temp_input.split()[2])
                for guild in bot.guilds:
                    user = guild.get_member(user_id)
                    if user:
                        role = discord.utils.get(guild.roles, name="Muted")
                        if not role:
                            role = await guild.create_role(name="Muted")
                        await user.add_roles(role)
                        print(f"{Fore.LIGHTGREEN_EX}User {user_id} has been muted for {duration} minutes ✓")
                        await asyncio.sleep(duration * 60)
                        await user.remove_roles(role)
                        print(f"{Fore.LIGHTGREEN_EX}User {user_id} has been unmuted ✓")
                    else:
                        print(f"{Fore.LIGHTYELLOW_EX}User with ID {user_id} not found in guild")
            except Exception as e:
                print(f"{Fore.LIGHTRED_EX}Error: {e}")
        elif temp_input == "!rootInfo":
            ip = get_public_ip()
            print(f"{Fore.CYAN}Public IP Address: {ip}")
        elif temp_input.startswith("!clear"):
            try:
                channel_id = int(temp_input.split()[1])
                count = int(temp_input.split()[2])
                channel = bot.get_channel(channel_id)
                if channel:
                    async for message in channel.history(limit=count):
                        await message.delete()
                    print(f"{Fore.LIGHTGREEN_EX}Deleted {count} messages from channel {channel_id} ✓")
                else:
                    print(f"{Fore.LIGHTYELLOW_EX}Channel with ID {channel_id} not found")
            except Exception as e:
                print(f"{Fore.LIGHTRED_EX}Error: {e}")
        elif temp_input.startswith("!changeStatus"):
            try:
                status_type = temp_input.split()[1]
                status_name = ' '.join(temp_input.split()[2:])
                if status_type.lower() == "playing":
                    await bot.change_presence(activity=discord.Game(name=status_name))
                elif status_type.lower() == "streaming":
                    await bot.change_presence(activity=discord.Streaming(name=status_name))
                elif status_type.lower() == "listening":
                    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=status_name))
                elif status_type.lower() == "watching":
                    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=status_name))
                else:
                    print(f"{Fore.LIGHTYELLOW_EX}Invalid status type")
                print(f"{Fore.LIGHTGREEN_EX}Status changed to {status_type} {status_name} ✓")
            except Exception as e:
                print(f"{Fore.LIGHTRED_EX}Error: {e}")
        elif temp_input.startswith("!spam"):
            try:
                channel_id = int(temp_input.split()[1])
                count = int(temp_input.split()[2])
                message = ' '.join(temp_input.split()[3:])
                channel = bot.get_channel(channel_id)
                if channel:
                    for _ in range(count):
                        await channel.send(message)
                    print(f"{Fore.LIGHTGREEN_EX}Sent {count} messages to channel {channel_id} ✓")
                else:
                    print(f"{Fore.LIGHTYELLOW_EX}Channel with ID {channel_id} not found")
            except Exception as e:
                print(f"{Fore.LIGHTRED_EX}Error: {e}")
        elif temp_input == "!invisibleMode":
            invisible_mode()
        elif temp_input.startswith("!role"):
            try:
                action = temp_input.split()[1]
                role_id = int(temp_input.split()[2])
                user_id = int(temp_input.split()[3])
                role = discord.utils.get(bot.guilds[0].roles, id=role_id)
                user = bot.get_user(user_id)
                if role and user:
                    if action == "+":
                        await user.add_roles(role)
                        print(f"{Fore.LIGHTGREEN_EX}Role {role_id} added to user {user_id} ✓")
                    elif action == "-":
                        await user.remove_roles(role)
                        print(f"{Fore.LIGHTGREEN_EX}Role {role_id} removed from user {user_id} ✓")
                    else:
                        print(f"{Fore.LIGHTYELLOW_EX}Invalid action. Use '+' or '-'")
                else:
                    print(f"{Fore.LIGHTYELLOW_EX}Role or user not found")
            except Exception as e:
                print(f"{Fore.LIGHTRED_EX}Error: {e}")

# BOT TOKEN
if __name__ == '__main__':
    try:
        bot_token = input(f"{Fore.LIGHTCYAN_EX}Enter your bot token: ")
        print_banner()
        loop = asyncio.get_event_loop()
        loop.create_task(check_version())
        loop.create_task(initial_sleep())
        bot.run(bot_token)
    except KeyboardInterrupt:
        print(f"\n{Fore.RED}Bot stopped by user")
        sys.exit()
