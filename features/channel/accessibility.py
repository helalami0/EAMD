from discord.ext import commands


class AccessibilityCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='join', help='Tells the bot to join the voice channel')
    async def join(self, ctx):
        channel = ctx.author.voice.channel
        voice_client = ctx.voice_client

        if channel is None:
            print("Not connected")
            return
        if voice_client and voice_client.is_connected():
            await voice_client.move_to(channel)
            print("Successfuly Connected")
        else:
            voice_client = await channel.connect()
            print("Successfuly Connected")

    @commands.command(name='disconnect', help='Tells the bot to disconnect the voice channel')
    async def disconnect(self, ctx):
        voice_client = ctx.voice_client
        if voice_client.is_connected():
            await voice_client.disconnect()
            print("Successfuly Disconnected")
        else:
            print("Not Connected")