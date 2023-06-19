from features.channel.accessibility import AccessibilityCommands


async def setup_commands(bot):
    accessibility_cog = AccessibilityCommands(bot)
    await bot.add_cog(accessibility_cog)