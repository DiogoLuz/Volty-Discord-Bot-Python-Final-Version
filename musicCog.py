import discord
from discord.ext import commands
import youtube_dl
import asyncio

class Song(songName, user):
    def __init__(self):
        self.songName = songName
        self.user = user



class musicCog(commands.Cog):
    def __init__(self):
        self.queue = []

    @commands.command()
    async def play(self, ctx,*, song):


