# Python-Discord-AI-Chat-Bot

### What is it?
A discord chat bot that can respond dynamically and creatively in conversations with discord users.

### Purpose:
To save time by no longer needing to login and connect to the OpenAI website to speak to a chat bot, while also providing an entertaining and convenient experience to discord users who want a chat bot on their server.

### What Inspired this Project?

I previously developed a Discord chat bot using Node.js and a chat API from a small team. Initially, I hosted the bot on Glitch, but due to the 5-minute sleep intervals, I decided to migrate it to Heroku for its Dyno hours which allows for smooth operation within the free tier. I believe this was a better choice for the long-term operation of the bot.

With the addition of ChatGPT, I decided it was time to create a new discord chat bot and decided to use Python this time as well as FireBase Cloud to run it.

### Langues Used:

Python

### APIs Used:

Discord, Open AI

### Hosting:

- FireBase Cloud 

### Live Demo:

(in progress)

### Set-Up Process:

Store the discord and open ai key in a ".env". sampleEnvVars shows the required env variables for this file.

To run the bot, the following libraries are required:
pip install firebase-admin
pip install firebase-cli
pip install discord
pip install requests
pip install python-dotenv

The bot is then ran using: chat_bot.py

Firebase Hosting:
npm install -g firebase-tools
firebase login --no-localhost
firebase init
firebase deploy

If using windows, or windows subsystem for Linux, make sure to edit your system path variables:
/mnt/c/Windows/system32;C:\Windows\System32

Make sure to Access Your Secret Keys:
Secret Key Management: https://github.com/[username]/Python-Discord-AI-Chat-Bot/settings/secrets
Replace "[username]" with your github username, such as "mtemkit". 

### Extra Notes:

- The final image used to represent the chat bot was also chosen amongst several other images generated using one of OpenAi's models!

<p align="left">
  <img src="images/professor_chat_bot.png" width="800" height="900" title="Chat Bot Representing Image">
</p>
