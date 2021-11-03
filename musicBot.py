import os
import discord as ds
from discord.ext import commands
import youtube_dl

client = commands.Bot(command_prefix=".")


@client.command()
async def play(ctx, url: str, channel):
    song_there = os.path.isfile("song.mp3")
    try:
        if song_there:
            os.remove("song.mp3")
    except PermissionError:
        await ctx.send("Tunggu lagu ne entek sek jancok! Lek ga yo 'Stop'")
        return

    voiceChannel = ds.utils.get(
        ctx.guild.voice_channels, name=str(channel))
    await voiceChannel.connect()
    voice = ds.utils.get(client.voice_clients, guild=ctx.guild)

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
            os.rename(file, "song.mp3")
    voice.play(ds.FFmpegPCMAudio("song.mp3"))


@client.command()
async def leave(ctx):
    voice = ds.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_connected():
        await voice.disconnect()
    else:
        await ctx.send("Bot e durung konek nek channel bos")


@client.command()
async def resume(ctx):
    voice = ds.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_paused():
        voice.resume()
    else:
        await ctx.send("Sek mlaku lagune...")


@client.command()
async def stop(ctx):
    voice = ds.utils.get(client.voice_clients, guild=ctx.guild)
    voice.stop()

client.run('OTA1MzQ0NzUxMTE5NzczNzM3.YYIuAQ.IwWyZcCOVZvaXepzzV71lLrgyrY')
