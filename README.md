# Discord-Bot-Prototype

Initial build to understand the basics of programming a discord bot utilizing the discord.py (python) library

## Installing the discord.py library

1. Open the terminal in VSCode (Text Editor may differ)
2. Run "pip install -U discord.py"

## Installing the env library

1. Open a terminal in VSCode (Text Editor may differ)
2. Run "pip install -U python-dotenv"

## Setting up Environment Variables

1. Open the example.env file in VSCode (Text Editor may differ)
2. Update DISCORD_TOKEN to contain the discord bot's token | Replace - {your-bot-token}

   a. If you don't know the token, you'll need to click Reset Token to generate a new one
   b. Token Location = Discord_Developer_Portal -> Your_Application -> Bot_Tab -> Token_Section

3. Update DISCORD_GUILD to contain the name of the discord guild it's associated with | Replace - Guild Name

   a. Don't remove the quotation marks, only change the characters inside of them

4. Initialize the .env file by removing example from example.env | example.env -> .env
5. Save the .env file

## Initializing Client/Bot

- Run "python3 client.py" for client
- Run "python3 bot.py" for bot
