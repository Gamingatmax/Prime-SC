import discord
from discord import Game
from discord.ext import commands
from discord.ext.commands import Bot
from discord.voice_client import VoiceClient
import time
import asyncio
import aiofortnite
import os
import json
import requests
from PIL import Image, ImageDraw, ImageFont
from pyfiglet import figlet_format
import subprocess
import sys, traceback
import discord.opus

bot = commands.Bot(command_prefix='>')

@bot.command()
async def servercreate(ctx):
    guild = ctx.message.guild
    overwrites = {
        guild.default_role: discord.PermissionOverwrite(manage_roles=False, kick_members=False, ban_members=False, administrator=False, manage_channels=False, manage_guild=False, add_reactions=True, view_audit_log=False, read_messages=True, send_messages=False, manage_messages=False, read_message_history=True, mention_everyone=False, external_emojis=True, manage_nicknames=False, speak=False, mute_members=False, ),
        guild.me: discord.PermissionOverwrite(read_messages=True)
    }
    catergory1 = await guild.create_category('SERVER', overwrites=overwrites)
    channel1 = await guild.create_text_channel('welcome', category=catergory1, overwrites=overwrites)
    channel2 = await guild.create_text_channel('Annoucements', category=catergory1, overwrites=overwrites)
    channel3 = await guild.create_text_channel('Rules', category=catergory1, overwrites=overwrites)

    catergory2 = await guild.create_category('General')
    channel4 = await guild.create_text_channel('General', category=catergory2)
    channel5 = await guild.create_text_channel('Bot Room', category=catergory2)

    catergory3 = await guild.create_category('💬Chat')
    channel6 = await guild.create_voice_channel('💬Chat 1', category=catergory3)
    channel7 = await guild.create_voice_channel('💬Chat 2', category=catergory3)
    channel8 = await guild.create_voice_channel('💬Chat 3', category=catergory3)
    catergory4 = await guild.create_category('🎮 GAMES')
    channel10 = await guild.create_voice_channel('🎮 CALL OF DUTY', category=catergory4)
    channel11 = await guild.create_voice_channel('🎮 FORTNITE', category=catergory4)
    channel12 = await guild.create_voice_channel('🎮 PUBG', category=catergory4)
    channel13 = await guild.create_voice_channel('🎮 WOW', category=catergory4)
    channel14 = await guild.create_voice_channel('🎮 CSGO', category=catergory4)
    catergory5 = await guild.create_category('🎶Music')
    channel15 = await guild.create_voice_channel('🎶Rythm', category=catergory5)
    channel16 = await guild.create_voice_channel('🎶FredBoat', category=catergory5)
    channel17 = await guild.create_voice_channel('🎶DabBot', category=catergory5)
    catergory6 = await guild.create_category('💤 AFK')
    channel18 = await guild.create_voice_channel('💤AFK', category=catergory6)
    await guild.edit(afk_channel=channel18)
    await ctx.send("Server Creation Complete. You can now kick me :D")

@bot.event
async def on_guild_join(guild):
    ch = guild.text_channels[0]
    embed = discord.Embed(title="Hello!", description="Hiya im Prime SC which is my bot recreated for one sole purpose... to create a nice and clean server for your needs", color=0xd4183b)
    embed.add_field(name="Why?", value="Why you ask? I was just so annoyed at having to setup servers over and over and over again so i was like hey let me just make a bot for it and then it turned into this", inline=False)
    embed.add_field(name="Something you should know...", value="I made this whilst i had to do my science homework but to be honest i couldnt be bothered so i spent the next two hours making this", inline=False)
    embed.add_field(name="Setup:", value="You just type in >servercreate into the chat and the bot should do its magic. If there are any bugs please contact me at zomboid333@gmail.com. I would also suggest adding Rythm bot, Fredboat bot and dabbot. Also give prime role all permissions and drag his role to the top", inline=False)
    embed.add_field(name="Special Thx You", value="And finally a special thank you to the people in the official discord.py server if it wasnt for them i wouldnt be able to make this because i am bad at understanding the docs", inline=False)
    embed.set_footer(icon_url="https://cdn.discordapp.com/avatars/428597692617326593/26e04115a38a65f2d6d568b194216948.webp?size=1024", text="gamingatmax#4204  •  01/07/2018")
    await ch.send(embed=embed)






print(discord.__version__)
bot.run('NDYzMzg4ODgzNjExMjg3NTgy.DhvtUw.jz1nJo5KvhWxmNi9DFhdKpwc018')
