import discord
import colorama
from colorama import Fore

colorama.init(autoreset=True)
from discord.ext import commands
import sys
import urllib.request
import requests
import asyncio

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True

client = discord.Client(intents=intents)


async def emergencyMode():
    for guild in client.guilds:
        print("test 1")
        print(f'sending warning message to {guild.name} server')
        for channel in guild.text_channels:
            try:
                print("test2")
                await channel.send('Attention bot manager launches emergency protocol!')
                print(f'{Fore.WHITE}{channel.name}{Fore.GREEN} ✓')
            except Exception as e:
                print("test3")
                print(f'{Fore.WHITE}{channel.name}{Fore.RED} x{Fore.YELLOW} [{e}]')
    try:
        await client.close()
        print(f"{Fore.WHITE}Delegate server authorizations{Fore.GREEN} ✓")
    except:
        print(f"{Fore.WHITE}Delegate server authorizations{Fore.RED} x")
    print("XXXXXXXXXXXXXXX")
    sys.exit()


def get_public_ip():
    try:
        response = requests.get('https://api.ipify.org?format=json')
        ip_info = response.json()
        return ip_info['ip']
    except:
        return "error"


def check_connection(url="http://www.google.com"):
    try:
        urllib.request.urlopen(url, timeout=5)
        return True
    except urllib.error.URLError:
        return False


bot = commands.Bot(command_prefix='!', intents=intents)

TOKEN = "XYZ"


@bot.event
async def on_ready():
    print(f"{Fore.LIGHTWHITE_EX}Connected to discord servers with {bot.user.name} account {Fore.GREEN} ✓")
    while True:
        tempInput = input(f">> {Fore.LIGHTGREEN_EX}")
        if tempInput == "!help":
            print(f"!send <channelId> <message>")
        elif tempInput.split()[0] == "!send":
            channelId = int(tempInput.split()[1])
            channel = bot.get_channel(channelId)
            if channel:
                await channel.send(f"{tempInput.split()[2:]}")
            else:
                print(f"{Fore.LIGHTYELLOW_EX}Channel with ID {channelId} not found")
        elif tempInput == "!monitoringMode":
            print(f"{Fore.CYAN} Monitoring mode is on! He's listening now: All")
            return
        elif tempInput == "!emergencyMode":
            print(
                f"{Fore.RED} EMERGENCY MODE: when emergency mode is turned on, your bot will exit all servers and lock itself!")
            tempInput = input(f"{Fore.LIGHTYELLOW_EX}Are you sure? (Y/N)(default:N)")
            if tempInput.lower() == "y":
                await emergencyMode()
            else:
                print(f"{Fore.YELLOW}Emergency mode cancelled.")


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    print(f"{Fore.CYAN}{message.author}: {Fore.WHITE}{message.content}")
    await bot.process_commands(message)


print("\n" * 9)

TOKEN = input(f"{Fore.CYAN} Please enter the key of the application you want to connect to (token) {Fore.GREEN}>> ")
if check_connection():
    print(f"{Fore.LIGHTWHITE_EX}Connection{Fore.GREEN} ✓")
else:
    print(f"{Fore.LIGHTWHITE_EX}Connection{Fore.RED} x")
    sys.exit()

try:
    print(f"{Fore.LIGHTWHITE_EX}Connecting to the app{Fore.GREEN} ✓")
    bot.run(TOKEN)
except:
    print(f"{Fore.LIGHTWHITE_EX}Connecting to the app{Fore.RED} x")
    print(f"{Fore.YELLOW}Please check if your token is correct.")
    print(f"{Fore.LIGHTYELLOW_EX}Operation terminated for security reasons")
    sys.exit()
