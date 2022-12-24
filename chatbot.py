import os
import discord
import requests
import firebase_admin
from revChatGPT.revChatGPT import Chatbot


#chatbot = Chatbot({})

#chatbot.get_chat_response(prompt, output="text") #output=stream uses async generator


# Initialize Firebase
cred = firebase_admin.credentials.ApplicationDefault()
firebase_admin.initialize_app(cred)

# Get the OpenAI API key from the environment variables
api_key = os.environ['CHATGPT_API_KEY']

#client = discord.Client()

client = discord.Client(intents=discord.Intents.default())

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    channel = client.get_channel(1056001153747390587)

    # Send the message to the channel
    await channel.send('Hello, world!')



@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!prompt'):
        # Set the prompt and maximum number of tokens
        prompt = 'What is your favorite color?'
        max_tokens = 256

        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {api_key}',
        }

        data = {
            'prompt': prompt,
            'max_tokens': max_tokens,
        }

        # Send the request to the OpenAI API
        response = requests.post('https://api.openai.com/v1/chatgpt/prompt', headers=headers, json=data)
        response_text = response.json()['text']
        await message.channel.send(response_text)

# Get the Discord bot token from the environment variables
bot_token = os.environ['DISCORD_BOT_TOKEN']
client.run(bot_token)
