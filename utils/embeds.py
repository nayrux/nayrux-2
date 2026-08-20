import discord
from config import Config

def create_embed(title=None, description=None, color=None, icon=None):
    """Crea un embed con el estilo de Zayy"""
    embed = discord.Embed(
        title=title,
        description=description,
        color=color or Config.BOT_COLOR
    )
    embed.set_footer(text=f"Zayy Bot • {Config.PREFIX}help")
    return embed

def create_help_embed():
    """Embed principal del help"""
    embed = discord.Embed(
        title="Zayy Help",
        description=(
            f"Use `{Config.PREFIX}help <command>` for help on a specific command.\n"
            f"Parameters in `<>` are required, `[]` are optional.\n"
            f"Join the [support server](https://discord.gg/zayybot) for more support."
        ),
        color=Config.BOT_COLOR
    )
    return embed
