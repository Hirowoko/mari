import os
import discord
from discord.ext import commands
counter_ban_up = -1
counter_ban_down = -1
with open('/home/hiwo/discord_token', 'r') as data:
    token = data.read().strip()

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}!')
#@bot.event 
#async def on_reaction_rem(reaction_rem, user):
#       
@bot.event
async def on_reaction_add(reaction, user):
    counter_up = 1
    counter_down = 1
    print(f"{reaction} from {user}")
    print(int(reaction))
    pass

@bot.command()
async def poll(ctx, user_id,*, question):
    await ctx.channel.purge(limit=1)
    message = await ctx.send(f"{question} - {user_id}: \n✅ = Yes\n❎ = No")
    await message.add_reaction('✅')
    await message.add_reaction('❎')
    

@bot.command()
async def you(ctx):
    await ctx.send("fucker")

bot.run(token)
