import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    TOKEN = os.getenv("DISCORD_TOKEN")
    DATABASE_URL = os.getenv("DATABASE_URL", "")
    OWNER_ID = int(os.getenv("OWNER_ID", 0))
    
    # Configuración del bot
    PREFIX = "!"
    BOT_NAME = "Zayy"
    BOT_COLOR = 0x2B2D31  # Color gris oscuro como Zayy
    
    # Emojis/Iconos Unicode (sin emojis personalizados)
    ICONS = {
        "moderation": "🔨",
        "security": "🛡️",
        "voicemaster": "🎙️",
        "economy": "",
        "fun": "🎮",
        "information": "📊",
        "tickets": "🎫",
        "giveaways": "🎁",
        "invites": "📩",
        "ai": "🤖",
        "configuration": "🔧",
        "welcome": "👋",
        "boost": "",
        "backup": "💾",
        "afk": "😴",
        "emojis": "🔤",
        "counting": "🔢",
        "jail": "⛓️",
        "roblox": "🦴",
        "embeds": "📝",
        "suggestions": "💡",
        "autorole": "🎯",
        "autoreact": "😊",
        "autogreet": "👋",
        "reminders": "⏰",
        "logging": "",
        "audit": "",
        "owner": "👑",
        "help": "ℹ️",
        "integrations": "",
        "music": "🎵",
        "socials": "💬",
        "utilities": "🛠️"
    }