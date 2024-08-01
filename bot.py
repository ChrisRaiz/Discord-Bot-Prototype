# Imports
import os
import random
import discord
import aiohttp
from io import BytesIO
from dotenv import load_dotenv
from discord.ext import commands

# Parse .env file and load variables
load_dotenv()

# Environment variables
TOKEN = os.getenv('DISCORD_TOKEN')

# Flag all intents to true
intents = discord.Intents.all()

# Initialize bot commands | !cmd
bot = commands.Bot(command_prefix = '!', intents = intents)

# Print bot connected
@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

# Send a random quote from wow_famous_quotes
@bot.command(name='quote', help='Responds with a random quote from World of Warcraft')
async def wow_quote(ctx):
    
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

    response = random.choice(wow_famous_quotes)
    await ctx.send(response)

# Simulate rolling x dice with x sides
@bot.command(name = 'roll_dice', help = 'Simulates rolling dice')
async def roll_dice(ctx, number_of_dice: int, number_of_sides: int):
    
    dice = [
        str(random.choice(range(1, number_of_sides + 1)))
        for _ in range(number_of_dice)
    ]

    await ctx.send(', '.join(dice))

# Create a new text channel named x
@bot.command(name = 'create_channel', help = 'Creates a new channel')
@commands.has_role('addymin')
async def create_channel(ctx, channel_name: str):
    
    guild = ctx.guild
    existing_channel = discord.utils.get(guild.channels, name = channel_name)

    if not existing_channel:
        print(f'Creating a new channel: {channel_name}')
        await guild.create_text_channel(channel_name)

# Role error event handler
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send('You do not have the correct role for this command.')

# Sends a random image with random dimensions
@bot.command(name = 'image_test', help = 'Sends a random image')
async def image_test(ctx):
    random_dimension = random.randint(100, 800)
    random_image_url = f'https://picsum.photos/{random_dimension}/{random_dimension}'

    async with aiohttp.ClientSession() as session: # creates session
      async with session.get(random_image_url) as response: # gets image from url
          img = await response.read() # reads image from response
          with BytesIO(img) as file: # converts to file-like object
              await ctx.send(file=discord.File(file, "randomimage.png"))


bot.run(TOKEN)

