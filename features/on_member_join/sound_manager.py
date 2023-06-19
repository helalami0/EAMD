import discord
from pathlib import Path
from .users_manager import UsersManager
from datetime import datetime

#have to implement permission feature
#build on this to use later database
#first try with simple dic


class SoundManager():
    def __init__(self):
        self.usersManager = UsersManager()

    async def getSound(self, user):
        script_path = Path(__file__)
        audio_name = user.name + '.mp3'
        audio_path = script_path.parent / 'audio' / audio_name

        #"D:/Dev/DiscordBot/features/utils/ffmpeg6.0/bin/ffmpeg.exe"

        audio_source = discord.FFmpegPCMAudio(executable="D:/Dev/DiscordBot/features/utils/ffmpeg6.0/bin/ffmpeg.exe", source=str(audio_path))

        return audio_source

    async def playSound(self, user, vc):
        print("Playing sound for:", user.name)

        audio_source = await self.getSound(user)

        if self.isAllowedToPlaySound(user):
            self.usersManager.update_user_data(user)
            vc.play(audio_source)

    def isAllowedToPlaySound(self, user):
        last_connected = self.usersManager.get_user_lastconnection(user)

        if last_connected:
            last_connected = datetime.fromisoformat(last_connected)
            timestamp = datetime.now()
            time_difference = timestamp - last_connected

            if time_difference.total_seconds() > 1 * 30:
                return True
            else:
                return False

        return True

    def addSound(self, user, sound):
        return

    def updateSound(self, user, sound):
        return

