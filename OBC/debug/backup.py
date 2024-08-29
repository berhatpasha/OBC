import time
import os
import discord
import colorama
from colorama import Fore
from discord.ext import commands
import sys
import urllib.request
import requests
import asyncio
import warnings

colorama.init(autoreset=True)

# FİLTER
warnings.filterwarnings("ignore")

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True

bot = commands.Bot(command_prefix='!', intents=intents)

# BANNER
print("\n" * 50)
print(f"{Fore.LIGHTMAGENTA_EX}  /$$$$$$  /$$$$$$$   /$$$$$$ ")
print(f"{Fore.LIGHTMAGENTA_EX} /$$__  $$| $$__  $$ /$$__  $$ ")
print(f"{Fore.LIGHTMAGENTA_EX} | $$  \ $$| $$  \ $$| $$  \__/")
print(f"{Fore.LIGHTMAGENTA_EX} | $$  | $$| $$$$$$$ | $$")
print(f"{Fore.LIGHTMAGENTA_EX} | $$  | $$| $$__  $$| $$")
print(f"{Fore.LIGHTMAGENTA_EX} | $$  | $$| $$  \ $$| $$    $$")
print(f"{Fore.LIGHTMAGENTA_EX} |  $$$$$$/| $$$$$$$/|  $$$$$$/")
print(f"{Fore.LIGHTMAGENTA_EX} \______/ |_______/  \______/ ")
time.sleep(1)

async def emergencyMode():
    for guild in bot.guilds:
        print(f'sending warning message to {guild.name} server')
        for channel in guild.text_channels:
            try:
                await channel.send('Attention bot manager launches emergency protocol!')
                print(f'{Fore.WHITE}{channel.name}{Fore.GREEN} ✓')
            except Exception as e:
                print(f'{Fore.WHITE}{channel.name}{Fore.RED} x{Fore.YELLOW} [{e}]')
    try:
        await bot.close()
        print(f"{Fore.WHITE}Delegate server authorizations{Fore.GREEN} ✓")
    except Exception as e:
        print(f"{Fore.WHITE}Delegate server authorizations{Fore.RED} x [{e}]")
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


async def read_user_input():
    while True:
        tempInput = await asyncio.get_event_loop().run_in_executor(None, input, f">> {Fore.LIGHTGREEN_EX}")
        if tempInput == "!help":
            print(f"{Fore.CYAN}!send {Fore.LIGHTCYAN_EX}<channelId> {Fore.BLUE}<message>")
            print(f"{Fore.CYAN}!monitoringMode {Fore.LIGHTMAGENTA_EX}(does not take arguments)")
            print(f"{Fore.CYAN}!emergencyMode {Fore.LIGHTMAGENTA_EX}(does not take arguments)")
            print(f"{Fore.CYAN}!ban {Fore.LIGHTCYAN_EX}<userID>")
            print(f"{Fore.CYAN}!kick {Fore.LIGHTCYAN_EX}<userID>")
            print(f"{Fore.CYAN}!mute {Fore.LIGHTCYAN_EX}<userID> {Fore.BLUE}<duration (in minutes)>")
            print(f"{Fore.CYAN}!rootInfo {Fore.LIGHTMAGENTA_EX}(does not take arguments)")
        elif tempInput.startswith("!send"):
            try:
                channelId = int(tempInput.split()[1])
                channel = bot.get_channel(channelId)
                if channel:
                    await channel.send(f"{' '.join(tempInput.split()[2:])}")
                else:
                    print(f"{Fore.LIGHTYELLOW_EX}Channel with ID {channelId} not found")
            except Exception as e:
                print(f"{Fore.RED}Error: {e}")
        elif tempInput == "!monitoringMode":
            print(f"{Fore.CYAN} Monitoring mode is on! He's listening now: All")
        elif tempInput == "!emergencyMode":
            print(f"{Fore.RED} EMERGENCY MODE: when emergency mode is turned on, your bot will exit all servers and lock itself!")
            tempInput = input(f"{Fore.LIGHTYELLOW_EX}Are you sure? (Y/N)(default:N) ")
            if tempInput.lower() == "y":
                await emergencyMode()
            else:
                print(f"{Fore.YELLOW}Emergency mode cancelled.")
        elif tempInput == "!rootInfo":
            # bu özellik şimdilik desteklenmemektedir !
            print(f"{Fore.CYAN}discord.com (hidden ip adress) {Fore.GREEN} [DİSCORD][ACTİVE]")
            print(f"{Fore.CYAN}{get_public_ip()}{Fore.GREEN} [THIS MACHINE][ACTİVE]")
        elif tempInput.split()[0] == "!ban":
            pass
        elif tempInput.split()[0] == "!kick":
            pass
        elif tempInput.split()[0] == "!mute":
            pass


@bot.event
async def on_ready():
    print(f"{Fore.LIGHTWHITE_EX}Connected to discord servers with {bot.user.name} account {Fore.GREEN} ✓")
    asyncio.create_task(read_user_input())  # Kullanıcı girişini işleme görevini başlatıyoruz


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    print(f"{Fore.CYAN}{message.author}: {Fore.WHITE}{message.content}")
    await bot.process_commands(message)


print("\n" * 2)

TOKEN = input(f"{Fore.CYAN} Please enter the key of the application you want to connect to (token) {Fore.GREEN}>> ")
if check_connection():
    print(f"{Fore.LIGHTWHITE_EX}Connection{Fore.GREEN} ✓")
else:
    print(f"{Fore.LIGHTWHITE_EX}Connection{Fore.RED} x")
    sys.exit()

try:
    print(f"{Fore.LIGHTWHITE_EX}Connecting to the app{Fore.GREEN} ✓")
    bot.run(TOKEN)
except Exception as e:
    print(f"{Fore.LIGHTWHITE_EX}Connecting to the app{Fore.RED} x")
    print(f"{Fore.YELLOW}Please check if your token is correct.")
    print(f"{Fore.LIGHTYELLOW_EX}Operation terminated for security reasons: {e}")
    sys.exit()
