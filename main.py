import discord
from discord.ext import commands
import asyncio
from itertools import cycle

import config
import models

TOKEN = config.TOKEN


client = discord.Client()
bot = commands.Bot(command_prefix='.')

@bot.command(pass_context=True, name='createprofile')
async def create_profile(ctx, profile):
    author = ctx.message.author
    models.Profile.create(
        username = author,
        profile = profile
    )
    await ctx.send('Your profile has been created')

@bot.command(pass_context=True)
async def showprofile(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        title = 'Title',
        description = 'This is a description',
        color = discord.Color.blue()
    )

    embed.set_footer(text='This is a footer.')
    #embed.set_image(url='')
    #embed.set_thumbnail(url='')
    embed.set_author(name='Author Name', icon_url='')
    embed.add_field(
        name='Field Name',
        value='Description',
        inline='True'
    )
    await client.send()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
