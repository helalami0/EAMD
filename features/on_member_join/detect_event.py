from discord.ext import commands
from .sound_manager import SoundManager
import discord


class DetectUserJoined(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.soundManager = SoundManager()

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        if before.channel is None and after.channel is not None:
            print(f'{member} joined {after.channel.name}')
            target_channel_id = after.channel.id
            vc = discord.utils.get(self.bot.voice_clients, channel__id = target_channel_id)
            if not vc:
                print("not connected")
                try:
                    vc = await after.channel.connect()
                    print("now connected")
                except discord.ClientException:
                    print("bot already connected to another channel")
                    return
            else:
                print("was connected")
            await self.soundManager.playSound(member, vc)

