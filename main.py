import discord
from discord.ext import commands


import config
import models


TOKEN = config.TOKEN


client = commands.Bot(command_prefix='.')

@client.command(aliases=['createprofile', 'profilecreate'])
async def create_profile(ctx, *, profile):
    author = ctx.message.author
    models.Profile.create(
        username = author,
        profile = profile
    )
    await ctx.send('Your profile has been created')

@client.command(aliases=['editprofile', 'profileedit'])
async def edit_profile(ctx, *, profile):
    author = ctx.message.author
    query = models.Profile.update(profile=profile).where(models.Profile.username == author)
    query.execute()
    await ctx.send('Your profile has been edited')

@client.command(aliases=['deleteprofile', 'profiledelete'])
async def delete_profile(ctx):
    author = ctx.message.author
    query = models.Profile.select().where(models.Profile.username == author).get()
    query.delete_instance()
    await ctx.send('Your profile has been deleted')

@client.command(aliases=['showprofile', 'profiledshow'])
async def show_profile(ctx, *, user):
    profile = models.Profile.select().where(models.Profile.username == user).get()
    embed = discord.Embed(color = discord.Color.blue())
    embed.add_field(
        name=f"{user}'s profile",
        value=profile.profile,
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
    models.initialize()
    client.run(TOKEN)
