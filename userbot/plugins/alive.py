import asyncio
from telethon import events
from userbot.utils import admin_cmd, edit_or_reply, sudo_cmd
from userbot import ALIVE_NAME, hellversion
from telethon.tl.types import ChannelParticipantsAdmins
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Hell User"

ludosudo = Config.SUDO_USERS

if ludosudo:
    sudou = "True"
else:
    sudou = "False"

kraken = bot.uid

PM_IMG = "https://telegra.ph/file/64f0450a2f15dfdb14b43.png"
pm_caption = "âž¥ **HyperShroud/PeruUserBot Is:** `Active`\n\n"
pm_caption += "âž¥ **SYSTEMS STATUS**\n"
pm_caption += f"☣HyperShroud☣ : `{hellversion}`\n"
pm_caption += "âž¥ **Telethon Version:** `1.15.0` \n"
pm_caption += "âž¥ **Python:** `3.9.0` \n"
pm_caption += f"âž¥ **Uptime** : `{uptime}` \n"
pm_caption += "âž¥ **Database Status:**  `Functional`\n"
pm_caption += "âž¥ **Current Branch** : `Master`\n"
pm_caption += f"âž¥ **Version** : `{currentversion}`\n"
pm_caption += f"âž¥ **My Peru Master** : {@NotShroudX97} \n"
pm_caption += "âž¥ **My Peru Assistant** : @HyperShroudXBot
pm_caption += "âž¥ **Heroku Database** : `AWS - Working Properly Noice`\n\n"
pm_caption += "âž¥ **License** : [GNU General Public License v3.0](github.com/NotShroudX97/HyperShroud/blob/master/LICENSE)\n"
pm_caption += "âž¥ **Copyright** : By [NotShroudX97@Github](GitHub.com/NotShroudX97)\n"
pm_caption += "âž¥ **Check Stats By Doing** `.stat`. \n\n"
pm_caption += "[Join My Gang Here @HyperMTKGang](t.me/HyperMTKGang)"

pm_caption += "☣The Creator God☣ : [Master Peru Saar Here](https://t.me/NotShroudX97)\n\n"

pm_caption += "[☣Repository☣](https://github.com/NotShroudX97/HyperShroud) [☣License☣](https://github.com/NotShroudX97/HyperShroud/blob/master/LICENSE)" [📜License📜](https://github.com/HellBoy-OP/HellBot/blob/master/LICENSE)"

@bot.on(admin_cmd(outgoing=True, pattern="alive$"))
@bot.on(sudo_cmd(pattern="alive$", allow_sudo=True))
async def amireallyalive(alive):
    chat = await alive.get_chat()
    await alive.delete()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG,caption=pm_caption)
    await alive.delete() 
