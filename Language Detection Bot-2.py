import pycld2
import discord
import time

client = discord.Client(intents=discord.Intents.default())

def detect_non_english_sentence(sentence):
    is_reliable, _, details = pycld2.detect(sentence)
    return not is_reliable or details[0][0] != "ENGLISH"

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if detect_non_english_sentence(message.content):
        await message.delete()
        await message.channel.send("Warning: Non-English sentence detected. Deleting.")
        time.sleep(10)
        await message.channel.purge(limit=1)  # Delete the warning message after 10 seconds

client.run('Your-Token-Here')
