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

presences = [
    "Made By Waffieu",
]
@client.event
async def on_ready():
    print(f"Bot logged in as {client.user}")

# Set the bot's activity and status
    activity = discord.Activity(
        type=discord.ActivityType.playing,
        name="Made By Waffieu"
    )
    await client.change_presence(activity=activity, status=discord.Status.online)

    presences_cycle = cycle(presences)
    while True:
        presence = next(presences_cycle)
        presence_with_count = presence.replace("{guild_count}", str(len(bot.guilds)))
        delay = 30  # Delay in seconds, adjust as needed
        await client.change_presence(activity=discord.Game(name=presence_with_count))
        await asyncio.sleep(delay)


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

client.run('your-bot-token')

