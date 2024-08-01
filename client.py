# imports
import os
import random
import discord
from dotenv import load_dotenv

# Parse .env file and load variables
load_dotenv()

# Environment variables
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

# Flag all intents to true
intents = discord.Intents.all()

# Client connection to Discord
client = discord.Client(intents = intents)

# on_ready() | Called when bot is initialized
# Print bot connected, server name, server id, and server members
@client.event
async def on_ready():
    guild = discord.utils.get(client.guilds, name=GUILD)
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )
    print(f'{client.user.name} has connected to Discord!')

    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')

# on_member_join(member) | Called when a user joins the server
# Bot will DM new user a welcome message
@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )

# on_message(message) | Called when a message is created and sent
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    wow_famous_quotes = [
        "I am Deathwing, the Destroyer, the end of all things! Inevitable. Indomitable. I am the Cataclysm!",
        "You are not prepared!",
        "Now I stand, the lion before the lambs… And they do not fear. They cannot fear.",
        "You cannot kill hope.",
        "For the Alliance!",
        "For the Horde!",
        "By fire, be purged!",
        "Did you think we had forgotten? Did you think we had forgiven? Behold, now, the terrible vengeance of the Forsaken.",
        "My son, the day you were born, the very forests of Lordaeron whispered the name Arthas.",
        "Lok'tar Ogar"
    ]

    if message.content.lower() == "wow":
        response = random.choice(wow_famous_quotes)
        await message.channel.send(response)
    elif message.content == 'raise-exception':
        raise discord.DiscordException

# on_error(event, *args, **kwargs) | Called when an exception is raised
# Writes error message in error.log if error is due to on_message() event
@client.event
async def on_error(event, *args, **kwargs):
    with open('error.log', 'a') as f:
        if event == 'on_message':
            f.write(f'Unhandled message: {args[0]}\n')
        else:
            raise


# Initialize client using environment Token
client.run(TOKEN)