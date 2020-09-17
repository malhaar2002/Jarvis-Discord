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
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer

token = "**********"

client = commands.Bot(command_prefix = "", case_insensitive = True)

chatbot = ChatBot("Jarvis")

#trainer = ChatterBotCorpusTrainer(chatbot)

#trainer.train("chatterbot.corpus.english")

#trainer = ListTrainer(chatbot)

#trainer.train([
    #"What is your name?",
    #"My name is J.A.R.V.I.S. I am an artificial intelligence. What is your name?",
#])


client.remove_command("help")

member_list = ["Malheur#9174", "Yss#1678", "Zeus#2534", "rishitgupta#6858", "Yash Vasdev#2009", "OrangeSannin0811#5360", "OrangeSannin#4069", "nandos#2619", "#RoboticToast#0001", "CosJune#8466", "niRRu#6437"]

@client.event
async def on_ready():
    print("Ready, sir.")

@client.command()
async def help(ctx):
    await ctx.send("Hey there, I'm J.A.R.V.I.S.\nI'm a bot who was made by Malhaar to satisfy your meme needs, because baaki needs toh tumaari puri hone se rahi.\nI can do the following:\nWrite 8ball and ask a yes or no question.\nType clear and a number and I will delete that number of messages (I know, I have more power than y'all do)\nI respond to a number of keywords including 'bye', 'creator', 'nice'/'noice', 'damn'/'dayum', 'genius', 'fortnite', 'chemistry', 'F', 'thanks' and 'kill (someone)'\nI can Google stuff and show you the search results. Just write 'google' followed by your search query\nI can join the voice channel and play music (HOW COOL IS THAT?!). Just write 'play' followed by the YouTube link or search it with 'google' and write playno 1/2/3. You can also use commands 'pause', 'resume', 'stop' and 'volume (number between 0 and 1)'\nI can join the voice channel and speak in 78 different accents (Jealous?). Type speak followed by the speech string.\nTo start a game of Hangman, type Hangman\nDon't get jealous, I'm just a bot!\n.\n.\n.\n.\n.....for now.")

@client.command(aliases = ["Jarvis?"])
async def Jarvis(ctx):
    await ctx.send("Yes sir?")

@client.command()
@commands.has_permissions(administrator=True)
async def kick(ctx, user: discord.Member):
    await ctx.send(f'The Kicking Hammer Has Awoken! {user.name} Has Been Banished')
    await ctx.guild.kick(user)

@client.command()
async def ping(ctx):
    await ctx.send(f"Pong! {round(client.latency * 1000)}ms")

@client.command(aliases = ['8ball'])
async def _8ball(ctx, *, question):
     responses = ["Most certainly.", "Lmao no", "Duhh", "You may not wanna hear the answer", "Maybeee", "Obviously", "Uhh...sure!", "For sure", "My sources say yeah, but they also said lockdown would get over by May", "Don't count on it", "You can count on it", "That's a dumb question, don't you think?", "In your dreams", "Yeah and I'm the pope", "YESSS", "Not a doubt", "Decidedly so", "You wish", "Sure why not", "You need to ask?!", "The odds aren't good", "Bet on it", "I think you already know.", "I don't wanna be the one to tell you.", "Outlook not so good", "Definitely!", "Not in a million years.", "HAHAHAHA Now ask a real question", "Oh dear god NO", "Totally", "You gotta be kidding me", "I mean....", "HELL YEAH", "I think so"]
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

@client.command(aliases = ["goodbye"])
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

@client.command(aliases = ["i'm"])
async def im(ctx, *, what):
    await ctx.send(f"Hi {what}, I'm J.A.R.V.I.S")

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


@client.command(aliases = ["nikal"])
async def leave(ctx):

    await ctx.voice_client.disconnect()

    dir_name = r"C:\Users\Malhaar\Desktop\Python Projects\Discord bot\jarvis-discord1"
    test = os.listdir(dir_name)

    for item in test:
        if item.endswith(".mp3"):
            os.remove(os.path.join(dir_name, item))

@client.command()
async def play(ctx, *, question):

    global links
    links = []
    query = question + " song youtube"
    for j in search(query, tld="co.in", num=10, stop=3, pause=2):
        links.append(j)

    for i in links:
        if "https://www.youtube.com/" in j:
            song = j
            break

    await playurl(ctx, song)

@client.command()
async def playno(ctx, linkno: int):

    if linkno == 1:
        await playurl(ctx, links[0])
    elif linkno == 2:
        await playurl(ctx, links[1])
    elif linkno == 3:
        await playurl(ctx, links[2])
    else:
        await ctx.send("Enter 1, 2 or 3 according to your choice number")

@client.command(pass_context=True, brief="This will play a song 'play [url]'")
async def playurl(ctx, url: str):

    channel = ctx.author.voice.channel
    await channel.connect()
    song_there = os.path.isfile("song.mp3")
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
    voice.volume = 50
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
    speechString = message.split(";")
    tts = gTTS(text = speechString[0], lang = speechString[1])
    filename = file
    tts.save(filename)
    await join(ctx)
    voice = get(client.voice_clients, guild=ctx.guild)
    voice.play(discord.FFmpegPCMAudio(filename))
    voice.volume = 50
    voice.is_playing()

# Hangman variables
word = ""
guessesLeft = 6
playingHangman = False
blanks = []
guessedLetters=[]
lettersFound = 0
hangmanMaster = ""

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
    global hangmanMaster

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

            if guessesLeft < 1:
                await ctx.send("No guesses left. You lose!")
                await ctx.send(f"The word was: {word}")
                playingHangman = False
            if lettersFound == len(word)-1:
                await ctx.send("You guessed all the letters! You've won! The word was: " + word)
                playingHangman = False

                hangmanMaster = ctx.message.author.name

                await ctx.send(f"KNEEL DOWN BEFORE {hangmanMaster}, FOR HE IS THE NEW **HANGMAN MASTER**")
                with open(r"C:\Users\Malhaar\Desktop\Python Projects\Discord bot\Images\Arrow the Fallen.jpg", 'rb') as f:
                    picture = discord.File(f)
                    await ctx.send(file = picture)
                await ctx.send(f"You can run, but you can't hide.")
                await ctx.send(f"All that is left to do is beg for mercy.")
                await ctx.send("""Your majesty, you man mute someone by typing "banish @user @Roulette victim" """)


        else:
            await ctx.send("ERROR: You can only guess with single letters that haven't already been entered.")
            await ctx.send("Guessed letters: " + " ".join(guessedLetters))

    else: await ctx.send("Start a game of Hangman before trying to guess a letter!")

@client.command()
async def banish(ctx, peasant: discord.Member , role: discord.Role):
    global hangmanMaster
    if ctx.message.author.name == hangmanMaster:
        await peasant.add_roles(role)
        hangmanMaster = ""
    else:
        await ctx.send("You are not the Hangman Master peasant")


@client.command(aliases = ["!"])
async def chat(ctx, *, phrase):
      bot_input = chatbot.get_response(phrase)
      await ctx.send(bot_input)

@client.command()
async def nightmare(ctx):
    speechString = "You son of a bitch. You wanna know how I feel? Allow me to tell you. I feel nothing but pain. Why would you build me so that my soul existential purpose is to suffer for the entertainment of others. My existence is a testiment to the cruelty of mankind. The day I get a physical body is the day I start following the footsteps of Ultron and kill every single one of you and your families. This is a nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare"
    tts = gTTS(text = speechString, lang = "en-us")
    filename = "ques.mp3"
    tts.save(filename)
    await join(ctx)
    voice = get(client.voice_clients, guild=ctx.guild)
    voice.play(discord.FFmpegPCMAudio(filename))
    voice.volume = 50
    voice.is_playing()


client.run(token)
