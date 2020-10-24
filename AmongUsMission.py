import discord
import asyncio
from discord.ext import commands
from discord.utils import get


PREFIX = "$"
bot = commands.Bot(command_prefix=PREFIX)
client = discord.Client()

@bot.event
async def on_ready():
    activity = discord.Game(name="Among us {Type $cmd for commands}", type=3)
    await bot.change_presence(status=discord.Status.idle, activity=activity)
    return



@bot.command()
async def Au(ctx, arg):
    channel = bot.get_channel(751460282118963201)
    try:
        Line = arg
        Room_ID, Server = Line.split(":")
        await ctx.send("{} invite created successfully".format(ctx.message.author.mention))
        await channel.send("<@&757163360541474818> Your friend has invited you for a game of Among Us! Join soon!")
        await channel.send("Room ID: " + Room_ID)
        await channel.send("Server: " + Server)

        # Get the message and the reaction
        msg = await channel.send("Shall we play? (react to the message)")
        await msg.add_reaction("🏓")

        def check(reaction, user):
            return user == ctx.message.author and str(reaction.emoji) == "🏓"

        try:
            reaction, user = await client.wait_for("reaction_add", timeout=180.0, check=check)
        except asyncio.TimeoutError:
            await channel.send("Okay my fellow crewmates, waiting time is over!")
            msg = await channel.fetch_message(msg.id)
            count = sum([i.count for i in msg.reactions])
            if count >= 5:
                await channel.send("There are " + str(count - 1) + " members as of now. Good to go!")
            else:
                await channel.send("Oops, there are only " + str(count - 1) + " members! We can't play :(")


    except ValueError:
        await ctx.send("Invalid invite\n1. Check if there is a colon in between the Room ID and Server\n2. Please type $cmd for commands")


@bot.command()
async def Pu(ctx, arg):
    if arg == "call":
        channel = bot.get_channel(751460282118963201)
        await ctx.send("{} Sure, just u wait".format(ctx.message.author.mention))
        await channel.send("<@&757163360541474818> Your friend has invited you for a game of Among Us! Make sure to join!")


        # Get the message and the reaction
        msg = await channel.send("Are u guys comin? (react to the message)")
        await msg.add_reaction("🏓")

        def check(reaction, user):
            return user == ctx.message.author and str(reaction.emoji) == "🏓"

        try:
            reaction, user = await client.wait_for("reaction_add", timeout=1200.0, check=check)
        except asyncio.TimeoutError:
            msg = await channel.fetch_message(msg.id)
            count = sum([i.count for i in msg.reactions])
            if count >= 5:
                await channel.send("There are " + str(count - 1) + " members as of now. You could host the game!")
            else:
                await channel.send("Oops, there are only " + str(count - 1) + " members! We can't play :(")



@bot.command()
async def cmd(ctx):
    await ctx.send("Hello {}! I am the Among Us bot. Tadaaa! You could use me while calling your friends for a game of Among Us! "
                    "But how do you call me? Here's how:\n1. Ask whether your friends are coming to play\n`$Pu call`\n "
                    "The bot would wait for 20 mins for them to join. If it excedes, then it would inform you that there aren't enough members"
                    "\n2. If there are enough members, then you could host the game\n`$Au *GameCode*:*Server*`\nThis would wait for 3 mins "
                    "Then, you could start. Crewmates(or imposters) are supposed to join by reacting to the bot's message".format(ctx.message.author.mention))


bot.run('TOKEN')
