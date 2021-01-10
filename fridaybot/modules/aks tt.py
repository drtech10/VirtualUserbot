from ..utils import admin_cmd, edit_or_reply, sudo_cmd


@bot.on(admin_cmd(pattern="aks$"))
@bot.on(sudo_cmd(pattern="aks$", allow_sudo=True))
async def gn(event):
    await edit_or_reply(
        event,
       "** අනියම් කාම සේවනය තරයේ හෙලා දකිමි 🙈 **",
    )

