import discord
from discord.ext import commands
import re
from datetime import timedelta
import traceback
import os
from random import choice, randint
import aiohttp

merda = [ 'seu merda', 'SEU MERDA', 'SEU MERDINHA', 'SEU MERDAO', 'seu merdao' ]

owner = ["419959252292075524D"]

bot = commands.Bot(command_prefix='!', description="Pois e.. Sabe nao cabaco?")

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    print(discord.utils.oauth_url(bot.user.id))
    await bot.change_presence(game=discord.Game(name="A Zoeira pela janela", url="twitch.tv/alanzoka", type=1))

@bot.event
async def on_message(message):
    if message.content.startswith('qual e a melhor musica'):
        await bot.send_message(message.channel, 'Pacificadores - Eu queria mudar BASS BOOSTED HARD BASS RUSSIAN CARALHO CRAZY FUCKING VAPE ULTRA MEGA BLASTER EXTRA TRICKS')
    if message.content.startswith('ddos'):
        await bot.send_message(message.channel, 'ME DA DDOS ENTAO ;3')
    if message.content.startswith('DDOS'):
        await bot.send_message(message.channel, 'ME DA DDOS ENTAO SEU LIXO DA CARALHO')
    if message.content.startswith('cuzao'):
        await bot.send_message(message.channel, 'CUZAO E VC SEU MERDA')
    if message.content.startswith('CUZAO'):
        await bot.send_message(message.channel, 'CUZAO E VC SEU MERDA LIXO COMEDOR DE BOLAS')
    if message.content.startswith('lixo'):
        await bot.send_message(message.channel, 'LIXAO E VC SEU LIXO JOGADOR DE MAINIGRAVIUTY')
    if message.content.startswith('LIXO'):
        await bot.send_message(message.channel, 'LIXAO E VC SEU LIXO JOGADOR DE MAINIGRAVIUTY SEU MERDA DO CARALHO SEM MAE')
    if message.content.startswith('tudo bom'):
        await bot.send_message(message.channel, 'Tudo e voce :3')
    if message.content.startswith('seu merda'):
        await bot.send_message(message.channel, 'MERDA FOI QUEM TE FEZ PAU NO CU')
    if message.content.startswith('SEU MERDA'):
        await bot.send_message(message.channel, 'MERDA FOI QUEM TE FEZ PAU NO CU')
    if message.content.startswith('vrau'):
        await bot.send_message(message.channel, 'SENTA NO MEU PAU') 
    if message.content.startswith('eae'):
        await bot.send_message(message.channel, 'Eae como oc ta')
    if message.content.startswith('qual foi'):
        await bot.send_message(message.channel, 'eu queria mudar')
    if message.content.startswith('FDP'):
        await bot.send_message(message.channel, 'FdP E VC SEU LIXO')
    if message.content.startswith('fdp'):
        await bot.send_message(message.channel, 'FdP E VC SEU LIXO')
    if message.content.startswith('JOGO MINECRAFT'):
        await bot.send_message(message.channel, 'KID')
    if message.content.startswith('inutil'):
        await bot.send_message(message.channel, 'INUTIL E VC')
    if message.content.startswith('clb'):
        await bot.send_message(message.channel, 'VEM CALAR')
    if message.content.startswith('CLB'):
        await bot.send_message(message.channel, 'VEM CALAR')
    if message.content.startswith('VAI TOMA NO SEU CU'):
        await bot.send_message(message.channel, 'QUEM VAI TOMAR NO MEU CU EIN?')
    if message.content.startswith('vai toma no seu cu'):
        await bot.send_message(message.channel, 'QUEM VAI TOMAR NO MEU CU EIN?')
    if message.content.startswith('SEU MERDA', merda):
        await bot.send_message(message.channel, 'MERDA E VC SEU LIXO DO CARALHO')
    if message.content.startswith('VC E CORNO'):
        await bot.send_message(message.channel, 'CUCK E TEU PAI <#')
    if message.content.startswith('vc e corno'):
        await bot.send_message(message.channel, 'CUCK E TEU PAI <#')

bot.run('NDM1ODQ2MzY0NzE5NDgwODMz.Dbe5og.j3MYEhtKUMqCreYnsAtpO2775_I')