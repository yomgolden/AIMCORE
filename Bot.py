import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True  # Important so your bot can read messages

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user} (ID: {bot.user.id})")
    print("Bot is online and ready.")

@bot.command()
async def ping(ctx):
    await ctx.send("🏓 Pong! (from Aimcore Bot)")

bot.run(os.getenv("DISCORD_TOKEN"))
