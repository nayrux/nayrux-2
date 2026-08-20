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
    print(f"Conectado como {bot.user} ({bot.user.id})")
    await bot.tree.sync()
    await bot.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.watching, name=f"{Config.PREFIX}help"
        )
    )


async def setup_hook():
    for cog in ["cogs.help", "cogs.voicemaster"]:
        await bot.load_extension(cog)


bot.setup_hook = setup_hook
bot.run(Config.TOKEN)
