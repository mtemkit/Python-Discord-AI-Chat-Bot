import os
import discord
import dotenv
import requests
import firebase_admin
from firebase_admin import credentials

dotenv.load_dotenv()

cred = credentials.Certificate('path/to/serviceAccountKey.json')
firebase_admin.initialize_app(cred)

"""
from firebase_admin import db

# Get a reference to the database
database = db.reference()

# Read data from the database
data = database.get()
"""

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!prompt'):
        prompt = 'What is your favorite color?'
        max_tokens = 256
        api_key = os.getenv('CHATGPT_API_KEY')

        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {api_key}',
        }

        data = {
            'prompt': prompt,
            'max_tokens': max_tokens,
        }

        response = requests.post('https://api.openai.com/v1/chatgpt/prompt', headers=headers, json=data)
        response_text = response.json()['text']
        await message.channel.send(response_text)

client.run(os.getenv('DISCORD_BOT_TOKEN'))