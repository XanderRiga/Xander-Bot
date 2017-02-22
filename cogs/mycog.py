import discord
from discord.ext import commands

class Mycog:
    """My custom cog that does stuff!"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def mycom(self):
        """This does stuff!"""

        #Your code will go here
        await self.bot.say("I can do stuff!")

    @commands.command(pass_context=True)
    async def echo(self, ctx, message):

        author = ctx.message.author
        myString = ctx.message.content
        await self.bot.say("{} {}".format(author.mention, myString[6:]))

def setup(bot):
    bot.add_cog(Mycog(bot))