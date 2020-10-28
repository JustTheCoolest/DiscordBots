import discord
from discord.ext import commands

PREFIX = "poll."
bot = commands.Bot(command_prefix=PREFIX)
client = discord.Client()

Options = []

@bot.event
async def on_ready():
    activity = discord.Game(name="Make a Poll {Type $cmd for commands}", type=3)
    await bot.change_presence(status=discord.Status.idle, activity=activity)
    return

@bot.command()
async def create(ctx, *args):
    global poll
    poll = "Poll: " + ' '.join(args)
    await ctx.send("Done")

@bot.command()
async def add(ctx, *args):
    arg = ' '.join(args)
    Options.append(arg)
    await ctx.send("Done")
    

@bot.command()
async def start(ctx):

    if ctx.guild.name == "Let's Rock!":
        channel_id = 770898839473094687
        Role_id = "<@&742616464321937408>"
    elif ctx.guild.name == "BOTLOL":
        channel_id = 762633165080100914
        Role_id = "<@&762632022547628042>"
    else:
        channel_id = 751460282118963201
        Role_id = "<@&757163360541474818>"

    PollChannel = bot.get_channel(channel_id)
    try:
        await PollChannel.send(Role_id + " " + poll)
        for i in range(int(len(Options))):
            msg = await PollChannel.send(str(i + 1) + ". " + Options[i])
            await msg.add_reaction("👍")
            await msg.add_reaction("👎")

    except NameError:
        await ctx.send("Please create the poll first")



bot.run('NzcwODk1MjI5NDg1MTg3MDgz.X5kOIQ.y0eIGVkZuCViyBJildCD8HoxPwo')
