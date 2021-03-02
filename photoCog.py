import discord
from discord.ext import commands
import os
import random


client = commands.Bot(command_prefix = "v!")


class pictureCog(commands.Cog):
    def __init__(self):
        self.directories = os.listdir()
    @commands.command()
    async def test(self, ctx):
        directoryFound = False
        for directory in self.directories:
            if directory == "peoplePhotos":
                directoryFound = True

        if directoryFound == False:
            os.mkdir("peoplePhotos")
        
        directoryFound = False

        for directory in os.listdir("peoplePhotos"):
            if directory == "john":
                directoryFound = True

        if directoryFound == False:
            os.mkdir("peoplePhotos/john")
        
        photos = os.listdir("peoplePhotos/john")

        if len(photos) == 0:
            await ctx.send("There are no photos stored for this command. Please try again later")

        else:
            photo = random.choice(photos)

            photoFile = discord.File(fp=f"peoplePhotos/john/{photo}")

            await ctx.send("Here's your random image. Enjoy...", file=photoFile)

    @commands.command()
    async def arjhay(self, ctx):
        directoryFound = False
        for directory in self.directories:
            if directory == "peoplePhotos":
                directoryFound = True

        if directoryFound == False:
            os.mkdir("peoplePhotos")
        
        directoryFound = False

        for directory in os.listdir("peoplePhotos"):
            print(directory)
            if directory == "arjhay":
                directoryFound = True

        if directoryFound == False:
            os.mkdir("peoplePhotos/arjhay")
        
        photos = os.listdir("peoplePhotos/arjhay")

        if len(photos) == 0:
            await ctx.send("There are no photos stored for this command. Please try again later")

        else:
            photo = random.choice(photos)

            photoFile = discord.File(fp=f"peoplePhotos/john/{photo}")

            await ctx.send("Here's your random image. Enjoy...", file=photoFile)



     

