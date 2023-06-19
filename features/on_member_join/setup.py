from features.on_member_join.detect_event import DetectUserJoined


async def setup_on_member_join(bot):
    on_member_join_cog = DetectUserJoined(bot)
    await bot.add_cog(on_member_join_cog)