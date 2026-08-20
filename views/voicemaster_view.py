import discord
from discord.ui import Button, View, Modal, TextInput

class VoiceMasterView(View):
    """Vista con botones para VoiceMaster"""
    
    def __init__(self, channel_id=None):
        super().__init__(timeout=None)
        self.channel_id = channel_id

    @discord.ui.button(emoji="🔒", style=discord.ButtonStyle.gray, custom_id="voicemaster:lock")
    async def lock_button(self, interaction: discord.Interaction, button: Button):
        await interaction.response.send_message("🔒 Channel locked", ephemeral=True)

    @discord.ui.button(emoji="🔓", style=discord.ButtonStyle.gray, custom_id="voicemaster:unlock")
    async def unlock_button(self, interaction: discord.Interaction, button: Button):
        await interaction.response.send_message(" Channel unlocked", ephemeral=True)

    @discord.ui.button(emoji="👁️", style=discord.ButtonStyle.gray, custom_id="voicemaster:hide")
    async def hide_button(self, interaction: discord.Interaction, button: Button):
        await interaction.response.send_message("👁️ Channel hidden", ephemeral=True)

    @discord.ui.button(emoji="👁️‍🗨️", style=discord.ButtonStyle.gray, custom_id="voicemaster:reveal")
    async def reveal_button(self, interaction: discord.Interaction, button: Button):
        await interaction.response.send_message("️‍🗨️ Channel revealed", ephemeral=True)

    @discord.ui.button(emoji="✏️", style=discord.ButtonStyle.gray, custom_id="voicemaster:rename")
    async def rename_button(self, interaction: discord.Interaction, button: Button):
        modal = RenameModal()
        await interaction.response.send_modal(modal)

    @discord.ui.button(emoji="➖", style=discord.ButtonStyle.gray, custom_id="voicemaster:decrease")
    async def decrease_button(self, interaction: discord.Interaction, button: Button):
        await interaction.response.send_message(" Member limit decreased", ephemeral=True)

    @discord.ui.button(emoji="➕", style=discord.ButtonStyle.gray, custom_id="voicemaster:increase")
    async def increase_button(self, interaction: discord.Interaction, button: Button):
        await interaction.response.send_message("➕ Member limit increased", ephemeral=True)

    @discord.ui.button(emoji="📋", style=discord.ButtonStyle.gray, custom_id="voicemaster:info")
    async def info_button(self, interaction: discord.Interaction, button: Button):
        embed = discord.Embed(
            title="Voice Channel Info",
            description="Channel information here",
            color=0x2B2D31
        )
        await interaction.response.send_message(embed=embed, ephemeral=True)

    @discord.ui.button(emoji="", style=discord.ButtonStyle.gray, custom_id="voicemaster:kick")
    async def kick_button(self, interaction: discord.Interaction, button: Button):
        await interaction.response.send_message(" Kick member modal", ephemeral=True)

    @discord.ui.button(emoji="👑", style=discord.ButtonStyle.gray, custom_id="voicemaster:claim")
    async def claim_button(self, interaction: discord.Interaction, button: Button):
        await interaction.response.send_message("👑 Ownership claimed", ephemeral=True)

class RenameModal(Modal):
    def __init__(self):
        super().__init__(title="Rename Channel")
        self.name = TextInput(label="New Name", placeholder="Enter new channel name")
        self.add_item(self.name)

    async def on_submit(self, interaction: discord.Interaction):
        await interaction.response.send_message(f"Channel renamed to: {self.name.value}", ephemeral=True)
