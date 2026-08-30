import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
from datetime import datetime, timedelta

import database

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    database.setup_database()

@bot.command()
async def bounty(ctx):
    user = database.get_user(str(ctx.author.id), str(ctx.author.name))
    balance = user[2]
    await ctx.send(f"{ctx.author.name}, your current bounty is {balance} Berries.")

@bot.command()
async def setsail(ctx):
    user = database.get_user(str(ctx.author.id), str(ctx.author.name))
    last_daily = user[3]

    now = datetime.now()

    if last_daily is not None:
        last_time = datetime.fromisoformat(last_daily)
        if now - last_time < timedelta(hours=24):
            remaining = timedelta(hours=24) - (now - last_time)
            hours = int(remaining.total_seconds() // 3600)
            await ctx.send(f"You've already raided today, Captain. Come back in {hours} hour(s).")
            return

    new_balance = user[2] + 100
    database.update_balance(str(ctx.author.id), new_balance)
    database.update_last_daily(str(ctx.author.id), now.isoformat())

    await ctx.send(f"You raided a merchant ship at dawn and earned 100 Berries! New balance: {new_balance}")

@bot.command()
async def trade(ctx, member: discord.Member, amount: int):
    if amount <= 0:
        await ctx.send("You must trade a positive amount of Berries.")
        return

    sender = database.get_user(str(ctx.author.id), str(ctx.author.name))
    receiver = database.get_user(str(member.id), str(member.name))

    if sender[2] < amount:
        await ctx.send("You don't have enough Berries for this trade.")
        return

    database.update_balance(str(ctx.author.id), sender[2] - amount)
    database.update_balance(str(member.id), receiver[2] + amount)

    await ctx.send(f"{ctx.author.name} traded {amount} Berries to {member.name}.")

@bot.command()
async def worstgeneration(ctx):
    top_users = database.get_top_users(5)

    if not top_users:
        await ctx.send("No pirates have made a name for themselves yet.")
        return

    message = "**Worst Generation - Top 5 Richest Pirates**\n"
    for i, (username, balance) in enumerate(top_users, start=1):
        message += f"{i}. {username} - {balance} Berries\n"

    await ctx.send(message)

bot.run(TOKEN)
