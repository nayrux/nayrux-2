import discord
from discord.ext import commands
from config import Config
from views.help_select import CompleteHelpView
from utils.embeds import create_help_embed

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command(name="help", description="Show help menu")
    async def help_menu(self, ctx, category: str = None):
        if category:
            await ctx.send(f"Help for {category}")
            return
        
        embed = create_help_embed()
        view = CompleteHelpView()
        
        await ctx.send(embed=embed, view=view)

async def setup(bot):
    await bot.add_cog(Help(bot))
    
