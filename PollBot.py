import discord
import os
import random
import string
from discord.ext import commands

PREFIX = "poll."
bot = commands.Bot(command_prefix=PREFIX)
client = discord.Client()

Options = []
Msg = []
Urgent_message = []


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
async def hello(ctx):
    await ctx.send("`Is my name a joke to you?`")


@bot.command()
async def create(ctx, *args):
    global poll
    poll = "POLL: " + ' '.join(args)
    Options.clear()
    await ctx.send("Done")


@bot.command()
async def add(ctx, *args):
    arg = ' '.join(args)
    Options.append(arg)
    await ctx.send("Done")


@bot.command()
async def start(ctx):
    global msg_sent, call_msg, react_msg, Reaction_list
    Reactions = 0
    Reaction_list = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣", "9️⃣", "🔟"]

    if os.path.exists("MessageID.txt"):
        msg_file = open("MessageID.txt", "w")
    else:
        msg_file = open("MessageID.txt", "w+")

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
        call_msg = await PollChannel.send(Role_id + " " + poll)
        for i in range(int(len(Options))):
            Reactions += 1
            msg_sent = await PollChannel.send(str(i + 1) + ". " + Options[i])
            Msg.append(msg_sent)

        react_msg = await PollChannel.send("React to the message according to the number to cast your poll")

        for j in range(Reactions):
            await react_msg.add_reaction(Reaction_list[j])

        msg_file.write(str(react_msg.id))

    except NameError:
        await ctx.send("Please create the poll first")


@bot.command()
async def urgent(ctx, *args):
    global urg_call_msg, urg_option_msg, urg_msg, urg_count
    if os.path.exists("MessageID.txt"):
        msg_file = open("MessageID.txt", "a")
    else:
        msg_file = open("MessageID.txt", "w+")
    Line = ' '.join(args)
    urg_reactions = 0
    urg_reaction_list = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣", "9️⃣", "🔟"]
    urg_poll, *urg_options = Line.split("&")
    urg_call_msg = await ctx.send("Urgent poll: " + str(urg_poll))

    for i in range(len(urg_options)):
        urg_reactions += 1
        urg_option_msg = await ctx.send("Urgent Option " + str(i + 1) + ": " + str(urg_options[i]))
        Urgent_message.append(urg_option_msg)

    urg_msg = await ctx.send(
        "Please react to the message to according to the option number to cast your poll. (Its urgent it seems)")

    y = ''
    for i in range(1, 3):
        x = random.choice(string.ascii_letters)
        y += x

    msg_file.write(y + ":" + str(urg_msg.id) + "\n")

    urg_count = 0
    for j in range(urg_reactions):
        await urg_msg.add_reaction(urg_reaction_list[j])
        urg_count += 1


@bot.command()
async def delete(ctx):
    try:
        await call_msg.delete()
        for d in range(int(len(Msg))):
            delete_msg = await ctx.fetch_message(Msg[d].id)
            await delete_msg.delete()
        await react_msg.delete()
        await ctx.send("Done")
    except NameError:
        await urg_call_msg.delete()
        for d in range(int(len(Urgent_message))):
            delete_msg = await ctx.fetch_message(Urgent_message[d].id)
            await delete_msg.delete()
        await urg_msg.delete()
        await ctx.send("Done")


@bot.command()
async def result(ctx, arg):
    try:
        d = {}
        with open('MessageID.txt') as poll_file:
            for line in poll_file:
                (key, value) = line.rstrip("\n").split(":")
                d[key] = value

            print(d.keys())

            if str(arg) in d.keys():
                poll_id = d[str(arg)]
                poll_msg = await ctx.fetch_message(poll_id)

                emojis = {}
                for i in poll_msg.reactions:
                    emojis[f'{i}'] = i.count
                emojis = {k: v for k, v in sorted(emojis.items(), key=lambda x: x[1], reverse=True)}

                key = list(emojis.keys())[0]

                values = []
                count = 0

                for i in emojis.values():
                    if emojis[key] == i:
                        values.append(list(emojis.keys())[count])
                    count += 1

                if len(values) == 1:
                    await ctx.send(f'{key} has the highest reactions: {emojis[key]}')
                else:
                    await ctx.send(str(values) + " are tied")

                reaction_count = sum([i.count for i in poll_msg.reactions])
                await ctx.send("Total number of reactions: " + str(reaction_count - urg_count))

            else:
                await ctx.send("Please choose a valid poll")
    except FileNotFoundError:
        await ctx.send("Please create the poll first")


@bot.command()
async def List(ctx):
    with open("MessageID.txt") as file1:
        lines = file1.readlines()
        new_lines = [x[:-1] for x in lines]
        await ctx.send('`\n`'.join(map(str, new_lines)))

    file1.close()


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


bot.run('NzcwODk1MjI5NDg1MTg3MDgz.X5kOIQ.CFttl7NlhhdzCu2kOkBlARjKoV0')
