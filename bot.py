# i am following sosp's guide but idk if it is the best https://sosp22.com/chatbots#replitcom-setup one sec
# might be better to treat this as a client

import discord
from discord.ext import commands
from datetime import datetime, time
from random import randint

import asyncio
import os
import dotenv

dotenv.load_dotenv()
# client = discord.Client(intents=discord.Intents.all())
client = discord.ext.commands.Bot(".", intents=discord.Intents.all())

TOKEN = os.getenv('DISCORD_TOKEN')
CHANNEL_ID = os.getenv('CHANNEL_ID')
SECRET_TAG = os.getenv('SECRET_KEY')

# client = discord.Client(intents=discord.Intents.all())
# bot = discord.Client(intents=discord.Intents.all(), prefix=".")
bot = discord.ext.commands.Bot(".", intents=discord.Intents.all())
ctr = 0

@bot.event
async def on_ready():
    print("has connected to Discord")

@bot.event
async def hello_world(message):
    await message.channel.send('Hello world!')

@bot.event
async def on_message(message):
    # u need this if yw to access the counter
    global ctr
    # # WE LIKE THIS yes 
    # if message.author == bot.user:
    #     return
    
    channel = bot.get_channel(int(CHANNEL_ID)) 
    recipient = f"<@{message.author.id}>"
    if ctr == 0:
        message = await channel.send(f"{SECRET_TAG} reminds {SECRET_TAG} to do th stupid mps!!") 
        ctr = randint(1, 10)
    else:
        ctr -= 1
    print(ctr)
    
    
@client.command
async def ping_at_datetime():
    await client.wait_until_ready()
    channel = client.get_channel(CHANNEL_ID)
    while client.is_open():
        now = datetime.now().time
        if (now >= time(22, 0) or now < time(1, 0)): # send notif between 10pm and 1am
            await channel.send("IM LIVING IN UR WALLS")
        await asyncio.sleep(60) # PINGS EVERY MIN :D

    client.loop.create_task(ping_at_datetime)
    client.run(TOKEN)
    # isn't run blocking

@bot.command()
async def ping(ctx):
    print("in")
    message = await ctx.send("aydan pirani is nerd!!")
    await message.edit(content = f":ping_pong:! {round(bot.latency*1000,2)} ms")

bot.run(TOKEN)