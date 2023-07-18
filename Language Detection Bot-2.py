import transformers
import discord
import time

# Initialize the Discord client
client = discord.Client(intents=discord.Intents.default())

# Function to detect if a sentence is in English
def detect_english_sentence(sentence):
    model = transformers.BertModel.from_pretrained("bert-base-multilingual-cased")
    tokenizer = transformers.BertTokenizer.from_pretrained("bert-base-multilingual-cased")
    input_ids = tokenizer(sentence, return_tensors="pt")["input_ids"]
    predictions = model(input_ids)
    prediction = predictions.last_hidden_state[0].softmax(dim=-1)
    prediction = prediction.argmax(dim=-1)
    return prediction == 1

# Function to delete non-English sentences
def delete_non_english_sentence(message):
    if not detect_english_sentence(message.content):
        message.delete()
        message.channel.send("Warning: Non-English sentence detected. Deleting.")
        time.sleep(10)

# Event handler for new messages
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    delete_non_english_sentence(message)

# Run the Discord bot
client.run('Your-Token-Here')
