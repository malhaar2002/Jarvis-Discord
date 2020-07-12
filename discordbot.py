import discord
from discord.ext import commands, tasks
from googlesearch import search
import random
import youtube_dl
import os
from discord.utils import get
from discord import FFmpegPCMAudio
from os import system
from gtts import gTTS
import playsound


token = "*********"

client = commands.Bot(command_prefix = "", case_insensitive = True)

member_list = ["Malheur#9174", "Yss#1678", "Zeus#2534", "rishitgupta#6858", "Yash Vasdev#2009", "OrangeSannin0811#5360", "OrangeSannin#4069", "nandos#2619", "#RoboticToast#0001", "CosJune#8466", "niRRu#6437"]

@client.event
async def on_ready():
    print("Ready, sir.")

@client.command()
async def jarvis(ctx):
    await ctx.send("Hey there, I'm Jarvis.\nI'm a bot who was made by Malhaar to satisfy your meme needs, because baaki needs toh tumaari puri hone se rahi.\nTry typing 8ball and a yes or no question.\nType clear and a number and I will delete that number of messages (I know, I have more power than y'all do)\nTry typing bruh\nIf any of my words ever offend you, they are working correctly!")

@client.command()
async def ping(ctx):
    await ctx.send(f"Pong! {round(client.latency * 1000)}ms")

@client.command(aliases = ['8ball'])
async def _8ball(ctx, *, question):
     responses = ["Most certainly.", "Lmao no", "Duhh", "You may not wanna hear the answer", "Maybeee", "You think?", "Obviously", "Uhh...sure!", "For sure", "My sources say yeah, but they also said lockdown would get over by May", "Don't count on it", "You can count on it", "That's a dumb question, don't you think?", "In your dreams", "Yeah and I'm the pope", "YESSS", "Not a doubt", "Decidedly so", "You wish", "Sure why not", "You need to ask?!", "The odds aren't good", "Bet on it", "I think you already know.", "I don't wanna be the one to tell you.", "Outlook not so good", "Definitely!", "Not in a million years.", "HAHAHAHA Now ask a real question", "Oh dear god NO", "Totally", "You gotta be kidding me", "I mean....", "HELL YEAH", "I think so"]
     await ctx.send(f"{random.choice(responses)}")

@client.command()
async def clear(ctx, amount = 5):
    await ctx.channel.purge(limit = amount+1)

@client.command(aliases = ['Who made you', 'Who created you', 'creator?'])
async def creator(ctx):
    await ctx.send("God.\nJust kidding, it's Malhaar.")

@client.command()
async def bruh(ctx):
    bruh_responses = [r"C:\Users\Malhaar\Desktop\Python Projects\Discord bot\Images\giphy.gif", r"C:\Users\Malhaar\Desktop\Python Projects\Discord bot\Images\tenor.gif", r"C:\Users\Malhaar\Desktop\Python Projects\Discord bot\Images\noice.jpg", r"C:\Users\Malhaar\Desktop\Python Projects\Discord bot\Images\tenor (1).gif"]
    with open(random.choice(bruh_responses), 'rb') as f:
        picture = discord.File(f)
        await ctx.send(file = picture)

@client.command(aliases = ["nice"])
async def noice(ctx):
    with open(r"C:\Users\Malhaar\Desktop\Python Projects\Discord bot\Images\noicejake.png", 'rb') as f:
        picture = discord.File(f)
        await ctx.send(file = picture)

@client.command()
async def bye(ctx):
    with open(r"C:\Users\Malhaar\Desktop\Python Projects\Discord bot\Images\tussinajao.gif", 'rb') as f:
        picture = discord.File(f)
        await ctx.send(file = picture)

@client.command(aliases = ['dayum', "damn!", "dayum!", "savage"])
async def damn(ctx):
    with open(r"C:\Users\Malhaar\Desktop\Python Projects\Discord bot\Images\damn-son.jpg", 'rb') as f:
        picture = discord.File(f)
        await ctx.send(file = picture)

@client.command(aliases = ['outstanding'])
async def genius(ctx):
    bruh_responses = [r"C:\Users\Malhaar\Desktop\Python Projects\Discord bot\Images\iit.jpg", r"C:\Users\Malhaar\Desktop\Python Projects\Discord bot\Images\waysofscience.png", r"C:\Users\Malhaar\Desktop\Python Projects\Discord bot\Images\outstandingmove.png", r"C:\Users\Malhaar\Desktop\Python Projects\Discord bot\Images\geniusfrightening.png"]
    with open(random.choice(bruh_responses), 'rb') as f:
        picture = discord.File(f)
        await ctx.send(file = picture)

@client.command(aliases = ["bhenchod", "mdrchd", "maadarchod", "bhosadike", "bsdke", "chutiya", "hutiya"])
async def behenchod(ctx):
    await ctx.send("OYE GAAL NI KADNI\nJust kidding, fire away.")

@client.command(aliases = ["fortnite?"])
async def fortnite(ctx):
    await ctx.send("Kabhi padh bhi liya kar")

@client.command(aliases = ["chemistry"])
async def chem(ctx):
    await ctx.send("Did someone just mention the worst subject ever?")

@client.command(aliases = ["thank", "thanks!"])
async def thanks(ctx):
    await ctx.send("You're welcome.")

@client.command()
async def kill(ctx):
    await ctx.send("Gladly.")

@client.command()
async def f(ctx):
    with open(r"C:\Users\Malhaar\Desktop\Python Projects\Discord bot\Images\f.gif", 'rb') as f:
        picture = discord.File(f)
        await ctx.send(file = picture)

@client.command()
async def google(ctx, *, question):
    global links
    links = []
    query = question
    for j in search(query, tld="co.in", num=10, stop=3, pause=2):
        await ctx.send(j)
        links.append(j)

@client.command()
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()


@client.command()
async def leave(ctx):
    await ctx.voice_client.disconnect()

@client.command()
async def playno(ctx, linkno: int):
    if linkno == 1:
        await play(ctx, links[0])
    elif linkno == 2:
        await play(ctx, links[1])
    elif linkno == 3:
        await play(ctx, links[2])
    else:
        await ctx.send("Enter 1, 2 or 3 according to your choice number")

@client.command(pass_context=True, brief="This will play a song 'play [url]'")
async def play(ctx, url: str):
    channel = ctx.author.voice.channel
    await channel.connect()
    song_there = os.path.isfile("song.mp3")
    try:
        if song_there:
            os.remove("song.mp3")
    except PermissionError:
        await ctx.send("Wait for the current playing music end or use the 'stop' command")
        return
    await ctx.send("Getting everything ready, playing audio soon")
    print("Someone wants to play music let me get that ready for them...")
    global voice
    voice = get(client.voice_clients, guild=ctx.guild)
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            os.rename(file, 'song.mp3')
    voice.play(discord.FFmpegPCMAudio("song.mp3"))
    voice.volume = 100
    voice.is_playing()

@client.command()
async def pause(ctx):
    voice.pause()

@client.command(aliases = ['continue'])
async def resume(ctx):
    voice.resume()

@client.command()
async def stop(ctx):
    voice.stop()

@client.command()
async def volume(ctx, *, volume):
    voice.source = discord.PCMVolumeTransformer(voice.source)
    voice.source.volume = float(volume)

@client.command()
async def speak(ctx, *, message: str, file = "ques.mp3"):
    tts = gTTS(text = message, lang = "sv")
    filename = file
    tts.save(filename)
    await join(ctx)
    voice = get(client.voice_clients, guild=ctx.guild)
    voice.play(discord.FFmpegPCMAudio(filename))
    voice.volume = 100
    voice.is_playing()

@client.command()
async def message_count(ctx, channel: discord.TextChannel=None):

    channel = channel or ctx.channel

    malhaar = 0
    chibu = 0
    vibhu = 0
    rishit = 0
    vasdev = 0
    rushil = 0

    count = 0
    async for message in channel.history(limit= 10):
        await ctx.send(message.author)
        if message.author == "Malheur":
            malhaar += 1
        elif message.author == "Yss#1678":
            chibu += 1
        elif message.author == "rishitgupta#6858":
            rishit += 1
        elif message.author == "Yash Vasdev#2009":
            vasdev += 1
        elif message.author == "OrangeSannin0811#5360" or message.author == "OrangeSannin#4069":
            rushil += 1
        count += 1

        messagePerPerson = {malhaar: "Malhaar", chibu: "Chibu", vibhu: "Vibhu", rishit: "Rishit", vasdev: "Vasdev", rushil: "Rushil"}

    await ctx.send("There were a total of {} messages in {}".format(count, channel.mention))
    await ctx.send("Number of messages sent by each member:")
    for i in messagePerPerson:
        await ctx.send(f"{messagePerPerson[i]}: {i}\n")
    #await ctx.send(f"Malhaar: {malhaar}\nChibu: {chibu}\nVibhu: {vibhu}\nRishit: {rishit}\nVasdev: {vasdev}\nRushil: {rushil}")
    await ctx.send(f"{messagePerPerson.get(max(messagePerPerson))} sent the max number of messages. Congrats {messagePerPerson.get(max(messagePerPerson))}! You are the Vela-est of the Vele-est Log.")

# Hangman variables
word = ""
guessesLeft = 6
playingHangman = False
blanks = []
guessedLetters=[]
lettersFound = 0

@client.command()
async def hangman(ctx):
    await ctx.send("Assuming and hoping you meant the game and not the death penalty, let's go!")
    global playingHangman, word, guessesLeft, blanks, lettersFound, guessedLetters
    lines = []
    with open("hangmanwords.txt", "r") as f:
        lines = f.readlines()
    random_line_num = random.randrange(0, len(lines))
    word = lines[random_line_num]
    blanks = []
    guessedLetters = []
    lettersFound = 0
    guessesLeft = 6
    playingHangman = True
    for i in range(1, len(word)):
        blanks .append("-")

    await ctx.send("Welcome to Hangman.")
    space = " "
    await ctx.send(f"You have {str(guessesLeft)} guesses to get all of the letters in the word. To guess a letter, type guess letter \n {space.join(blanks)}")

@client.command()
async def guess(ctx, guess):
    global playingHangman
    global word
    global guessesLeft
    global blanks
    global lettersFound
    global guessedLetters
    if playingHangman is True:
        if str.isalpha(guess) and len(guess) is 1 and str.lower(guess) not in guessedLetters:
            if str.lower(guess) in word:
                await ctx.send(guess + " is in the word.  Good job!")
                for i in range(0, len(word)):
                    if word[i] == str.lower(guess):
                        blanks[i] = str.lower(guess)
                        lettersFound += 1

            else:
                await ctx.send(guess + " is NOT in the word.")
                guessesLeft -= 1

            guessedLetters.append(str.lower(guess))
            await ctx.send(" ".join(blanks))
            await ctx.send("Guessed letters: " + " ".join(guessedLetters))
            await ctx.send("Guesses left: " + str(guessesLeft))

            if guessesLeft == 0:
                await ctx.send("No guesses left. You lose!")
                await ctx.send(f"The word was: {word}")
                playingHangman = False
            if lettersFound == len(word)-1:
                await ctx.send("You guessed all the letters! You've won! The word was: " + word)
                playingHangman = False

        else:
            await ctx.send("ERROR: You can only guess with single letters that haven't already been entered.")
            await ctx.send("Guessed letters: " + " ".join(guessedLetters))

    else: await ctx.send("Start a game of Hangman before trying to guess a letter!")


client.run(token)
