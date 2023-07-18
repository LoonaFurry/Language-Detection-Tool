import discord
import asyncio
from langdetect import detect, LangDetectException

client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    try:
        if detect(message.content) not in ['de', 'en']:
            warning_message = await message.channel.send("Warning: Non-German or Non-English message detected. This message will be deleted in 10 seconds.")
            await message.delete()
            await asyncio.sleep(10)
            await warning_message.delete()
    except LangDetectException:
        return

client.run('Your-Token-Here')

