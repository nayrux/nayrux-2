Sí, ya lo vi. Esta vez el **build pasó**, pero el bot se cae al arrancar:

```
File "/app/main.py", line 4, in <module>
    from database import db
File "/app/database.py", line 1, in <module>
    import motor.motor_asyncio
ModuleNotFoundError: No module named 'motor'
```

## ❌ **QUÉ PASA**

Tu `main.py` y `database.py` **siguen siendo la versión vieja** (del repo perdido), que usa **MongoDB** (`motor`). Ese código no es el mío: mi `main.py` no importa `database`, y no usa MongoDB.

Además, en las variables vi que Railway te sugiere agregar `DATABASE_URL` con una URL de MongoDB → **NO la agregues**, no la necesitamos.

---

## ✅ **SOLUCIÓN**

**1.** En GitHub abre **main.py** → lápiz (edit) → **borra TODO** → pega esto → Commit:

```python
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
```

**2.** **database.py**: déjalo como está por ahora. Al no ser importado, ya no romperá nada. Lo reescribiremos (con SQLite, sin MongoDB) cuando agreguemos economía y demás sistemas.

**3.** Verifica que tu **config.py** sea la versión que te di (con `Config.TOKEN`, `Config.PREFIX`, `Config.ICONS`).

---

## ⚠️ **IMPORTANTE: TU TOKEN QUEDÓ EXPUESTO**

En la captura se ve tu token real (`MTUzOTgz...`). Cualquier persona con ese token controla tu bot. Haz esto **ahora**:

1. [discord.com/developers/applications](https://discord.com/developers/applications) → tu app → **Bot** → **Reset Token**
2. Copia el token nuevo
3. En Railway → **Variables** → edita `DISCORD_TOKEN` con el nuevo valor

(De ahora en adelante, no compartas capturas donde se vea el token.)

---

Con el commit del `main.py`, Railway redeploya solo. El log correcto debe decir:

```
Conectado como TuBot#1234 (1234567890)
```

Avísame cuando lo veas y probamos `,help` y `,voicemaster` en Discord.
