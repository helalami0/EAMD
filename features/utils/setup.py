from features.utils.accessibility import AccessibilityEvents


async def setup_events(bot):
    accessibility_cog = AccessibilityEvents(bot)
    await bot.add_cog(accessibility_cog)