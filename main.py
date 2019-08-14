import discord
from discord.ext import commands
import aiosqlite

import config
import models


TOKEN = config.TOKEN

client = commands.Bot(command_prefix='.')

@client.command(aliases=['createprofile', 'profilecreate'])
async def create_profile(ctx, *, profile):
    full_profile = (str(ctx.message.author), profile)
    await models.create(full_profile)
    await ctx.send('Your profile has been created')

@client.command(aliases=['editprofile', 'profileedit'])
async def edit_profile(ctx, *, profile):
    full_profile = (profile, str(ctx.message.author))
    await models.edit(full_profile)
    await ctx.send('Your profile has been edited')

@client.command(aliases=['deleteprofile', 'profiledelete'])
async def delete_profile(ctx):
    author = (str(ctx.message.author),)
    await models.delete(author)
    await ctx.send('Your profile has been deleted')

@client.command(aliases=['showprofile', 'profileshow'])
async def show_profile(ctx, *, user):
    get_user = (user,)
    profile = await models.show(get_user)
    embed = discord.Embed(color = discord.Color.blue())
    embed.add_field(
        name=f"{user}'s profile",
        value=profile,
        inline='True'
    )
    await ctx.send(embed=embed)


@client.command(aliases=['profilehelp'])
async def show_profile(ctx):
    embed = discord.Embed(color = discord.Color.blue())
    embed.add_field(
        name="Functions",
        value=""".createprofile / .profilecreate profile
        example: .profilecreate This is a short blurb about my character
        
        .editprofile / .profileedit profile
        example: .profileedit This is a short blurby blurb about my character
        
        .deleteprofile / .profiledelete
        example: .profiledelete
        
        .showprofile / .profileshow user#id
        example: .profileshow Adam#1234""",
        inline='True'
    )
    await ctx.send(embed=embed)    
    
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

if __name__ == '__main__':
    models.initialize("profiles.sqlite")
    client.run(TOKEN)
