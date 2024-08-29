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

version = "0.1 BETA"

colorama.init(autoreset=True)

# FİLTER
warnings.filterwarnings("ignore")

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True

bot = commands.Bot(command_prefix='!', intents=intents)

# BANNER
print("\n" * 50)
time.sleep(1)
print(f'''{Fore.LIGHTBLUE_EX}




 
           
        
       "$$$$bo.
         "$$$$$$$$booocS$$$    ..    ,.
     ".    "*$$$$SP{Fore.LIGHTRED_EX}*****{Fore.LIGHTBLUE_EX}V$o..o$$. .$$$b                ░█████╗░██████╗░░█████╗░
      "$$o. .$$$$$o{Fore.LIGHTRED_EX}*****{Fore.LIGHTBLUE_EX}A$$$$$$$$$$$$$$b               ██╔══██╗██╔══██╗██╔══██╗
""bo.   "*$$$$$$$$$$$$$$$$$$$$P*$$$$$$$$:              ██║░░██║██████╦╝██║░░╚═╝
    "$$.    V$$$$$$$$$P"**""*"'   VP  * "l             ██║░░██║██╔══██╗██║░░██╗
     "$$$o.4$$$$$$$$X                                  ╚█████╔╝██████╦╝╚█████╔╝
     "*$$$$$$$$$$$$${Fore.LIGHTRED_EX}AoA$o..{Fore.LIGHTRED_EX}oooooo..           .b{Fore.LIGHTBLUE_EX}       ░╚════╝░╚═════╝░░╚════╝░
            .X$$$$$$$$$$$P""     {Fore.LIGHTRED_EX}""*oo,,     ,$P{Fore.LIGHTBLUE_EX}       {Fore.CYAN}o⃨p⃨e⃨n⃨ b⃨o⃨t⃨ c⃨o⃨n⃨s⃨o⃨l⃨e⃨ {Fore.LIGHTYELLOW_EX}{version}{Fore.LIGHTBLUE_EX}
           $$P""V$$$$$$$:    .        {Fore.LIGHTRED_EX}""*****"{Fore.LIGHTBLUE_EX}  {Fore.CYAN}    Github :{Fore.LIGHTYELLOW_EX} https://bit.ly/4h2u{Fore.LIGHTBLUE_EX} 
          .*"    A$$$$$$$$o.4;      .
               .oP""   "$$$$$$b.  .$;
                         A$$$$$$$$$$P
                         "  "$$$$$P"
                             $$P*"
                            .$"
                            "
''')

async def emergencyMode():
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

async def read_user_input():
    print(f"{Fore.GREEN}Interaction complete ! For help, try this :{Fore.CYAN} !help")
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
            print(f"{Fore.CYAN}!clear {Fore.LIGHTCYAN_EX}<channelId> {Fore.BLUE}<count>")
        elif tempInput.startswith("!send"):
            try:
                channelId = int(tempInput.split()[1])
                channel = bot.get_channel(channelId)
                if channel:
                    await channel.send(f"{' '.join(tempInput.split()[2:])}")
                    print(f"{Fore.LIGHTGREEN_EX} Your message has been sent ✓")
                else:
                    print(f"{Fore.LIGHTYELLOW_EX}Channel with ID {channelId} not found")
                    print(f"{Fore.LIGHTRED_EX} Send operation failed x")
            except Exception as e:
                print(f"{Fore.RED}Error: {e}")
        elif tempInput == "!monitoringMode":
            print(f"{Fore.CYAN} Monitoring mode is on! Listening to all messages.")
        elif tempInput == "!emergencyMode":
            print(f"{Fore.RED} EMERGENCY MODE: When emergency mode is turned on, your bot will exit all servers and lock itself!")
            confirm = input(f"{Fore.LIGHTYELLOW_EX}Are you sure? (Y/N)(default:N) ")
            if confirm.lower() == "y":
                await emergencyMode()
            else:
                print(f"{Fore.YELLOW}Emergency mode cancelled.")
        elif tempInput == "!rootInfo":
            print(f"{Fore.CYAN}discord.com (hidden IP address) {Fore.GREEN} [DİSCORD][ACTIVE]")
            print(f"{Fore.CYAN}{get_public_ip()}{Fore.GREEN} [THIS MACHINE][ACTIVE]")
        elif tempInput.split()[0] == "!ban":
            pass
        elif tempInput.split()[0] == "!kick":
            pass
        elif tempInput.split()[0] == "!mute":
            pass
        elif tempInput.split()[0] == "!clear":
            channel = bot.get_channel(int(tempInput.split()[1]))
            if not channel:
                print(f"{Fore.LIGHTRED_EX}The channel in question was not found x")
            else:
                deleted = await channel.purge(limit=int(tempInput.split()[2]))
                print(f"{Fore.CYAN}{len(deleted)}{Fore.LIGHTGREEN_EX} messages deleted ✓")

@bot.event
async def on_ready():
    print(f"{Fore.LIGHTWHITE_EX}Connected to Discord servers with {bot.user.name} account {Fore.GREEN} ✓")
    asyncio.create_task(read_user_input())  # Start task to handle user input

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    print(f"{Fore.CYAN}{message.author}: {Fore.WHITE}{message.content}")
    await bot.process_commands(message)

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
