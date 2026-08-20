import discord
from discord.ui import Select, View
from config import Config

class HelpSelect(Select):
    def __init__(self):
        options = [
            discord.SelectOption(label="Moderation", value="moderation", emoji=Config.ICONS["moderation"], description="Moderate your server"),
            discord.SelectOption(label="Security", value="security", emoji=Config.ICONS["security"], description="Protect your server"),
            discord.SelectOption(label="VoiceMaster", value="voicemaster", emoji=Config.ICONS["voicemaster"], description="Voice channel controls"),
            discord.SelectOption(label="Economy", value="economy", emoji=Config.ICONS["economy"], description="Earn money and buy items"),
            discord.SelectOption(label="Fun", value="fun", emoji=Config.ICONS["fun"], description="Fun commands and games"),
            discord.SelectOption(label="Information", value="information", emoji=Config.ICONS["information"], description="Server and user info"),
            discord.SelectOption(label="Tickets", value="tickets", emoji=Config.ICONS["tickets"], description="Ticket system"),
            discord.SelectOption(label="Giveaways", value="giveaways", emoji=Config.ICONS["giveaways"], description="Host giveaways"),
            discord.SelectOption(label="Invites", value="invites", emoji=Config.ICONS["invites"], description="Invite tracking"),
            discord.SelectOption(label="AI", value="ai", emoji=Config.ICONS["ai"], description="AI-powered commands"),
        ]
        super().__init__(placeholder="Select a category...", min_values=1, max_values=1, options=options)

    async def callback(self, interaction: discord.Interaction):
        category = self.values[0]
        await self.show_category_help(interaction, category)

    async def show_category_help(self, interaction: discord.Interaction, category: str):
        commands = self.get_commands_for_category(category)
        
        embed = discord.Embed(
            title=f"{Config.ICONS.get(category, '')} {category.title()} Commands",
            description="\n".join(commands),
            color=Config.BOT_COLOR
        )
        embed.set_footer(text="Select another category from the dropdown")
        
        await interaction.response.edit_message(embed=embed, view=HelpView())

    def get_commands_for_category(self, category: str):
        command_lists = {
            "moderation": [
                "`ban` - Ban a member",
                "`kick` - Kick a member",
                "`timeout` - Timeout a member",
                "`purge` - Delete messages",
                "`warn` - Warn a member",
                "`lock` - Lock a channel",
                "`unlock` - Unlock a channel",
            ],
            "security": [
                "`antinuke` - Protect against nuking",
                "`antiraid` - Prevent raids",
                "`antispam` - Anti-spam system",
                "`antilink` - Block links",
                "`antiinvite` - Block invites",
            ],
            "voicemaster": [
                "`voicemaster setup` - Setup VoiceMaster",
                "`voicemaster reset` - Reset configuration",
                " `lock` - Lock voice channel",
                " `unlock` - Unlock voice channel",
                " `hide` - Hide voice channel",
                " `reveal` - Reveal voice channel",
                " `rename` - Rename channel",
                " `increase` - Increase member limit",
                " `decrease` - Decrease member limit",
                " `info` - Channel information",
                " `kick` - Kick from channel",
                " `claim` - Claim ownership",
            ],
            "economy": [
                "`balance` - Check balance",
                "`daily` - Claim daily reward",
                "`work` - Work for money",
                "`shop` - Browse shop",
                "`buy` - Buy an item",
            ],
            "fun": [
                "`8ball` - Ask the magic 8-ball",
                "`meme` - Random meme",
                "`coinflip` - Flip a coin",
                "`roll` - Roll a dice",
                "`trivia` - Trivia game",
            ],
            "information": [
                "`userinfo` - User information",
                "`serverinfo` - Server information",
                "`ping` - Bot latency",
                "`uptime` - Bot uptime",
                "`avatar` - User avatar",
            ],
            "tickets": [
                "`ticket setup` - Setup ticket system",
                "`ticket new` - Create a ticket",
                "`ticket close` - Close ticket",
            ],
            "giveaways": [
                "`gw start` - Start a giveaway",
                "`gw end` - End a giveaway",
                "`gw reroll` - Reroll winners",
            ],
            "invites": [
                "`invites` - Check invites",
                "`inviter` - Who invited someone",
                "`invites lb` - Invite leaderboard",
            ],
            "ai": [
                "`ask` - Ask AI a question",
                "`translate` - Translate text",
                "`summarize` - Summarize text",
            ],
        }
        return command_lists.get(category, ["No commands found."])

class HelpView(View):
    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(HelpSelect())

class SupportButton(discord.ui.Button):
    def __init__(self):
        super().__init__(
            label="Support Server",
            url="https://discord.gg/zayybot",
            emoji="🔗",
            style=discord.ButtonStyle.link
        )

class CompleteHelpView(View):
    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(HelpSelect())
        self.add_item(SupportButton())
