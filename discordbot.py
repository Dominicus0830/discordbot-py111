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

class MyModal(ui.Modal, title="π’ κ³΅μ§μ¬ν­"):
    contents = ui.TextInput(label="κ³΅μ§ λ΄μ©", placeholder="λ΄μ©μ μλ ₯νμΈμ.", style=discord.TextStyle.long)
    
    async def on_submit(self, interaction: discord.Interaction):
        embed1 = discord.Embed(title=f"κ³΅μ§κ° μ±κ³΅μ μΌλ‘ λ³΄λ΄μ‘μ΅λλ€.")
        embed1.add_field(name="κ³΅μ§λ΄μ©", value=f"{self.contents}")
        await interaction.response.send_message(embed=embed1)

        channel = interaction.guild.get_channel(μ±λμμ΄λ) #κ³΅μ§κ° μ¬λΌμ¬ μ±λ
        embed = discord.Embed(title = f"``π’`` **κ³΅μ§μ¬ν­** ``π’``" , description = f"**{self.contents}**", color = 0xfff2cc, timestamp = datetime.datetime.now())
        embed.set_thumbnail(url=interaction.guild.icon)
        await channel.send(f"@everyone", embed=embed)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}.')
    print("λ΄μ΄ μΌμ‘μ΅λλ€")
    print("λλ―Έλμ½#8655")
    print("λλ―Έλλ―Έ νλ₯νλ₯")
    await bot.change_presence(status=discord.Status.online, activity=discord.Game("λλ―Έλλ―Έ")) #λ΄μ ~νλμ€ νμ
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
        
@bot.tree.command(name="κ³΅μ§")
async def notice(interaction: discord.Interaction):
    await interaction.response.send_modal(MyModal())

try:
    client.run(TOKEN)
except discord.errors.LoginFailure as e:
    print("Improper token has been passed.")
