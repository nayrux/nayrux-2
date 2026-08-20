import discord
from discord.ext import commands
from config import Config
from views.voicemaster_view import VoiceMasterView
from utils.embeds import create_embed

class VoiceMaster(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = {}

    @commands.hybrid_command(name="voicemaster", description="VoiceMaster commands")
    async def voicemaster(self, ctx):
        await ctx.send("Use `voicemaster setup` or `voicemaster reset`")

    @commands.hybrid_command(name="setup", description="Setup VoiceMaster system")
    async def setup(self, ctx):
        category = await ctx.guild.create_category_channel(
            name="VoiceMaster",
            reason="VoiceMaster Setup"
        )
        
        interface_channel = await ctx.guild.create_text_channel(
            name="interface",
            category=category,
            reason="VoiceMaster Setup"
        )
        
        voice_channel = await ctx.guild.create_voice_channel(
            name="Join to Create",
            category=category,
            reason="VoiceMaster Setup"
        )
        
        self.config[ctx.guild.id] = {
            "category": category.id,
            "interface": interface_channel.id,
            "voice": voice_channel.id
        }
        
        embed = discord.Embed(
            title="VoiceMaster Interface",
            description="Click the buttons below to control your voice channel!",
            color=Config.BOT_COLOR
        )
        embed.add_field(
            name="Controls",
            value=(
                "🔒 - `lock` the voice channel\n"
                "🔓 - `unlock` the voice channel\n"
                "️ - `hide` the voice channel\n"
                "👁️‍🗨️ - `reveal` the voice channel\n"
                "✏️ - `rename` the voice channel\n"
                "➖ - `decrease` the member limit\n"
                "➕ - `increase` the member limit\n"
                "📋 - `info` about the voice channel\n"
                "🔨 - `kick` someone from the voice channel\n"
                "👑 - `claim` ownership of the voice channel"
            ),
            inline=False
        )
        
        view = VoiceMasterView()
        await interface_channel.send(embed=embed, view=view)
        
        embed_setup = create_embed(
            title="VoiceMaster Setup Complete",
            description=f"VoiceMaster has been set up in {category.mention}\nInterface: {interface_channel.mention}"
        )
        await ctx.send(embed=embed_setup)

    @commands.hybrid_command(name="reset", description="Reset VoiceMaster configuration")
    async def reset(self, ctx):
        if ctx.guild.id in self.config:
            del self.config[ctx.guild.id]
        
        embed = create_embed(
            title="VoiceMaster Reset",
            description="VoiceMaster configuration has been reset"
        )
        await ctx.send(embed=embed)

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        if not after.channel:
            return
        
        guild_config = self.config.get(member.guild.id)
        if not guild_config:
            return
        
        if after.channel.id != guild_config.get("voice"):
            return
        
        category = member.guild.get_channel(guild_config["category"])
        temp_channel = await member.guild.create_voice_channel(
            name=f"{member.display_name}'s Channel",
            category=category
        )
        
        await member.move_to(temp_channel)
        
        if "temp_channels" not in guild_config:
            guild_config["temp_channels"] = {}
        guild_config["temp_channels"][temp_channel.id] = member.id

async def setup(bot):
    await bot.add_cog(VoiceMaster(bot))
