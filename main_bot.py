import discord
from discord.ext import commands
import random, os, requests
from model import get_class

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def checkAI(ctx):
    if ctx.message.attachments:
        for file in ctx.message.attachments:
            namafile = file.filename
            urlfile = file.url
            await file.save(f'./{namafile}')
            await ctx.send(f'gambar telah disimpan dengan nama {namafile}')

            kelas, skor = get_class('keras_model.h5', 'labels.txt', namafile)
            
            if kelas == 'Mobil Sedan\n' and skor >= 0.75:
                await ctx.send('Ini adalah mobil sedan')
                await ctx.send('ini adalah jenis mobil penumpang yang memiliki bodi yang lebih rendah dan panjang dibandingkan dengan SUV')

            if kelas == 'Mobil SUV\n' and skor >= 0.75:
                await ctx.send('Ini adalah mobil suv')
                await ctx.send('SUV (Sport Utility Vehicle) adalah jenis mobil yang mengkombinasikan dua tipe mobil yakni tipe penumpang dan off-road.')
            else:
                await ctx.send('KYKNYA INI BUKAN TIPE MOBIL SUV ATAU SEDAN')
    else:
        await ctx.send('mana nih gambarnya coyy???')


bot.run("TOKEN")