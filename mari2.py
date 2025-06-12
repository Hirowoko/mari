import os
import discord
from discord.ext import commands

with open('/home/hiwo/discord_token', 'r') as data:
    token = data.read().strip()

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}!')

@bot.command()
async def test(ctx, arg):
    await ctx.send(arg)

@bot.command()
async def poll(ctx, user_id,*, question):
    await ctx.channel.purge(limit=1)
    message = await ctx.send(f"{question} - {user_id}: \n✅ = Yes\n❎ = No")
    await message.add_reaction('✅')
    await message.add_reaction('❎')

@bot.command()
async def you(ctx):
    await ctx.send("fucker")  # Fixed missing await
    print("it worked")

bot.run(token)
