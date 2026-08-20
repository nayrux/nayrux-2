import discord
from discord.ext import commands
from config import Config

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.voice_states = True

bot = commands.Bot(command_prefix=Config.PREFIX, intents=intents)

@bot.event
async def on_ready():
    print(f"Conectado como {bot.user}")
    await bot.tree.sync()

async def setup_hook():
    await bot.load_extension("cogs.help")
    await bot.load_extension("cogs.voicemaster")

bot.setup_hook = setup_hook
bot.run(Config.TOKEN)
