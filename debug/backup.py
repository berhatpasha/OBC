import discord
import colorama
import time
from colorama import Fore
colorama.init(autoreset=True)
from discord.ext import commands
import sys
from tqdm import tqdm
import urllib.request
import requests
import asyncio

intents = discord.Intents.default()
intents.message_content = True  # Mesaj içeriğine erişim izni gerekli
intents.guilds = True           # Sunucuları görme izni gerekli

client = discord.Client(intents=intents)


def emergencyMode():
    print("")
    print(f'Bot {client.user} olarak giriş yaptı!')
    for guild in client.guilds:
        print(f'{guild.name} sunucusunda mesaj gönderiliyor...')
        for channel in guild.text_channels:  # Metin kanallarını al
            try:
                await channel.send('sa')
                print(f'{channel.name} kanalına mesaj gönderildi.')
            except Exception as e:
                print(f'{channel.name} kanalına mesaj gönderilirken bir hata oluştu: {e}')
    await client.close()


def get_public_ip():
    try:
        response = requests.get('https://api.ipify.org?format=json')
        ip_info = response.json()
        return  ip_info['ip']
    except:
        return "eror"

def check_connection(url="http://www.google.com"):
    try:
        urllib.request.urlopen(url, timeout=5)
        return True
    except urllib.error.URLError:
        return False

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

TOKEN = "XYZ"

@bot.event
async def on_ready():
    print(f"{Fore.LIGHTWHITE_EX}Connected to discord servers with {bot.user.name} account {Fore.GREEN} ✓")
    while True:
        tempInput = input(">> ")
        if tempInput == "!help":
            print(f"!send <channelId> <message>")
            print(f"")
            print(f"")
            print(f"")
            print(f"")
        elif tempInput.split()[0] == "!send":
            channelId = int(tempInput.split()[1])
            channel = bot.get_channel(channelId)
            if channel:
                await channel.send(f"{tempInput.split()[2:]}")
            else:
                print(f"{Fore.LIGHTYELLOW_EX}Channel with ID {channelId} not found")
        elif tempInput == "!monitoringMode":
            print(f"{Fore.CYAN} Monitroing mode is on! He's listening now: All")
            return
        elif tempInput == "!ban":
            print("")
        elif tempInput == "!kick":
            print("")
        elif tempInput.split()[0] == "!mute":
            log = tempInput.split()[1]
        elif tempInput.split()[0] == "!changeUserName":
            user = tempInput.split()[1]
            nick = tempInput.split()[1]
        elif tempInput == "!rootStatus":
            print(f"{Fore.CYAN}discord.com{Fore.GREEN} [ACTİVE][DİSCORD]")
            print(f"{Fore.CYAN}{get_public_ip()}{Fore.GREEN} [ACTİVE][YOU]")
            print(f"{Fore.CYAN}-")
            print(f"{Fore.CYAN}-")
            print(f"{Fore.CYAN}-")
        elif tempInput == "!emergencyMode":
            print(f"{Fore.RED}")
            print(f"{Fore.RED}")
            print(f"{Fore.RED}")
            print(f"{Fore.RED}")
            print(f"{Fore.RED}")
            print(f"{Fore.RED}")
            print(f"{Fore.RED}")
            print(f"{Fore.RED}")
            print(f"{Fore.RED}")
            print(f"{Fore.RED}")
            print(f"{Fore.RED}")
            print(f"{Fore.RED}")
            print(f"{Fore.RED} EMERGENCY MODE: when emergency mode is turned on, your bot will exit all servers and lock itself!")
            tempInput = input(f"{Fore.LIGHTYELLOW_EX}Are you sure? (Y/N)(defould:N)")
            if tempInput == "Y":
                emergencyMode()
            elif tempInput == "y":
                emergencyMode()
            elif tempInput == "N":
                print("")
                print("")
                pass
            elif tempInput == "n":
                print("")
                print("")
                pass
            else:
                print("")
                print("")
                pass







@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    print(f"{Fore.CYAN}{message.author}: {Fore.WHITE}{message.content}")

    await bot.process_commands(message)

print("\n" * 9)

TOKEN = input(f"{Fore.CYAN} Please enter the key of the application you want to connect to (token) >> ")
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
