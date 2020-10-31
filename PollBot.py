import discord
from discord.ext import commands

PREFIX = "poll."
bot = commands.Bot(command_prefix=PREFIX)
client = discord.Client()

Options = []

@bot.event
async def on_ready():
    activity = discord.Game(name="Make a Poll", type=3)
    await bot.change_presence(status=discord.Status.idle, activity=activity)
    return

'''
@bot.command()
async def cmd(ctx):
    await ctx.send("HOW TO START A POLL:")
'''

@bot.command()
async def create(ctx, *args):
    global poll
    poll = "POLL: " + ' '.join(args)
    await ctx.send("Done")

@bot.command()
async def add(ctx, *args):
    arg = ' '.join(args)
    Options.append(arg)
    await ctx.send("Done")
    

@bot.command()
async def start(ctx):
    Reactions = 0
    Reaction_list = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣", "9️⃣", "🔟"]

    if ctx.guild.name == "Let's Rock!":
        channel_id = 770898839473094687
        Role_id = "<@&742616464321937408>"
    elif ctx.guild.name == "BOTLOL":
        channel_id = 762633165080100914
        Role_id = "<@&762632022547628042>"
    else:
        channel_id = 761971712613941268
        Role_id = "<@&742311683585867869>"

    PollChannel = bot.get_channel(channel_id)
    try:
        await PollChannel.send(Role_id + " " + poll)
        for i in range(int(len(Options))):
            Reactions += 1
            await PollChannel.send(str(i + 1) + ". " + Options[i])
            
        msg = await PollChannel.send("React to the message according to the number to cast your poll")

        for j in range(Reactions):
            await msg.add_reaction(Reaction_list[j])

    except NameError:
        await ctx.send("Please create the poll first")




@bot.command()
async def reason(ctx, arg1, arg2):

    if arg2 == "admin":
        role = "<@&675204055810834432>"
        statement = "Being an " + role + ", this is considered a serious crime!"
    if arg2 == "helping-hand":
        role = "<@&675214370346893353>"
        statement = "Being a " + role + ", its a shame on you!"
    if arg2 == "channel-head":
        role = "<@&749856631390732379>"
        statement = "Being a " + role + ", a wrong example is being set to others!"

    if arg1 == "diffmem":
        await ctx.send("According to Rule: 1, adding members who do not belong here is crime! " + statement)



bot.run('TOKEN')
