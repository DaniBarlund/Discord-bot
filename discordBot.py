import discord
import os
import subprocess
import psutil
import random
from discord.ui import Button, View
from discord.ext import commands

def bot():
    intents = discord.Intents.all()
    TOKEN = ''
    filePath = ''
    bot = commands.Bot(command_prefix = '!', intents=intents)
    
    emoji = None
    class myButton(Button):
        def __init__(self,label,style,emoji=None):
            super().__init__(label=label, style=style, emoji=emoji)
            
    
    @bot.event
    async def on_ready():
        print('updated bot is running')
        
        
        
    #----------COMMANDS-----------    
    @bot.command()
    async def Help(ctx):
        await ctx.send('Use command !server to use server related commands.')
        
    @bot.command()    
    async def server(ctx):
        buttonOpen = myButton(label='OPEN', style=discord.ButtonStyle.green, emoji='🎮')
        buttonClose = myButton(label='CLOSE', style=discord.ButtonStyle.red, emoji='🔒')
        buttonStatus = myButton(label='STATUS', style=discord.ButtonStyle.grey, emoji='🖥')
        
        async def buttonOpen_callback(interaction):
            openServer()
            await interaction.response.edit_message(content='Server is now open!', view=None)

        async def buttonClose_callback(interaction):
            closeServer()
            await interaction.response.edit_message(content='Server is now closed!', view=None)
            
        async def buttonStatus_callback(interaction):
            content = serverStatus()
            await interaction.response.send_message(content)
            
        
        buttonOpen.callback = buttonOpen_callback
        buttonClose.callback = buttonClose_callback
        buttonStatus.callback = buttonStatus_callback
            
        view = View()
        view.add_item(buttonOpen)
        view.add_item(buttonClose)
        view.add_item(buttonStatus)
        
        await ctx.send('Select wanted function', view=view)
        
    @bot.command()
    async def coinflip(ctx, bet=None):
        #Function to choose if it's heads or tails: 0 is heads and 1 is tails
        answer = random.randint(0, 1)
        
        #Buttons
        buttonHeads = myButton(label='HEADS', style=discord.ButtonStyle.green, emoji="🤑")
        buttonTails = myButton(label='TAILS', style=discord.ButtonStyle.grey, emoji="🐈")
        
        
        async def buttonHeads_callback(interaction):
            content = coinFlip(0, answer, bet)
            await interaction.response.edit_message(content=content, view=None)
            
        async def buttonTails_callback(interaction):
            content = coinFlip(1, answer, bet)
            await interaction.response.edit_message(content=content, view=None)
            
        buttonHeads.callback = buttonHeads_callback
        buttonTails.callback = buttonTails_callback
        
        view = View()
        view.add_item(buttonHeads)
        view.add_item(buttonTails)
        await ctx.send('Take your guess!', view=view)
        
    @bot.command()
    async def rps(ctx):
        id1 = command.author.id
        print(id1)
        await message.channel.send(id1)
            
    
    bot.run(TOKEN)
    
    
#----------FUNCTIONS-----------
def coinFlip(guess, answer, bet=None):
    if guess==answer:
        return 'You won!'
    else:
        return 'You lost'

def openServer():
    os.chdir(filePath)
    os.startfile(progName)
    
def closeServer():
    os.system("taskkill /f /im valheim_server.exe")
    
def serverStatus():
    if "valheim_server.exe" in (p.name() for p in psutil.process_iter()):
        return 'Server is open.'
    else:
        return 'Server is closed.'

if __name__ == '__main__':
    bot()
