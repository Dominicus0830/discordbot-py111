from cmath import log
from distutils.sysconfig import PREFIX
import discord
from dotenv import load_dotenv
import os
load_dotenv()
from discord.ext import commands
from discord import app_commands, ui
import datetime

PREFIX = os.environ['PREFIX']
TOKEN = os.environ['TOKEN']

client = discord.Client()

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

class MyModal(ui.Modal, title="📢 공지사항"):
    contents = ui.TextInput(label="공지 내용", placeholder="내용을 입력하세요.", style=discord.TextStyle.long)
    
    async def on_submit(self, interaction: discord.Interaction):
        embed1 = discord.Embed(title=f"공지가 성공적으로 보내졌습니다.")
        embed1.add_field(name="공지내용", value=f"{self.contents}")
        await interaction.response.send_message(embed=embed1)

        channel = interaction.guild.get_channel(채널아이디) #공지가 올라올 채널
        embed = discord.Embed(title = f"``📢`` **공지사항** ``📢``" , description = f"**{self.contents}**", color = 0xfff2cc, timestamp = datetime.datetime.now())
        embed.set_thumbnail(url=interaction.guild.icon)
        await channel.send(f"@everyone", embed=embed)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}.')
    print("봇이 켜졌습니다")
    print("도미니코#8655")
    print("도미도미 팔닥팔닥")
    await bot.change_presence(status=discord.Status.online, activity=discord.Game("도미도미")) #봇의 ~하는중 표시
    await bot.tree.sync()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == f'{PREFIX}call':
        await message.channel.send("callback!")

    if message.content.startswith(f'{PREFIX}hello'):
        await message.channel.send('Hello!')

bot.run(TOKEN)        
        
@bot.tree.command(name="공지")
async def notice(interaction: discord.Interaction):
    await interaction.response.send_modal(MyModal())

try:
    client.run(TOKEN)
except discord.errors.LoginFailure as e:
    print("Improper token has been passed.")
