import discord
from discord import Embed
import os
import random
import asyncio
import string
from discord.ext import commands

PREFIX = "poll."
bot = commands.Bot(command_prefix=PREFIX)
client = discord.Client()

Options = []
# Add_count = 0
Msg = []

Urgent_message = []


# started = False


@bot.event
async def on_ready():
    activity = discord.Game(name="Make a Poll", type=3)
    await bot.change_presence(status=discord.Status.idle, activity=activity)
    print("Bot started")
    return


@bot.command()
async def cmd(ctx):
    await ctx.send("HOW TO START A POLL:\nThere are 2 ways:\n1. Cool method:\n => Create the poll `poll.create <topic>`"
                   "\n => Add options `poll.add <option>` [Note that you could add any number of options]\n"
                   "=> Start the poll `poll.start`\n2. Urgent method:\n => Create the poll directly `poll.urgent "
                   "<Topic> & Options` "
                   "[Note that there could me multiple options but should should be separated using '&']")


@bot.command()
async def hello(ctx):
    await ctx.send("`Is my name a joke to you?`")


@bot.command()
async def create(ctx, *args):
    global poll, poll_ended, Add_count, poll_create_id
    Add_count = 0
    poll = "POLL: " + ' '.join(args)
    Options.clear()
    poll_ended = False
    y = ''
    for i in range(1, 3):
        x = random.choice(string.ascii_letters)
        y += x

    poll_create_id = y

    create_msg = "Poll created successfully!" + "\n" + "Poll ID: " + str(poll_create_id)
    embed = discord.Embed(title="Poll List", description=create_msg, color=0xF48D1)
    await ctx.send(embed=embed)


@bot.command()
async def add(ctx, *args):
    global Add_count
    arg = ' '.join(args)
    Add_count += 1
    Options.append(str(Add_count) + ". " + arg)
    await ctx.send("Done")
    if start.has_been_called:
        print("Yes")
        try:
            new_embed = Embed(title='POLL', description=call_msg + "\n" + "\n".join(Options) + "\n" + reaction_to_send,
                              color=0xF48D1)
            await react_msg.edit(embed=new_embed)
            Reactions = int(len(Options))
            count_react = 0
            for j in range(Reactions):
                await react_msg.add_reaction(Reaction_list[j])
                count_react += 1
        except NameError:
            await urg_option_msg.edit(content="\n".join(Options))
            urg_reaction = int(len(Options))
            count_react = 0
            for j in range(urg_reaction):
                await urg_msg.add_reaction(Reaction_list[j])
                count_react += 1


@bot.command()
async def edit(ctx):
    message_sent = await ctx.send("This message is gonna get edited into 'test'")
    await asyncio.sleep(1)
    await message_sent.edit(content="Test")


@bot.command()
async def start(ctx, arg):
    global Started, msg_sent, call_msg, react_msg, Reaction_list, count, total, options_to_send, reaction_to_send
    Started = True
    start.has_been_called = True
    Reactions = 0
    Reaction_list = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣", "9️⃣", "🔟"]

    if os.path.exists("MessageID.txt"):
        msg_file = open("MessageID.txt", "a")
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
    with open('MessageID.txt') as file2:
        o = {}
        for line in file2:
            (key, value) = line.rstrip("\n").split(" : ")
            o[key] = value

        if str(arg) in o.keys():
            print("Yup, it is there")
            await ctx.send("Yo, the poll has already started before")
        else:
            print("Nope, not here")
            try:
                call_msg = Role_id + " " + poll
                # embed = discord.Embed(title="Poll List", description=call_msg, color=0xF48D1)
                # await ctx.send(embed=embed)

                '''
                for i in range(int(len(Options))):
                    Reactions += 1
                    msg_sent = await PollChannel.send(str(i + 1) + ". " + Options[i])
                    Msg.append(msg_sent)
                '''
                Reactions = int(len(Options))
                options_to_send = "\n".join(Options)

                # embed = discord.Embed(title="Poll List", description=options_to_send, color=0xF48D1)
                # msg_sent = await ctx.send(embed=embed)

                reaction_to_send = "React to the message according to the number to cast your poll"
                total = call_msg + "\n" + options_to_send + "''\n" + reaction_to_send
                embed = discord.Embed(title="Poll List", description=total, color=0xF48D1)
                react_msg = await ctx.send(embed=embed)

                count = 0
                for j in range(Reactions):
                    await react_msg.add_reaction(Reaction_list[j])
                    count += 1

                msg_file.write(poll_create_id + " : " + str(react_msg.id) + "\n")

            except NameError:
                await ctx.send("Please create the poll first")


start.has_been_called = False


@bot.command()
async def urgent(ctx, *args):
    global urg_call_msg, urg_option_msg, urg_msg, urg_count
    if os.path.exists("MessageID.txt"):
        msg_file = open("MessageID.txt", "a")
    else:
        msg_file = open("MessageID.txt", "w+")

    Line = ' '.join(args)

    y = ''
    for i in range(1, 3):
        x = random.choice(string.ascii_letters)
        y += x

    urg_reaction_list = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣", "9️⃣", "🔟"]
    urg_poll, *urg_options = Line.split("&")
    urg_call_msg = "Urgent poll: " + str(urg_poll) + "\n" + "Poll ID: " + str(y)

    List1 = []
    urg_reactions = len(urg_options)

    for i in range(len(urg_options)):
        urg_reactions += 1
        List1.append(str(i + 1) + ". " + str(urg_options[i]))

    urg_option_msg = "\n".join(List1)

    urg_msg_send = "Please react to the message to according to the option number to cast your poll. (Its urgent it seems)"

    urg_total = urg_option_msg + "''\n" + urg_msg_send
    embed = discord.Embed(title=urg_call_msg, description=urg_total, color=0xF48D1)
    urg_msg = await ctx.send(embed=embed)

    urg_reactions = int(len(urg_options))
    msg_file.write(y + " : " + str(urg_msg.id) + "\n")

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
                (key, value) = line.rstrip("\n").split(" : ")
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
                    await ctx.send("{} These 2 values are tied".format(values))

                reaction_count = sum([i.count for i in poll_msg.reactions])
                try:
                    await ctx.send("Total number of reactions: " + str(reaction_count - urg_count))
                except NameError:
                    await ctx.send("Total number of reactions: " + str(reaction_count - count))

            else:
                await ctx.send("Please choose a valid poll")
    except FileNotFoundError:
        await ctx.send("Please create the poll first")


@bot.command()
async def List(ctx):
    with open("MessageID.txt") as file1:
        lines = file1.readlines()
        new_lines = [x[:-1] for x in lines]
        list_poll = '\n'.join(map(str, new_lines))
        embed = discord.Embed(title="Poll List", description=list_poll, color=0xF48D1)
        await ctx.send(embed=embed)
        print("Yes")

    file1.close()


bot.run("TOKEN")
