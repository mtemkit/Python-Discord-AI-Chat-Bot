import os
import discord
import requests
import json
from flask import Flask

# Get the OpenAI API key from the environment variables
api_key = os.environ['CHATGPT_API_KEY']

#client = discord.Client()

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    channel = client.get_channel(1056001153747390587)

    # Send the message to the channel
    await channel.send('Im back to being live! Feel free to ask any questions or just have a chat!')


@client.event
async def on_message(message):
    print (message.content)
    if message.author == client.user:
        return

    if message.content.startswith(''):
        # Set the prompt and maximum number of tokens
        model = 'text-davinci-003'
        
        # Extract the user's question from the message content
        #question = message.content[len('prompt'):].strip()
        question = message.content
        
        #prompt = 'What is your favorite color?'
        max_tokens = 500

        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {api_key}',
        }

        data = {
            'model': model,
            'prompt': question,
            'max_tokens': max_tokens,
        }


        print("here")
        try:
            # Send the request to the OpenAI API
            response = requests.post('https://api.openai.com/v1/completions', headers=headers, json=data)
            response_object = response.text
            response_text = json.loads(response_object)['choices'][0]['text']
            await message.channel.send(response_text)
        except Exception as e:
            # Handle any exceptions that might occur
            print(f'An error occurred: {e}')

# Get the Discord bot token from the environment variables
bot_token = os.environ['DISCORD_BOT_TOKEN']
client.run(bot_token)