import logging
from nicegrill.modules._init import modules as mods, classes as classinfo
from .. import utils


class Help:

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.ERROR)

    async def helpxxx(message):
        funcs = {}
        for cls in mods:
            for func in mods[cls]:
                funcs.update(mods[cls])
        help = " ‎\n•{}•".format("<b>Help</b>".center(85))
        name = utils.get_arg(message)
        if name and name in funcs:
            for cmd in funcs:
                if name == cmd:
                    templ = (
                        "{}\n\n<b>Here's the help for</b> <i>{}</i> <b>command:</b>\n\n"
                        .format(help, cmd))
                    await message.edit(
                        templ + funcs[cmd].__doc__) if funcs[cmd].__doc__ else await message.edit(
                        "<b>No help found for that command</b>")
                    return
            for cls in classinfo:
                if name == cls:
                    templ = (
                        "{}\n\n<b>Here's the commands in</b> <i>{}</i> <b>module:</b>\n\n"
                        .format(help, cls))
                    await message.edit(
                        templ + ", ".join(classinfo[cls]))
                    return
        elif name and (name not in mods or name not in classinfo):
            await message.edit("<b>There's nothing found under that name</b>")
            return
        for cls in classinfo:
            help += "\n\n<b>⬤ {}:</b>\n<i>".format(cls)
            help += ", ".join(classinfo[cls]) + "</i>"
        await message.edit(help)

    async def supportxxx(message):
        await message.edit("<b>Join</b> <a href=https://t.me/c/1409290957>Here</a> <b>for support!</b>")
