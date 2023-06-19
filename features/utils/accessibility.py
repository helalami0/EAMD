from discord.ext import commands


class AccessibilityEvents(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # @channel.event
    # async def on_ready(self):
    #     print(f'Logged on as {self.bot.user}!')

    @commands.Cog.listener()
    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')
        await self.bot.process_commands(message)

    # @commands.Cog.listener()
    # async def on_voice_state_update(self, member, before, after):
    #     if before.channel is None and after.channel is not None:
    #         print(f'{member} joined {after.channel.name}')