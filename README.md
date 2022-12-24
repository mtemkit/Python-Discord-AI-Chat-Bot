# Python-Discord-AI-Chat-Bot

### What is it?
A discord chat bot that can respond dynamically and creatively in conversations with discord users.

### Purpose:
To save time by no longer needing to login and connect to the OpenAI website to speak to a chat bot, while also providing an entertaining and convenient experience to discord users who want a chat bot on their server.

### What Inspired this Project?

I previously developed a Discord chat bot using Node.js and a chat API from a small team. Initially, I hosted the bot on Glitch, but due to the 5-minute sleep intervals, I decided to migrate it to Heroku for its Dyno hours which allows for smooth operation within the free tier. I believe this was a better choice for the long-term operation of the bot.

With the rise of ChatGPT, I decided it was time to create a new discord chat bot and use Python this time as well as FireBase Cloud to run it.

### Programming Langues Used:

Python

### APIs Used:

Discord, Open AI

### Hosting:

FireBase Cloud w/ Github Actions

Note: It's possible to run the bot for up to 6 hours at a time for every git push using solely Github Actions while running the python chat bot file with a workflow. However, I have chosen to instead use Github actions for deployment and Firebase Cloud for continuous hosting. This also allows me to host a site with the bot and add information bout it.

### Languages Used for File Configuration:

YAML

### Live Demo:

(in progress)

### Set-Up Process:

Store the discord and open ai key in a ".env". sampleEnvVars shows the required env variables for this file.

To run the bot, the following libraries are required (see installed libraries using "pip freeze"):
pip install firebase-admin
pip install firebase-cli
pip install discord
pip install requests
pip install revChatGPT

The bot is then ran using: chatbot.py

Firebase Hosting:
npm install -g firebase-tools
firebase login --no-localhost
firebase init
firebase deploy

If using windows, or windows subsystem for Linux, make sure to edit your system path variables:
/mnt/c/Windows/system32;C:\Windows\System32

Get firebase_token using: firebase login:ci in terminal

Make sure to Access Your Secret Keys:
Secret Key Management: https://github.com/[username]/Python-Discord-AI-Chat-Bot/settings/secrets
Replace "[username]" with your github username, such as "mtemkit". 

Test in the console using: python chatbot.py

Project Console: https://console.firebase.google.com/project/chatboigptai/overview
Hosting URL: https://chatboigptai.web.app

Note: YAML/yml file names for the github actions workflows can be renamed without affecting functionality but it's a good idea to give descriptive names that accurately reflect the purpose of the workflow.

### Extra Notes:

- The final image used to represent the chat bot was also chosen amongst several other images generated using one of OpenAi's models!

<p align="left">
  <img src="images/professor_chat_bot.png" width="800" height="800" title="Chat Bot Representing Image">
</p>

