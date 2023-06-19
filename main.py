import discord
import logging
import os
from dotenv.main import load_dotenv
from discord.ext import commands
from features.channel import setup_commands
from features.utils import setup_events
from features.on_member_join import setup_on_member_join

load_dotenv()
token = os.environ['TOKEN']

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')

bot = commands.Bot(command_prefix='#', intents=intents)

discord.FFmpegPCMAudio.executable = "features/utils/ffmpeg6.0/bin/ffmpeg.exe"

@bot.event
async def on_ready():
    print(f'Bot is ready. Logged in as {bot.user.name} ({bot.user.id})')
    await setup_commands(bot)
    await setup_events(bot)
    await setup_on_member_join(bot)

bot.run(token, log_handler=handler,
        log_level=logging.DEBUG)
