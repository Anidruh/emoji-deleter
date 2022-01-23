import discord
from discord.ext import commands
import asyncio

client = commands.Bot(command_prefix = emoji)

@client.command(aliases=['delemoji'])
@commands.has_permissions(manage_emojis=True)
@commands.cooldown(2,10,commands.BucketType.guild)
async def deleteemoji(ctx, emoji: discord.Emoji):
	guild = ctx.guild
	if ctx.author.guild_permissions.manage_emojis:
		await ctx.send(f'Successfully deleted (or not): {emoji}')
		await emoji.delete()

@client.event
async def on_ready():    

    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=f"{len(client.guilds)} servers | and what"))

    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="emojis yes"))

    await client.change_presence(activity=discord.Game(name="lol"))

    print("Bot is ready")


async def ch_pr():
    await client.wait_until_ready()

    statuses = ["lol", f"{len(client.guilds)} servers | and what", "emojis yes"] 

    while not client.is_closed():

        status = random.choice(statuses)

        await client.change_presence(activity=discord.Game(name=status))

        await asyncio.sleep(10)


client.loop.create_task(ch_pr())

client.run("TOKEN")
