# This example requires the 'message_content' intent.
import os
import discord
from discord.ext import commands
with open('/home/hiwo/discord_token', 'r') as data:
    contents = data.read()

    


class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

open ('/home/hiwo/discord_token')
intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(contents)

bot = commands.Bot(command_prefix='$', intents=intents)
@bot.command()
async def test(ctx, arg):
    await ctx.send(arg)

@bot.command()
async def you(ctx):
    ctx.send("fucker")
    print("it worked")

@bot.command(name='list')
async def _list(ctx, arg):
    pass

