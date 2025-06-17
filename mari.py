import os
import discord
from discord.ext import commands
import asyncio
import datetime
global total_member_count

with open('/home/hiwo/discord_token', 'r') as data:
    token = data.read().strip()

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}!')

@bot.command()
async def time(ctx, member: discord.Member):

    mess = await ctx.send(f"- {member}: \n✅ = Yes\n❎ = No")
    await mess.add_reaction('✅')
    await mess.add_reaction('❎')
    await asyncio.sleep(5)
    member_count = len([m for m in ctx.guild.members if not m.bot])
    print(member_count)

    msg = await ctx.channel.fetch_message(mess.id) # 'Cache' the message
    highest_reaction = ""
    highest_reaction_number = 3
    
    for reaction in msg.reactions: # iterate through every reaction in the message
        if (reaction.count-1) >= highest_reaction_number:
            highest_reaction = reaction.emoji
            highest_reaction_count = reaction.count-1
            await ctx.send(f"timeouted {member}!")
            await member.timeout(datetime.timedelta(days=28))
            #await interaction.response.send_message(f'was timeouted until for {duration}', ephemeral=True)


@bot.command()
async def you(ctx):
    await ctx.send("fucker")

bot.run(token)
