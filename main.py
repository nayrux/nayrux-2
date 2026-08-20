import discord
from discord.ext import commands
from config import Config
from database import db
import os

# Intents necesarios
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.voice_states = True

# Bot
bot = commands.Bot(
    command_prefix=commands.when_mentioned_or(Config.PREFIX),
    intents=intents,
    help_command=None  # Desactivamos help por defecto
)

@bot.event
async def on_ready():
    print(f"✅ {bot.user.name} is online!")
    print(f"📊 Connected to {len(bot.guilds)} servers")
    print(f"🔧 Prefix: {Config.PREFIX}")
    
    # Conectar base de datos
    await db.connect()
    
    # Sincronizar comandos slash
    try:
        synced = await bot.tree.sync()
        print(f"🔄 Synced {len(synced)} slash commands")
    except Exception as e:
        print(f"❌ Error syncing: {e}")

@bot.event
async def on_guild_join(guild):
    print(f"➕ Joined {guild.name}")

@bot.event
async def on_guild_remove(guild):
    print(f" Left {guild.name}")

# Cargar cogs
async def load_cogs():
    cogs_folder = "cogs"
    for filename in os.listdir(cogs_folder):
        if filename.endswith(".py") and not filename.startswith("__"):
            cog_name = f"cogs.{filename[:-3]}"
            try:
                await bot.load_extension(cog_name)
                print(f"✅ Loaded {cog_name}")
            except Exception as e:
                print(f"❌ Error loading {cog_name}: {e}")

async def main():
    await load_cogs()
    await bot.start(Config.TOKEN)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())