# Python-Discord-AI-Chat-Bot

### What is it?
A discord chat bot that can respond dynamically and creatively in conversations with discord users.

### Purpose:
To save time by no longer needing to login and connect to the OpenAI website to speak to a chat bot, while also providing an entertaining and convenient experience to discord users who want a chat bot on their server.

### What Inspired this Project?

I previously developed a Discord chat bot using Node.js and a chat API from a small team. Initially, I hosted the bot on repl.it, but due to the 5-minute sleep intervals, I decided to migrate it to Heroku for its Dyno hours which allows for smooth operation within the free tier. I believe that this was a better choice for the long-term operation of the bot.

With the rise of ChatGPT, I decided that it was time to create a new discord chat bot and use Python this time as well as a new hosting service to run it since Heroku no longer offers free dyno hours.

### Programming Langues Used:

Python (in progress, may require using Flask framework)

### APIs Used:

Discord, Open AI

### Hosting:

Update: This bot will no longer be hosted indefinitely for public use. It will mainly be for testing the code. If you manage catch the bot a few hours after I update the code, I've opted to leave the bot live for up to six hours after each code update.

PythonAnywhere with Github Actions (still updating only for testing purposes)

~~Firebase Cloud (previously)~~

Considerations: 

The bot should hypothetically be able to run indefinitely for free using PythonAnywhere hosting. However, the GPT-3 Davinci model (OpenAI's currently most powerful model besides ChatGPT) is starting to incur costs since I have ran out of credits so I will only be running the bot for testing purposes mainly using Github Actions. I have also opted to use the slightly weaker Babbage model for the chat bot to minimize these testing costs.

Therefore, for now, I will solely be using github actions meaning that the bot may not always be live. It's possible to run the bot for up to six hours at a time with every git push using solely Github Actions while running the python chat bot file with a workflow. I will also occasionally host the bot locally for testing purposes. Although hosting in this way is free, the API will still cost.

~~However, you can eventually expect the bot to run continuously once I've switched from firebase to another free hosting service.~~ 

The previous hosting service used for this project was Firebase Cloud with Github Actions for deployment but I found out that using Firebase Cloud Functions requires a pay-as-you-go plan so I've decided to delete the hosting files and functions and start over. At the moment, I've started looking into PythonAnywhere. I will add the code to enable hosting with this service but won't be implementing it until I can find a free and strong chatbot API that allows for a small number of users.

### Languages Used for Deployment:

YAML

Note: YAML/yml file names for the github actions workflows can be renamed without affecting functionality but it's a good idea to give descriptive names that accurately reflect the purpose of the workflow.

### Live Demo:

Below is a typical interaction you could expect with the bot. 

<p align="left">
  <img src="images/chat_with_bot.png" width="800" height="600" title="Chat Bot Discord Conversation">
</p>

### Test it Yourself:

~~Join the project discord to test it yourself: https://discord.gg/qV7rzjPZxV~~ (for cost reasons, it is only useable 6 hours after the code is updated)

OpenAI credits are used up and the bot is starting to incur costs. For now, I will only be running it for testing. I considered using GPT-2 to bypass this and just host the model since the small version is open-source and should be usable with free hosting, however, the strength of the model is a lot weaker than GPT-3's Davinci and Babbage models.

### Set-Up Process:

The file called "sampleGithubEnvVars" shows the required env variables for deploying the bot.

Before running the bot, the following libraries are required (see installed libraries using "pip freeze"):
pip install discord
pip install requests
pip install flask

If you want to run the bot locally, you can run: main.py

If using windows, or windows subsystem for Linux, make sure to edit your system path variables with secret keys:
/mnt/c/Windows/system32;C:\Windows\System32

Link access or edit your secret keys for github actions. Replace "[username]" with your github username, such as "mtemkit": 
https://github.com/[username]/Python-Discord-AI-Chat-Bot/settings/secrets

### Extra Notes:

The final image used to represent the chat bot was also chosen out of several other images generated using one of OpenAi's models! Feel free to look through them in the images folder.

<p align="left">
  <img src="images/professor_chat_bot.png" width="800" height="800" title="Chat Bot Representing Image">
</p>