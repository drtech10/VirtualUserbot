from ..utils import admin_cmd, edit_or_reply, sudo_cmd


@bot.on(admin_cmd(pattern="ja$"))
@bot.on(sudo_cmd(pattern="ja$", allow_sudo=True))
async def gn(event):
    await edit_or_reply(
        event,
       "** ජීවිතය අනියතය..☹️ මරණය නියතය 🙏 මහනවීම සැපය 🙏**",
    )

