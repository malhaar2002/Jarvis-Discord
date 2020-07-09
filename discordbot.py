import discord
from discord.ext import commands, tasks
from googlesearch import search
import random
import youtube_dl
import os
from discord.utils import get
from discord import FFmpegPCMAudio
from os import system


token = "********"

client = commands.Bot(command_prefix = "", case_insensitive = True)

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
    query = question
    for j in search(query, tld="co.in", num=10, stop=3, pause=2):
        await ctx.send(j)

@client.command()
async def join(ctx):
    channel = ctx.author.voice.channel
    try:
        await channel.connect()
    except:
        await ctx.send("Are you connected to voice channel?")

@client.command()
async def leave(ctx):
    await ctx.voice_client.disconnect()

@client.command(pass_context=True, brief="This will play a song 'play [url]'", aliases=['pl'])
async def play(ctx, url: str):
    channel = ctx.author.voice.channel
    try:
        await channel.connect()
    except:
        await ctx.send("Are you connected to the voice channel?")
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
async def move(ctx,member:discord.Member=None):
    if ctx.author.voice and ctx.author.voice.channel:
        channel = ctx.author.voice.channel
    else:
        await ctx.send("You are not connected to voice!")
    if not member:
        await ctx.send("Who am I trying to move? Use move @user")
    await member.move_to(channel)


client.run(token)
