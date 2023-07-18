import pycld2 as cld2
import discord
import os
import asyncio

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

def detect_non_english_sentence(sentence):
    is_reliable, _, details = cld2.detect(sentence)
    return not is_reliable or details[0][0] != "ENGLISH"

@client.event
async def on_ready():
    print(f"Bot logged in as {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if detect_non_english_sentence(message.content):
        if "hi" not in message.content.lower():
            await message.delete()
            await message.channel.send(f"Warning: Non-English sentence detected from {message.author.mention}. Deleting.")
            await asyncio.sleep(10)
            await message.channel.purge(limit=1)  # Delete the warning message after 10 seconds

client.run('MTA1MDczMzE4ODAxMzYyNTQwNA.GWL6O7.W49GIlPmIV5DosgJdxq4B8juCywJcc9GpdqQwM')

