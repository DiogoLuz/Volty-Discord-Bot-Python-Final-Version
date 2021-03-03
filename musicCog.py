from __future__ import unicode_literals
import discord
from discord.ext import commands
import youtube_dl
import asyncio
import os
from queue import Queue


class Song:
    def __init__(self, songName, songPath, user):
        self.songName = songName
        self.user = user
        self.songPath = songPath
        



class musicCog(commands.Cog):
    def __init__(self):
        self.queue = Queue()
        self.directories = os.listdir()

    @commands.command()
    async def play(self, ctx,*, url):
        user = ctx.author

        bot = ctx.bot


        botVoiceClient = ctx.voice_client

        voiceChannel = ctx.author.voice.channel


        
        if ctx.voice_client is None:
            self.vc = await voiceChannel.connect()
        else:
            await ctx.voice_client.move_to(voiceChannel)
            self.vc = ctx.voice_client

        

        directoryFound = False
        for directory in self.directories:
            if directory == "music":
                directoryFound = True

        if directoryFound == False:
            os.mkdir("music")
        
        directoryFound = False

        for directory in os.listdir("music"):
            if directory == "queue":
                directoryFound = True

        if directoryFound == False:
            os.mkdir("music/queue")

        ydl_opts = {
                        'format': 'bestaudio/best',
                        'outtmpl': 'music/queue/%(title)s.%(ext)s',
                        'postprocessors': [{
                            'key': 'FFmpegExtractAudio',
                            'preferredcodec': 'mp3',
                            'preferredquality': '192',
                        }]}

        await ctx.send("Loading song...")
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
            songInformation = ydl.extract_info(url, download=False)

        songPath = os.listdir("music/queue")
        for song in songPath:
            if songInformation["title"] in song:
                songPath = f"music/queue/{song}"

        song = Song(songInformation['title'], songPath, ctx.author)

        self.queue.put(song)

        songToPlay = self.queue.get()

        self.ffmpegAudio = discord.FFmpegPCMAudio(source=songToPlay.songPath)

        await ctx.send(f"Now playing: {songToPlay.songName}")

        
        if not self.vc.is_playing():
            self.vc.play(source=self.ffmpegAudio)
        else:
            await ctx.send("Added to queue!")

            self.queue.put(song)

            songToPlay = self.queue.get()

            self.ffmpegAudio = discord.FFmpegPCMAudio(source=songToPlay.songPath)
        

    @commands.command()
    async def skip(self, ctx):
        print(self.vc.is_playing())
        if not self.vc.is_playing():
            await ctx.send("There is no song to skip!")
        else:
            skippedSong = self.queue.get()

            self.ffmpegAudio = discord.FFmpegPCMAudio(source=skippedSong.songPath)

            await ctx.send(f"Skipped song! Now playing: {skippedSong.songPath}")

            self.vc.stop()

            self.vc.play(source=self.ffmpegAudio)






            









        

        
