import discord

client = discord.Client()


@client.event
async def on_message(message):
    message.content = message.content.lower()
    if message.author == client.user:
        return
    
    # English
    if message.content.startswith("studybot.help"):
        await message.channel.send("Hello! I am Study Bot\nCOMMANDS:\n<subject>.cycle test\n<subject>.midterm\n<subject>.term exam\n<subject>.portions")

    if message.content.startswith("english.cycle test"):
        await message.channel.send("What's the hurry? No test is scheduled. Please don't be a padipaali. Have patience")

    if message.content.startswith("english.midterm"):
        await message.channel.send("What's the hurry? No test is scheduled. Please don't be a padipaali. Have patience")

    if message.content.startswith("english.term exam"):
        await message.channel.send("What's the hurry? No test is scheduled. Please don't be a padipaali. Have patience")

    if message.content.startswith("english.portions"):
        await message.channel.send("No test is going on")

    # Computer Science
    if message.content.startswith("cs.cycle test"):
        await message.channel.send("What's the hurry? No test is scheduled. Please don't be a padipaali. Have patience")

    if message.content.startswith("cs.midterm"):
        await message.channel.send("What's the hurry? No test is scheduled. Please don't be a padipaali. Have patience")

    if message.content.startswith("cs.term exam"):
        await message.channel.send("What's the hurry? No test is scheduled. Please don't be a padipaali. Have patience")

    if message.content.startswith("cs.portions"):
        await message.channel.send("No test is going on")

    # Chemistry
    if message.content.startswith("chemistry.cycle test"):
        await message.channel.send("What's the hurry? No test is scheduled. Please don't be a padipaali. Have patience")

    if message.content.startswith("chemistry.midterm"):
        await message.channel.send("What's the hurry? No test is scheduled. Please don't be a padipaali. Have patience")

    if message.content.startswith("chemistry.term exam"):
        await message.channel.send("What's the hurry? No test is scheduled. Please don't be a padipaali. Have patience")

    if message.content.startswith("chemistry.portions"):
        await message.channel.send("No test is going on")

    # Mathematics
    if message.content.startswith("math.cycle test"):
        await message.channel.send("What's the hurry? No test is scheduled. Please don't be a padipaali. Have patience")

    if message.content.startswith("math.midterm"):
        await message.channel.send("What's the hurry? No test is scheduled. Please don't be a padipaali. Have patience")

    if message.content.startswith("math.term exam"):
        await message.channel.send("What's the hurry? No test is scheduled. Please don't be a padipaali. Have patience")

    if message.content.startswith("math.portions"):
        await message.channel.send("No test is going on")

    # Physics
    if message.content.startswith("physics.cycle test"):
        await message.channel.send("What's the hurry? No test is scheduled. Please don't be a padipaali. Have patience")

    if message.content.startswith("physics.midterm"):
        await message.channel.send("What's the hurry? No test is scheduled. Please don't be a padipaali. Have patience")

    if message.content.startswith("physics.term exam"):
        await message.channel.send("What's the hurry? No test is scheduled. Please don't be a padipaali. Have patience")

    if message.content.startswith("physics.portions"):
        await message.channel.send("What's the hurry? No test is scheduled. Please don't be a padipaali. Have patience")


client.run('TOKEN')
